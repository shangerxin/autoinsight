

# export
```
yolo export model=yolov8n-cls.pt format=onnx imgsz=224,128
```

# train
```
yolo detect train data=coco128.yaml model=yolov8n.pt epochs=100 imgsz=640
```


# Predict
```
yolo detect predict model=yolov8n.pt source='https://ultralytics.com/images/bus.jpg'
```


# Default configuration
```
yolo copy-cfg
yolo cfg=default_copy.yaml imgsz=320
```


# Validate trained yolov8n model accuracy
```
yolo detect val model=yolov8n.pt
```
