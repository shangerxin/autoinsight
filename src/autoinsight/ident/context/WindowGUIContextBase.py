from abc import ABC
from time import sleep
from typing import Optional, Iterable, Any, Mapping, Tuple, Union

from pywinauto import Desktop, Application, WindowSpecification
from pywinauto.controls.uiawrapper import UIAWrapper
from pywinauto.findbestmatch import MatchError

from autoinsight.common.CustomTyping import AutomationInstance, ElementsInfo, FoundCtrlItem
from autoinsight.common.Utils import matchScore, isIEqual, isSimilar, first, similarRate
from autoinsight.decorator.Log import log, Log
from autoinsight.ident.target.TargetBase import TargetBase
from autoinsight.ident.context.GUIContextBase import GUIContextBase


class WindowGUIContextBase(GUIContextBase, ABC):
    _desktop = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def _isContainerTypes(self, classname: str) -> bool:
        return any(similarRate(classname, c) > 0.5 for c in self.containers)

    def _isSimilarTypes(self, classname, types: Iterable[str]) -> bool:
        return any(similarRate(classname, t) > 0.5 for t in types)

    def _getAllCtrlMapFromElementsInfo(self, info: ElementsInfo, target: TargetBase = None) -> Iterable[Tuple[Iterable[Any], Mapping[int, Iterable[str]]]]:
        allCtrlMapPairs = []
        children = []
        ctrlInfo = info
        while True:
            if target:
                invalidIndexes = (i for i, c in enumerate(ctrlInfo.allCtrl) if not (self._isSimilarTypes(c.friendly_class_name(), target.aliases)
                                                                                    or self._isContainerTypes(c.friendly_class_name())))
                for index in invalidIndexes:
                    if index in ctrlInfo.allCtrlIndexNameMaps:
                        del ctrlInfo.allCtrlIndexNameMaps[index]

            allCtrlMapPairs.append((ctrlInfo.allCtrl, ctrlInfo.allCtrlIndexNameMaps))
            for index in ctrlInfo.allCtrlIndexNameMaps.keys():
                ctrl = ctrlInfo.allCtrl[index]
                if hasattr(ctrl, 'allCtrl') and ctrl.allCtrl:
                    children.append(ctrl)

            if children:
                ctrlInfo = children.pop()
            else:
                break
        return allCtrlMapPairs

    def _getTexts(self, ctrl: UIAWrapper) -> str:
        texts = []
        if ctrl:
            try:
                texts.append(ctrl.window_text())
                texts.append(ctrl.friendly_class_name())
            except:
                pass
        return texts

    def _getAllCtrlMapFromUIAWrapper(self, info: UIAWrapper, target: TargetBase = None) -> Iterable[Tuple[Iterable[Any], Mapping[int, Iterable[str]]]]:
        allCtrlMapPairs = []
        children = []
        ctrlInfo = info

        while True:
            infoChildren = ctrlInfo.children()
            infoCtrlIndexNameMaps = {k: self._getTexts(v) for k, v in enumerate(infoChildren)}

            if target:
                invalidIndexes = [i for i, c in enumerate(infoChildren) if not (self._isSimilarTypes(c.friendly_class_name(), target.aliases)
                                                                                or self._isContainerTypes(c.friendly_class_name()))]
                for index in invalidIndexes:
                    del infoCtrlIndexNameMaps[index]

            allCtrlMapPairs.append((infoChildren, infoCtrlIndexNameMaps))
            for index in infoCtrlIndexNameMaps.keys():
                ctrl = infoChildren[index]
                children.append(ctrl)

            if children:
                ctrlInfo = children.pop()
            else:
                break

        return allCtrlMapPairs

    def _getAllCtrlMap(self, info: Union[ElementsInfo, UIAWrapper], target: TargetBase = None) -> Iterable[Tuple[Iterable[Any], Mapping[int, Any]]]:
        if isinstance(info, ElementsInfo):
            return self._getAllCtrlMapFromElementsInfo(info, target)
        elif isinstance(info, UIAWrapper):
            return self._getAllCtrlMapFromUIAWrapper(info, target)

    def _getMaxScoreItem(self, controls: Iterable[FoundCtrlItem], target: TargetBase) -> Optional[Any]:
        if controls:
            firstIndex, score, secondSore = 0, 1, 2
            controls.sort(key=lambda x: x[score], reverse=True)
            controls = [c for c in controls if controls[firstIndex][score] == c[score]]
            controls.sort(key=lambda x: x[secondSore], reverse=True)

            if len(controls) > 1 and target:
                firstCandidate = controls[firstIndex]
                candidates = [x for x in filter(lambda x: firstCandidate[score] == x[score] and firstCandidate[secondSore] == x[secondSore], controls)]
                return first(candidates, isRevert=True, sortKeyFunc=lambda x: similarRate(x.ctrl.friendly_class_name(), target.classname)).ctrl

            return controls[firstIndex].ctrl

    def _getClickable(self, ctrl: Any, foundIndex: int) -> Any:
        if ctrl and isIEqual(ctrl.friendly_class_name(), 'Hyperlink'):
            index = -1
            controls = ctrl.parent().children()
            for i, c in enumerate(controls):
                if c == ctrl:
                    index = i
                    break

            for i in range(index - 1, -1, -1):
                ctrl = ctrl.parent().children()[i]
                if isIEqual(ctrl.friendly_class_name(), 'Button'):
                    return ctrl

        return ctrl

    def _getElementInfo(self, context: Any, query, target: TargetBase) -> ElementsInfo:
        try:
            if isinstance(context, Application):
                context = context.top_window()
            elif isinstance(context, UIAWrapper):
                return context

            return context.get_elements_info(depth=self._searchDepth, max_width=self._searchWidth)
        except MatchError:
            return self._findFromDesktop(query, target, context)

    def _findFromDesktop(self, query: str, target: TargetBase, context: ElementsInfo) -> Any:
        window: WindowSpecification = None
        for w in self.desktop.windows():
            if w.process_id() == self.processId and w.is_active() and not isSimilar(w.friendly_class_name(), 'tooltip'):
                window = w
                break

        if not window:
            window = WindowGUIContextBase.desktop.top_from_point(self.rectangle.center.x, self.rectangle.center.y)

        if window:
            self._automationInstance = window
            window.wait_for_idle()
            return window

    @property
    def parent(self) -> Any:
        if not self._parent:
            self._parent = self.desktop
        return self._parent

    @classmethod
    @property
    def desktop(cls) -> Desktop:
        if not cls._desktop:
            cls._desktop = Desktop(backend="uia")
        return cls._desktop

    def _toStr(self, value):
        try:
            return str(value)
        except:
            return ""

    @log
    def find(self, query: str, target: TargetBase = None, *args, **kwargs) -> Optional[AutomationInstance]:
        if self.automationInstance:
            try:
                info: ElementsInfo = self._getElementInfo(self.automationInstance, query, target)
                allCtrlMapPairs = self._getAllCtrlMap(info, target)
                foundControls = []
                for pair in allCtrlMapPairs:
                    bestIndex, bestScore, bestSecond = -1, -1, -1
                    allCtrl, allCtrlIndexMaps = pair
                    otherCandidateIndexes = []
                    for index, names in allCtrlIndexMaps.items():
                        score, secondScore = matchScore(query, names)
                        if score > bestScore:
                            bestIndex = index
                            bestScore = score
                            bestSecond = secondScore
                            otherCandidateIndexes.clear()

                        elif score == bestScore and secondScore > bestSecond:
                            bestIndex = index
                            bestScore = score
                            bestSecond = secondScore
                            otherCandidateIndexes.clear()

                        elif score > 0 and secondScore > 0 and score == bestScore and secondScore == bestSecond:
                            otherCandidateIndexes.append(index)

                    if bestIndex > -1 and bestScore > 0 and bestSecond > 0:
                        foundControls.append(FoundCtrlItem(allCtrl[bestIndex], bestScore, bestSecond, bestIndex))

                        if otherCandidateIndexes:
                            for index in otherCandidateIndexes:
                                foundControls.append(FoundCtrlItem(allCtrl[index], bestScore, bestSecond, index))
                            otherCandidateIndexes.clear()

                if foundControls:
                    ctrl = self._getMaxScoreItem(foundControls, target)
                    return ctrl
                else:
                    Log.logger.warning(f"Find target {self._toStr(target)} failed with {query} in context {self._toStr(self.automationInstance)}")

            except Exception as e:
                Log.logger.warning("Find %s from context failed with error %s", query, e)
                return
