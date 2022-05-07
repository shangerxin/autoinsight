import re
from typing import Iterable
from uuid import uuid4, UUID


def GUID() -> UUID:
    return uuid4()


def strGUID() -> str:
    return str(uuid4())


def strToGUID(strGuid: str):
    return UUID(f'{strGuid}')


def toUniqueList(items: Iterable[str]) -> Iterable[str]:
    uniqueList = []
    illegal = -1
    patterns = [r'\d', '[a-z]', '[A-Z]', r'\W', r'[^\d|a-z|A-Z|\s|\W]']
    isMatchChanged = lambda pattern, char: re.search(pattern, char) and previous != pattern

    for item in items:
        if isinstance(item, str) and not item.strip():
            continue

        words = re.split(r'\s', item)
        for word in words:
            previous = None
            splitIndexes = []
            for i, c in enumerate(word):
                for p in patterns:
                    if isMatchChanged(p, c):
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
