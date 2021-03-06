import os
import re
import shutil
import logging
from difflib import get_close_matches
from typing import Collection, Tuple, Iterable
from uuid import uuid4, UUID
from pathlib import Path
from time import strftime, gmtime, time_ns


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


def matchScore(query: str, descriptions: Iterable[str]) -> Tuple[float, float]:
    if not (descriptions and query):
        return 0.0, 0.0

    unique = toUniqueList(descriptions)
    if unique:
        words = toUniqueList(re.split(r"\s", query))
        matchCount = 0
        for word in words:
            matches = get_close_matches(word, unique)
            matchCount += len(matches)

        return matchCount / len(words), matchCount / len(unique)
    else:
        return 0.0, 0.0


def isIEqual(str0: str, str1: str) -> bool:
    """
    Test two strings are ignored case equaled
    """
    if isinstance(str1, str) and isinstance(str0, str):
        return str0.lower() == str1.lower()
    else:
        return False


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
