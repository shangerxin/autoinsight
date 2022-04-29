from uuid import uuid4, UUID


def GUID():
    return uuid4()

def strGUID():
    return str(uuid4())

def strToGUID(strGUID:str):
    return UUID(f'{strGUID}')
