import os
from typing import Union, NewType, Optional
from multiprocessing import Process

from pywinauto import Desktop, WindowSpecification
from pywinauto.win32_element_info import HwndElementInfo
from pywinauto.uia_element_info import UIAElementInfo

from autoinsight.common.models.Knowledge import Knowledge
from .KnowledgeServiceBase import KnowledgeServiceBase

WindowAutomationInstance = NewType("WindowAutomationInstance", Optional[Union[UIAElementInfo, HwndElementInfo]])


class WindowKnowledgeService(KnowledgeServiceBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.knowledge.append(Knowledge(alias=["windowscamera",
                                               "windowscamera.exe",
                                               "camera",
                                               "camera.exe",
                                               "microsoft.windows.camera"],
                                        launch=_launchCamera))

        self.knowledge.append(Knowledge(alias=["control panel"],
                                        launch=_launchControlPanel))

        self.knowledge.append(Knowledge(alias=["settings"],
                                        launch=_launchSettings))

    def recognize(self, name: str) -> WindowAutomationInstance:
        knowledge = None
        if name:
            name = name.lower()
            for k in self.knowledge:
                if name in k.alias:
                    knowledge = k
                    break

        if knowledge:
            return knowledge.launch(knowledge)

    def __repr__(self):
        pass

    def __str__(self):
        pass

    def wait(self, timeoutSeconds: int = 0):
        pass


def __camera_worker():
    os.system('cmd /C "start microsoft.windows.camera: "')


def _launchCamera(knowledge: Knowledge) -> WindowAutomationInstance:
    worker = Process(target=__camera_worker, args=knowledge.arguments)
    worker.start()
    camera = WindowSpecification({"backend": "uia", "best_match": "Camera"})
    camera.wait("exists visible ready", timeout=30, retry_interval=3)
    return camera


def _launchControlPanel() -> WindowAutomationInstance:
    pass


def _launchSettings() -> WindowAutomationInstance:
    pass
