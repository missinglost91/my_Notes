---
tags:
  - "#计算机"
  - "#编程"
  - "#人工智能"
abstract: 这里填写这篇笔记的摘要
author:
  - 关山难
---

# Arduino 笔记

## 目录

- [准备工作](#准备工作)
- [常用指令](#常用指令)
- [数字信号](#数字信号)
- [模拟信号](#模拟信号)
- [面包板](#面包板)
- [电路连接](#电路连接)
- [传感器](#传感器)
- [项目案例](#项目案例)

---

## 准备工作

### 数据线选择

下载的数据线需要购买带数据传输功能的，有些只是充电线不能用于下载。

![20260802211829](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/20260802211829.png)

### 图形化编程

喜欢图形化编程的用户可以选择相应的可视化编程工具。

---

## 常用指令

### 1、数字信号

#### digitalWrite(pin, value)

**功能**：设置指定引脚的数字电平

**参数**：
- `pin`：引脚号（0-13）
- `value`：HIGH 或 LOW

**示例**：
```cpp
digitalWrite(13, HIGH);  // 设置引脚13为高电平
digitalWrite(13, LOW);  // 设置引脚13为低电平
```

#### digitalRead(pin)

**功能**：读取指定引脚的数字电平

**参数**：
- `pin`：引脚号（0-13）

**返回值**：HIGH 或 LOW

**示例**：
```cpp
int sensorValue = digitalRead(2);  // 读取引脚2的数字电平
```

---

### 2、模拟信号

#### analogWrite(pin, value)

**功能**：在支持 PWM 的引脚上输出模拟值（PWM 波形）

**参数**：
- `pin`：支持 PWM 的引脚（通常为 3, 5, 6, 9, 10, 11）
- `value`：0-255 之间的值

**示例**：
```cpp
analogWrite(9, 128);  // 在引脚9输出50%占空比的PWM
```

#### analogRead(pin)

**功能**：读取模拟引脚的值

**参数**：
- `pin`：模拟引脚（A0-A5）

**返回值**：0-1023 之间的值

**示例**：
```cpp
int sensorValue = analogRead(A0);  // 读取A0引脚的模拟值
```

---

## 面包板

### 结构说明

- **电源轨**：红色/蓝色轨，用于供电
- **信号轨**：中间区域，用于连接元件
- **行标识**：a-j 行，用于识别连接点

### 连接规则

- 同一行（a-j）内的点相互连通
- 电源轨左右两侧分别连通
- 上下电源轨通常不连通

---

## 电路连接

### LED 控制电路

```
Arduino Pin 13 ─── 220Ω 电阻 ─── LED (+) ─── GND
                            LED (-)
```

### 按钮输入电路

```
Arduino Pin 2 ─── 按钮 ─── GND
              └── 10kΩ 电阻 ─── VCC (内部上拉)
```

---

## 传感器

### 光敏电阻（LDR）

- **工作原理**：光照强度影响电阻值
- **典型阻值**：暗光 10kΩ，明亮 1kΩ
- **连接方式**：串联分压电路

### 温度传感器（TMP36）

- **测量范围**：-40°C 到 +125°C
- **精度**：±2°C
- **输出**：模拟电压信号

---

## 项目案例

### 闪烁 LED

```cpp
void setup() {
  pinMode(13, OUTPUT);
}

void loop() {
  digitalWrite(13, HIGH);
  delay(1000);
  digitalWrite(13, LOW);
  delay(1000);
}
```

### 按钮控制 LED

```cpp
const int buttonPin = 2;
const int ledPin = 13;

void setup() {
  pinMode(buttonPin, INPUT_PULLUP);
  pinMode(ledPin, OUTPUT);
}

void loop() {
  if (digitalRead(buttonPin) == LOW) {
    digitalWrite(ledPin, HIGH);
  } else {
    digitalWrite(ledPin, LOW);
  }
}
```

---

**最后更新**：2026-08-02