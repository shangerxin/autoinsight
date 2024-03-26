from typing import Iterable

from ultralytics import YOLO

from .AIServiceBase import AIServiceBase
from autoinsight.common.models.Rectangle import Rectangle
from autoinsight.common.models.IdentResult import IdentResult


class YoloAIService(AIServiceBase):
    def __init__(self, *args, **kwargs):
        self._model = YOLO(r"C:\Users\erxinsha\projects\autoinsight\training\raw_img\yolov8l_custom.pt")

    # 0: button_create   1: search_box   2: start_bar
    def predict(self, image) -> Iterable[IdentResult]:
        results = self._model.predict(source=image, show=False, save=True, save_txt=True, line_width=1, save_conf=True, conf=0.6)

        identResults = []
        for result in results:
            result = result.numpy()
            boxes = result.boxes
            for i, box in enumerate(boxes.xywh):
                confidence = boxes.conf[i]
                classnum = boxes.cls[i]
                left, top, width, height = (int(x) for x in box)
                identResults.append(IdentResult(Rectangle(left, top, width, height), confidence, classnum))

        return identResults
