import os
import re
import shutil
import logging
import platform

from enum import Enum
from difflib import get_close_matches, SequenceMatcher
from typing import Collection, Tuple, Iterable, Callable, Any, Optional, Union
from uuid import uuid4, UUID
from pathlib import Path
from time import strftime, gmtime, time_ns

from .EnumTypes import BinaryTypes, OSTypes


def GUID() -> UUID:
    return uuid4()


def strGUID() -> str:
    return str(uuid4())


def strToGUID(strGuid: str):
    return UUID(f"{strGuid}")


# TODO refactor the method
def toUniqueList(items: Iterable[str]) -> Collection[str]:
    uniqueList = []
    illegal = -1
    patterns = [r"\d", "[a-z]", "[A-Z]", r"\W", r"[^\d|a-z|A-Z|\s|\W]"]

    for item in items:
        if isinstance(item, str) and not item.strip():
            continue

        words = re.split(r"\s", item)
        for word in words:
            previous = None
            splitIndexes = []
            for i, c in enumerate(word):
                for p in patterns:
                    if re.search(p, c) and previous != p:
                        splitIndexes.append(i)
                        previous = p
                        break

            length = len(splitIndexes)
            for i, v in enumerate(splitIndexes):
                j = i + 1
                if j < length:
                    if v + 1 == splitIndexes[j]:
                        splitIndexes[j] = illegal

            if length - splitIndexes.count(illegal) < 2:
                frag = word.lower()
                if frag not in uniqueList:
                    uniqueList.append(frag)

                continue

            i = 0
            for j in splitIndexes[1:]:
                if j == illegal:
                    continue
                frag = word[i:j].lower()
                if frag not in uniqueList:
                    uniqueList.append(frag)
                i = j

            frag = word[i:].lower()
            if frag not in uniqueList:
                uniqueList.append(frag)

    return uniqueList


def toAllPossibleGroups(items: Iterable[str]) -> Collection[str]:
    possibles = []
    for i in range(1, len(items) + 1):
        possibles.append(' '.join(items[:i]))
    return possibles


def matchScore(query: str, descriptions: Iterable[str]) -> Tuple[float, float]:
    if not (descriptions and query):
        return 0.0, 0.0

    unique = toUniqueList(descriptions)
    if unique:
        words = toUniqueList(re.split(r"\s", query))
        possibles = toAllPossibleGroups(words)
        matchCount = 0
        possibleCount = 0
        for word in words:
            matches = get_close_matches(word, unique)
            matchCount += len(matches)

        for possible in possibles:
            matches = get_close_matches(possible, unique)
            possibleCount += len(matches)

        lengthUnique = len(unique)
        lengthWord = len(words)
        maxLength = max(lengthUnique, lengthWord)
        firstScore = possibleCount / lengthWord
        secondScore = (firstScore + matchCount) / maxLength
        return firstScore, secondScore
    else:
        return 0.0, 0.0


def isComparable(obj: Any) -> bool:
    try:
        obj < obj
        return True
    except:
        return False


def first(collection: Iterable[Any], isRevert: bool = False, filterFunc: Callable[Any, bool] = None, sortKeyFunc: Optional[Callable[Any, int]] = None, isSort: bool = True) -> Any:
    try:
        if not collection:
            return

        collection = tuple(collection)
        isSort = isComparable(collection[0]) and isSort
        if not (isSort or sortKeyFunc):
            return next(filter(filterFunc, collection))
        else:
            return next(filter(filterFunc, sorted(collection, key=sortKeyFunc, reverse=isRevert)))
    except StopIteration:
        return


def isIEqual(str0: str, str1: str) -> bool:
    """
    Test two strings are ignored case equaled
    """
    if isinstance(str1, str) and isinstance(str0, str):
        return str0.lower() == str1.lower()
    else:
        return False


def isSimilar(str0: Union[str, Enum], str1: Union[str, Enum]) -> bool:
    """
    Check two strings are similar or not

    Args:
        str0 (str): First string
        str1 (str): Second string

    Returns:
        bool: return True if the two strings contain similar contents.
    """
    return SequenceMatcher(None, str(str0).lower(), str(str1).lower()).ratio() > 0.2


def similarRate(str0: Union[str, Enum], str1: Union[str, Enum]) -> float:
    """
    Check two strings are similar or not

    Args:
        str0 (str): First string
        str1 (str): Second string

    Returns:
        bool: return True if the two strings contain similar contents.
    """
    return SequenceMatcher(None, str(str0).lower(), str(str1).lower()).ratio()


def makeDirs(path: str, isRecreate: bool = False):
    isExist = os.path.isdir(path)
    if isRecreate and isExist:
        try:
            shutil.rmtree(path)
        except Exception as e:
            logging.warning("Call makeDirs with ", path, isRecreate, " failed with error", e)
            pass

    elif isExist:
        return

    else:
        os.makedirs(path)


def decorateFileName(name: str) -> str:
    p = Path(name)

    if p.parent and str(p.parent) != ".":
        parent = p.parent
    else:
        parent = ""

    return f'{parent}{strftime("UTC%Y%m%d-%H%M%S", gmtime())}.{str(time_ns())[-9:-6]}-{p.name}'


def getOSType() -> OSTypes:
    platform = platform.system()
    if platform == OSTypes.Windows.name:
        return OSTypes.Windows
    elif platform == OSTypes.MacOS.name:
        return OSTypes.MacOS
    elif platform == OSTypes.Linux.name:
        return OSTypes.Linux
    elif platform == OSTypes.Java.name:
        return OSTypes.Java
    else:
        return OSTypes.Any


def getExecutableBinaryTypes(path: Path) -> bool:
    if getOSType() == OSTypes.Windows:
        import win32file

        if path.exists():
            binaryType = win32file.GetBinaryType(path)
            if binaryType == win32file.SCS_32BIT_BINARY:
                return BinaryTypes.Bit32
            elif binaryType == win32file.SCS_DOS_BINARY         \
                    or binaryType == win32file.SCS_WOW_BINARY   \
                    or binaryType == win32file.SCS_PIF_BINARY   \
                    or binaryType == win32file.SCS_OS216_BINARY \
                    or binaryType == win32file.SCS_POSIX_BINARY:
                return BinaryTypes.Bit16
            else:
                return BinaryTypes.Bit64

    # TODO: Add for other OS
    return BinaryTypes.Bit32
