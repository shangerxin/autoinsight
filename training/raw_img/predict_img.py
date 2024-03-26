from ultralytics import YOLO
from PIL import Image
import cv2


model = YOLO(r"C:\Users\erxinsha\projects\autoinsight\training\raw_img\yolov8l_custom.pt")
results = model.predict(source=r"C:\Users\erxinsha\projects\autoinsight\training\raw_img\confulence_wiki_page_29.jpg", show=False, save=True, save_txt=True, line_width=1, save_conf=True, conf=0.6)

# https://docs.ultralytics.com/reference/engine/results/#ultralytics.engine.results.Boxes
print("=======================RESULT=====================")
for result in results:
    result = result.numpy()
    box_xy = result.boxes.xyxy
    box_xywh = result.boxes.xywh
    conf = result.boxes.conf
    class_num = result.boxes.cls





    print("===========================")
    print("box_xy: ", box_xy)  # (N, 4)
    print("box_xywh: ", box_xywh) # (N, 4)
    print("conf: ", conf)  # (N, 1)
    print("class_num: ", class_num)  # 0: button_create 1: search_box 2: start_bar

