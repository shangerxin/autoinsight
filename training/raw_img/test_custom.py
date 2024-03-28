from ultralytics import YOLO

model = YOLO("yolov8l_custom.pt")

result=model.predict(source="confulence_wiki_page_29.jpg", show=False, save=True, save_txt=True, line_width=1, save_conf=True, conf=0.6)

print("=====================Result================")
print(result)
print("=====================End==================")