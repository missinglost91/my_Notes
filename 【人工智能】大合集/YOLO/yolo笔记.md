# yolo学习笔记

## uv环境配置

不多说了

```bash
uv add ultralytics
```

```python
from ultralytics import YOLO
import checkdevice
device = checkdevice.check_device()
model = YOLO("yolov8n.pt").to(device)
```


interGPU的配置还要做如下修改

![20260213194524](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/20260213194524.png)

```

```
![20260213194210](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/20260213194210.png)

  

![20260213194858](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/20260213194858.png)

## 命令行

```bash
yolo detect predict model=yolov8n.pt source="211.jpg"
```

第一个yolo
```python
yolo=YOLO("yolov8n.pt",task="detect").to(device)
result=yolo.predict(source="1.jpg",save=True)
```

```python
display(result[0].names)
```


数据标注
![20260213162651](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/20260213162651.png)

![20260213175935](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/20260213175935.png)

有时会出现保存不想要的文件夹的目录的情况

yolo i