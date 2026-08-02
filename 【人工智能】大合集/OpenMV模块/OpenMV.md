# OpenMV入门到精通
编写:关山难
______
## 初入门

### IDE主界面

![](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/20251007200421.png)

### 学习网站

星瞳官网
[序言 · OpenMV中文入门教程](https://book.openmv.cc/)

库函数大全
[概述 — MicroPython 1.22 文档](https://docs.singtown.com/micropython/zh/latest/openmvcam/index.html)


## 图像处理方法

```python
import sensor #引入感光元件模块
import time #引入时间模块
```



### 使用统计信息

```python

while True:
    clock.tick()  # Update the FPS clock.
    
    img = sensor.snapshot()  # 使用sensor库中的snapshot函数拍张照片，命名为img对象
    statistics=img.get_statistics(roi=(0,0,10,20)) #对 img对象 使用get_statistics方法【统计roi（感兴趣区域）内的所有信息】，后果传到statistics对象
    color_l=statistics.l_mode() #对statistics使用l_mode方法【求L通道的平均数】，结果传到 color_l 对象
    color_a=statistics.a_mode()
    color_b=statistics.b_mode()
    x=statistics.mean() # 对statistics使用mean方法【灰度的平均数】，结果传到 x 对象
    print(color_l,color_a,color_b)
    
    
```

各种方法：
![](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/1acd63c3dd47147200aeb67ea4dcb4d6.png)

举例

检测左上方的区域中的颜色值。

```python
import sensor, image, time

sensor.reset() # 初始化摄像头
sensor.set_pixformat(sensor.RGB565) # 格式为 RGB565.
sensor.set_framesize(sensor.QVGA)
sensor.skip_frames(10) # 跳过10帧，使新设置生效
sensor.set_auto_whitebal(False)               # Create a clock object to track the FPS.

ROI=(80,30,15,15)

while(True):
    img = sensor.snapshot()         # Take a picture and return the image.
    statistics=img.get_statistics(roi=ROI)
    color_l=statistics.l_mode()
    color_a=statistics.a_mode()
    color_b=statistics.b_mode()
    print(color_l,color_a,color_b)
    img.draw_rectangle(ROI)  # 在图像上绘制一个矩形，您可以分别传递 x、y、w、h
```

`img.draw_rectangle(ROI)` 在图像上绘制一个矩形,效果如图
![](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/d64f2ad6b34d26d36f57b7286b414dc9.png)

### 画图


视觉系统通常需要给使用者提供一些反馈信息。直接在图像中显示出来，很直观。就像[10分钟快速上手](https://book.openmv.cc/quick-starter.html)的程序中一样，当找到色块，把这个区域用矩形框标注出来，这样非常直观。

注意：

- 颜色可以是灰度值(0-255)，或者是彩色值(r, g, b)的tupple。默认是白色。
    
- 其中的color关键字必须**显示**的标明**color=**。例如：
    
```
image.draw_line((10,10,20,30), color=(255,0,0))
image.draw_rectangle(rect_tuple, color=(255,0,0))
```

#### 画线

- image.draw_line(line_tuple, color=White) 在图像中画一条直线。
    - line_tuple的格式是(x0, y0, x1, y1)，意思是(x0, y0)到(x1, y1)的直线。
    - 颜色可以是灰度值(0-255)，或者是彩色值(r, g, b)的tupple。默认是白色

#### 画框

- image.draw_rectangle(rect_tuple, color=White) 在图像中画一个矩形框。
    - rect_tuple 的格式是 (x, y, w, h)。

#### 画圆

- image.draw_circle(x, y, radius, color=White) 在图像中画一个圆。
    - x,y是圆心坐标
    - radius是圆的半径

#### 画十字

- image.draw_cross(x, y, size=5, color=White) 在图像中画一个十字
    - x,y是坐标
    - size是两侧的尺寸

#### 写字

- image.draw_string(x, y, text, color=White) 在图像中写字 8x10的像素
    - x,y是坐标。使用\n, \r, and \r\n会使光标移动到下一行。
    - text是要写的字符串。
#### 画关键点

cv2.drawKeypoints(image, keypoints, outImage, color=None, flags=None)

```python
 img.draw_keypoints( #用于在图像上绘制关键点的函数
            [(blob.cx(), blob.cy(), int(math.degrees(blob.rotation())))], size=20
        )
```
- **image**: 原始图像，可以是三通道或单通道图像。
    
- **keypoints**: 特征点向量，每个元素是一个 KeyPoint 对象，包含特征点的各种属性信息。
    
- **outImage**: 特征点绘制的画布图像，可以是原图像。
    
- **color**: 绘制特征点的颜色信息，默认绘制的是随机彩色。
    
- **flags**: 绘图功能的标识设置。

![](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/630c0b96025fedf349fd27ce97e18c58.png)

#### 例子

```
import sensor, image, time

sensor.reset() # 初始化摄像头
sensor.set_pixformat(sensor.RGB565) # 格式为 RGB565.
sensor.set_framesize(sensor.QQVGA)
sensor.skip_frames(10) # 跳过10帧，使新设置生效

while(True):
    img = sensor.snapshot()         #拍照
    img.draw_line((20, 30, 40, 50)) 
    img.draw_line((80, 50, 100, 100), color=(255,0,0))
    img.draw_rectangle((20, 30, 41, 51), color=(255,0,0))
    img.draw_circle(50, 50, 30)
    img.draw_cross(90,60,size=10)
    img.draw_string(10,10, "hello world!")
```

![](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/fcdd7f0919a5a767bd5a7018cf88b163.png)

### 寻找色块

#### 代码

```python

red = (minL, maxL, minA, maxA, minB, maxB)


image.find_blobs(
	thresholds, #颜色阈值
	roi=Auto, # 感兴趣区域
	x_stride=2, #
	y_stride=1, #
	invert=False, #颜色翻转
	area_threshold=10, #面积阈值
	pixels_threshold=10, #像素个数阈值
	merge=False, #颜色框框合并
	margin=0,  
	threshold_cb=None,
	merge_cb=None) 
	
	
	
	
```


#### blog的方法

blob有多个方法：

- blob.rect() 返回这个色块的外框——矩形元组(x, y, w, h)，可以直接在image.draw_rectangle中使用。
    
- blob.x() 返回色块的外框的x坐标（int），也可以通过blob[0]来获取。
    
- blob.y() 返回色块的外框的y坐标（int），也可以通过blob[1]来获取。
    
- blob.w() 返回色块的外框的宽度w（int），也可以通过blob[2]来获取。
    
- blob.h() 返回色块的外框的高度h（int），也可以通过blob[3]来获取。
    
- blob.pixels() 返回色块的像素数量（int），也可以通过blob[4]来获取。
    
- blob.cx() 返回色块的外框的中心x坐标（int），也可以通过blob[5]来获取。
    
- blob.cy() 返回色块的外框的中心y坐标（int），也可以通过blob[6]来获取。
    
- blob.rotation() 返回色块的旋转角度（单位为弧度）（float）。如果色块类似一个铅笔，那么这个值为0~180°。如果色块是一个圆，那么这个值是无用的。如果色块完全没有对称性，那么你会得到0~360°，也可以通过blob[7]来获取。
    
- blob.code() 返回一个16bit数字，每一个bit会对应每一个阈值。举个例子：
    
    blobs = img.find_blobs([red, blue, yellow], merge=True)
    

如果这个色块是红色，那么它的code就是0001，如果是蓝色，那么它的code就是0010。注意：一个blob可能是合并的，如果是红色和蓝色的blob，那么这个blob就是0011。这个功能可以用于查找颜色代码。也可以通过blob[8]来获取。

- blob.count() 如果merge=True，那么就会有多个blob被合并到一个blob，这个函数返回的就是这个的数量。如果merge=False，那么返回值总是1。也可以通过blob[9]来获取。
    
- blob.area() 返回色块的外框的面积。应该等于(w * h)
    
- blob.density() 返回色块的密度。这等于色块的像素数除以外框的区域。如果密度较低，那么说明目标锁定的不是很好。  
    比如，识别一个红色的圆，返回的blob.pixels()是目标圆的像素点数，blob.area()是圆的外接正方形的面积。
#### 颜色阈值的确定
##### 阈值编辑器的使用

![](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/99d3192621916bfa0b9b695ba3407741.png)


![](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/b813b0200295211844a6527dce23e84a.png)

调整区域直到目标区域变成白色

![](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/e656b436a0c391b5bd20dc25e6d86188.png)

记录LAB阈值

(9,100,-128,-16,-128,60)  该绿色区域的LAB阈值

##### 在帧缓冲区框选

![](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/04e67d6a85409bbaad59562e475790fb.png)

#### 示例

##### 单颜色识别

```python
import sensor
import time
import math

threshold_index = 4  # 0 for red, 1 for green, 2 for blue

# Color Tracking Thresholds (L Min, L Max, A Min, A Max, B Min, B Max)
# The below thresholds track in general red/green/blue things. You may wish to tune them...
thresholds = [
    (30, 100, 15, 127, 15, 127),  # generic_red_thresholds
    (30, 100, -64, -8, -32, 32),  # generic_green_thresholds
    (0, 30, 0, 64, -128, 0),  #  系统给的 蓝色 阈值
    (9,100,-128,-16,-128,60),  #通过阈值编辑器自己确定的绿色阈值
    (38,50,20,30,-75,-50),   #通过帧缓冲区自己确定的蓝色阈值
]  

sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.skip_frames(time=2000)
sensor.set_auto_gain(False)  # must be turned off for color tracking
sensor.set_auto_whitebal(False)  # must be turned off for color tracking
clock = time.clock()

# Only blobs that with more pixels than "pixel_threshold" and more area than "area_threshold" are
# returned by "find_blobs" below. Change "pixels_threshold" and "area_threshold" if you change the
# camera resolution. "merge=True" merges all overlapping blobs in the image.

while True:
    clock.tick()
    img = sensor.snapshot()
    for blob in img.find_blobs(
        [thresholds[threshold_index]] ,#通过索引来确定要找的颜色
        pixels_threshold=200, #像素阈值
        area_threshold=200, #面积阈值
        merge=True, #开启合并
        
    ):
        # These values depend on the blob not being circular - otherwise they will be shaky.
        if blob.elongation() > 0.5: #延伸度如果大于0.5（接近一条线）
            img.draw_edges(blob.min_corners(), color=(255, 0, 0)) #画该线的红色轮廓
            img.draw_line(blob.major_axis_line(), color=(0, 255, 0)) #画最长绿色轴线
            img.draw_line(blob.minor_axis_line(), color=(0, 0, 255))#画最短蓝色轴线
        img.draw_rectangle(blob.rect()) #画白框
        img.draw_cross(blob.cx(), blob.cy()) #画中心十字
        img.draw_keypoints( #用于在图像上绘制关键点的函数
            [(blob.cx(), blob.cy(), int(math.degrees(blob.rotation())))], size=20
        )
    print(clock.fps())


```


![](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/e95a691ef34b158e0aba6b964c6b8b34.png)


## 串口通信
