from __future__ import annotations
from itertools import chain

from typing import Any, Optional, Dict, Sequence

from .Step import Step
from autoinsight.decorator.Log import log, Log


class Record(Step):
    _records: Dict[str, list[Record]] = {}

    def __init__(self, value: Any, recordKey: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._value = value
        self._recordKey = str
        self._addRecord(recordKey, self)

    @log
    def execute(self, isPaused: bool = False):
        Log.logger.info("Execute %s", self)
        self._isExecuted = True

    @property
    def value(self) -> Any:
        return self._value

    @classmethod
    @log
    def records(cls, recordKey: Optional[str] = None) -> Sequence[Record]:
        if recordKey and recordKey in cls._records:
            return cls._records[recordKey]
        else:
            return tuple(chain(*cls._records.values()))

    @classmethod
    @log
    def _addRecord(cls, key: str, record: Record):
        if key in cls._records:
            cls._records[key].append(record)
        else:
            cls._records.setdefault(key, [record])
