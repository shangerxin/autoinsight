import os

fixturePath = os.path.dirname(__file__)
fixtureImageRoot = os.path.join(fixturePath, "images")


def imagePath(name: str) -> str:
    return os.path.join(fixtureImageRoot, name)
