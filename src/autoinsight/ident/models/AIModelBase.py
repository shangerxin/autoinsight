from __future__ import annotations

from pathlib import Path

from abc import abstractmethod
from uuid import UUID

from autoinsight.common.ObjectBase import ObjectBase
from autoinsight.common.Utils import GUID
from autoinsight.common.CustomTyping import PathStr


class AIModelBase(ObjectBase):
    def load(self, pretrain_model_path: PathStr):
        pass

    def ident(self, image_path: PathStr):
        pass

    def _train(self, *args):
        pass

    def _export(self, *args):
        pass
