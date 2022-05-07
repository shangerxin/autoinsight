from enum import Enum

import autoinsight.extend.ExtendEnum  # noqa:F401


class OSTypes(Enum):
    Any = "Any"
    Windows = "Windows"
    Linux = "Linux"
    Java = "Java"
    MacOS = "Darwin"
