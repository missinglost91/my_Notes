---
tags:
  - STM32
abstract: 《Stm32江科大（标准库）》笔记以及《HAL库重制版》笔记
author:
  - 关山难
---
# 目录页




# ==第一章==：软件下载与认识
## 1-1软件下载与安装
keil安装
CubeMX安装
CubeIDE安装


tip1生成可执行文件的配置
project->properties
![image.png](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/20260325151614288.png?imageSlim)

cubemx与cubeide的同步
cubemx中改完配置要回车，再generate code
再在ide中refresh（f5）
## 1-2 CubeMX认识

## 1-3 注释认识
### 1. `/* USER CODE BEGIN Includes */` ~ `/* USER CODE END Includes */`
- **用途**：添加你自己需要的头文件引用
- 例子：
    ```C
    /* USER CODE BEGIN Includes */
    #include "OLED.h"       // 你的OLED驱动头文件
    #include "Motor.h"      // 电机驱动头文件
    #include "Remote.h"     // 遥控器接收头文件
    /* USER CODE END Includes */
    ```
### 2. `/* USER CODE BEGIN PTD */` ~ `/* USER CODE END PTD */`
- **PTD = Private Typedef**
- **用途**：定义你自己的结构体、枚举、类型别名（只在当前 `.c` 文件内使用）
- 例子：
    ```C
    /* USER CODE BEGIN PTD */
    typedef struct
      float temp;
      float humi;
    } SensorData_t; // 传感器数据结构体
    /* USER CODE END PTD */
    ```
### 3. `/* USER CODE BEGIN PD */` ~ `/* USER CODE END PD */`
- **PD = Private Define**
- **用途**：定义只在当前 `.c` 文件内使用的宏常量
- 例子：
    ```C
    /* USER CODE BEGIN PD */
    #define SENSOR_ADC_CHANNEL ADC_CHANNEL_0
    #define OLED_REFRESH_MS    100
    /* USER CODE END PD */
    ```
### 4. `/* USER CODE BEGIN PM */` ~ `/* USER CODE END PM */`
- **PM = Private Macro**
- **用途**：定义只在当前 `.c` 文件内使用的功能宏（带参数的宏）
- 例子：
    ```C
    /* USER CODE BEGIN PM */
    #define MAX(a,b) ((a) > (b) ? (a) : (b))
    #define SET_BIT(reg, bit) ((reg) |= (1 << (bit)))
    /* USER CODE END PM */
    ```

### 5. `/* USER CODE BEGIN PV */` ~ `/* USER CODE END PV */`
- **PV = Private Variables**
- **用途**：声明只在当前 `.c` 文件内使用的静态全局变量（用 `static` 修饰）
- 例子：
 
    ```C
    /* USER CODE BEGIN PV */
    static uint8_t sensor_buffer[16];
    static float   last_temp = 25.0f;
    /* USER CODE END PV */
    ```

### 6. `/* USER CODE BEGIN PFP */` ~ `/* USER CODE END PFP */`
- **PFP = Private Function Prototypes**
- **用途**：声明只在当前 `.c` 文件内使用的**私有函数原型**（用 `static` 修饰的函数）

### 7. `/* USER CODE BEGIN 0 */` ~ `/* USER CODE END 0 */`
- **用途**：放置全局的、不依赖任何函数的代码，通常是：
    - 全局变量初始化
    - 宏定义
    - 只执行一次的初始化代码（在 `main()` 函数之前）


# ==第二章==：入门级项目
## 2-1 开关控制LED
![76f20a1c04a636024d966ace7835fbdb.jpg](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/76f20a1c04a636024d966ace7835fbdb.jpg?imageSlim)

```C
	  
if(HAL_GPIO_ReadPin(GPIOA,GPIO_PIN_9)==GPIO_PIN_SET)//PA9上拉，如果读到PA9是高那么把PC13置高。PC13默认是（上拉）高，不亮
	  {
	  HAL_GPIO_WritePin(GPIOC,GPIO_PIN_13,GPIO_PIN_SET);
	  }
	  else//PA9我们外接到GND，如果连上，那么if不到，那么把PC13置低，亮
	  {
		  HAL_GPIO_WritePin(GPIOC,GPIO_PIN_13,GPIO_PIN_RESET);
	  }
```





## 2-2 红外对射控制蜂鸣器


```C
if(HAL_GPIO_ReadPin(GPIOB,GPIO_PIN_13)==GPIO_PIN_RESET)
	  {
	  HAL_GPIO_WritePin(GPIOB,GPIO_PIN_12,GPIO_PIN_RESET);
	  }
else
	  {
		  HAL_GPIO_WritePin(GPIOB,GPIO_PIN_12,GPIO_PIN_SET);
	  }
```

关于==红外传感器==
经过测试，挡住时输出低电平，GPIO默认要拉高输入

关于==光敏传感器==
光线强时，电阻大，输出低电平，
光线弱时（遮住），电阻小，输出高电平，
（由于两种情况都有输入，GPIO没必要设置）

关于==蜂鸣器==
一般是低电平响，所以GPIO默认输出高电平









## 2-3  PWM控制呼吸灯

认识两个函数
```C

#define __HAL_TIM_SET_COMPARE(__HANDLE__, __CHANNEL__, __COMPARE__) 
//设置占空比（0~100）

#define __HAL_TIM_GET_COMPARE(__HANDLE__, __CHANNEL__) 
//获取占空比
```

```C
  HAL_TIM_PWM_Start(&htim2,TIM_CHANNEL_1);
  while (1)
  {
	  OLED_ShowString(1, 1, "compare:");
	 for(;i<100;i++)
	 {
		 __HAL_TIM_SET_COMPARE(&htim2,TIM_CHANNEL_1,i);
		 OLED_ShowNum(1, 9, i, 3); 
		 HAL_Delay(30);
	 }
	 for(;i>0;i--)
	  {
		 __HAL_TIM_SET_COMPARE(&htim2,TIM_CHANNEL_1,i);
		  OLED_ShowNum(1, 9, i, 3); 
		  HAL_Delay(30);
	 }
```

## 2-4 PWM驱动舵机

```C
__HAL_TIM_SET_COMPARE(&htim2,TIM_CHANNEL_2,(Angle/180)*2000+500);
```
发现哪里不对了吗嘻嘻？(正确如下)
```C
__HAL_TIM_SET_COMPARE(&htim2,TIM_CHANNEL_2,(Angle/180.0)*2000+500);
```


其实可以直接操作寄存器
```C
uint16_t a= htim2.Instance->PSC;

uint16_t b= htim2.Instance->ARR;

uint16_t c= htim2.Instance->CCR1;

#相当于 __HAL_TIM_SET_COMPARE(&htim2,TIM_CHANNEL_1,i);
  

OLED_ShowNum(1, 1, a, 8);

OLED_ShowNum(2, 1, b, 8);

OLED_ShowNum(3, 1, c, 8);
```


## 3-1 ADC单通道

```C
HAL_ADCEx_Calibration_Start(&hadc1);//**作用**：启动 ADC1 的**自校准**

HAL_ADC_Start(&hadc1);//**作用**：启动 ADC1

HAL_ADC_PollForConversion(&hadc1,HAL_MAX_DELAY);//阻塞式等待，直到 ADC 完成一次电压到数字的转换，才会继续执行后面的代码

value = HAL_ADC_GetValue(&hadc1);//一个 12/16 位的无符号整数（取决于 ADC 分辨率配置），范围是 `0 ~ 4095`

```

![image.png](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/20260324231011620.png?imageSlim)


## 3-2 ADC多通道

```C

HAL_ADCEx_Calibration_Start(&hadc1); //使用前校准

for(uint8_t i = 0; i<4; i++)

{

HAL_ADC_Start(&hadc1); //ADC启动，开始转换

if(HAL_ADC_PollForConversion(&hadc1,HAL_MAX_DELAY)==HAL_OK)

{

values[i]=HAL_ADC_GetValue(&hadc1);

}

}
```
![image.png](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/20260324231416846.png?imageSlim)

间断模式
## 3-3 DMA
```C
//启动循环模式

hdma_memtomem_dma1_channel1.Init.Mode = DMA_CIRCULAR;

HAL_DMA_Init(&hdma_memtomem_dma1_channel1);

//启动DMA

HAL_DMA_Start(&hdma_memtomem_dma1_channel1,(uint32_t*)&DataA,(uint32_t*)&DataB,4);
```


## 3-4 ADC多通道扫描+DMA

```C

uint16_t values[4];

OLED_Init(); //OLED初始化

HAL_ADCEx_Calibration_Start(&hadc1); //使用前校准

OLED_Clear();

HAL_ADC_Start_DMA(&hadc1,(uint32_t*)values,4);
```

![image.png](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/20260325151345928.png?imageSlim)
关于配置的解读
### 1. Mode：Independent mode（独立模式）

- **含义**：ADC 单独工作，不和其他 ADC（如 ADC2/ADC3）联动。
- **适用场景**：单 ADC 采样，最常用的基础模式。
- **对比**：如果是双 ADC 同步采样，才会选 Interleaved/Regular simultaneous 等模式。

---

### 2. Data Alignment：Right alignment（右对齐）

- **含义**：ADC 采样结果在 16 位寄存器里**靠右存放**，高位补 0。
    
    - 比如 12 位 ADC 采样值 `0x0A5`，右对齐后是 `0x00A5`（16 位）。
    
- **为什么选它**：
    
    - 方便直接用 `uint16_t` 读取，数值就是 0~4095（12 位）。
    - 左对齐会把结果放在高位，需要额外移位才能得到正确数值。
    
- **和 DMA 的关系**：右对齐 + Half Word 数据宽度，正好让 DMA 读到完整采样值。

---

### 3. Scan Conversion Mode：Enabled（扫描模式使能）

- **含义**：ADC 会按 Rank 顺序**依次扫描多个通道**，你这里配置了 4 个转换（Rank1~Rank4）。
- **作用**：实现多通道 ADC 采样，不用手动切换通道。
- **配合**：必须和 DMA 一起用，才能把多个通道的结果自动存到数组里。

---

### 4. Continuous Conversion Mode：Enabled（连续转换模式）

- **含义**：ADC 完成一次序列扫描后，**自动重新开始下一轮扫描**，不需要手动触发。
- **效果**：只要启动一次 ADC+DMA，就会一直循环采样 4 个通道。
- **和 DMA 循环模式的配合**：
    
    - DMA 设为 Circular 模式 + ADC 连续模式 → 无限循环采样，数据不断更新到 `values` 数组。
    

---

### 5. Discontinuous Conversion Mode：Disabled（间断模式关闭）

- **含义**：不把扫描序列拆成小段，一次完成所有 Rank 的转换。
- **为什么关闭**：你是 4 通道连续扫描，不需要分段触发，保持完整序列更高效。
- **开启的场景**：需要用定时器分段触发采样时才会打开。

---

### 6. ADC_Regular_ConversionMode（规则组转换）

#### Enable Regular Conversions：Enable

- 使能规则组转换（ADC 最常用的转换组）。

#### Number Of Conversion：4

- 定义本次扫描序列的**总通道数**，你这里是 4 个通道（Rank1~Rank4）。
- 必须和 DMA 传输长度 `HAL_ADC_Start_DMA(&hadc1, (uint32_t*)values, 4)` 里的 `4` 一致，否则会丢数据或溢出。

#### External Trigger Conversion Source：Software trigger（软件触发）

- 含义：ADC 转换由**软件调用 `HAL_ADC_Start_DMA()`** 来启动，而不是定时器 / 外部引脚触发。
- 你的代码里 `HAL_ADC_Start_DMA(&hadc1,(uint32_t*)values,4);` 就是软件启动的体现。

---

### 7. Rank（转换顺序）

- **Rank 1/2/3/4**：定义 4 个通道的**采样顺序**。
- 比如 Rank1=Channel0，Rank2=Channel1… → 采样顺序是：`CH0 → CH1 → CH2 → CH3 → 再回到 CH0` 循环。
- **Sampling Time**：55.5 Cycles
    - 采样时间越长，抗干扰能力越强，但采样率越低。
    - 55.5 个时钟周期是比较稳妥的选择，适合慢变化信号（如电压、温度）。




## 3-5 串口发送


### 📡 UART 配置项全解析

我帮你把这张图里的配置项逐一拆解，让你彻底明白每个选项的作用👇

---

#### 1. Mode（工作模式）

这是 UART 的核心工作方式选择：

- **Asynchronous（异步模式）**：最常用，**不需要时钟线**，收发双方靠约定好的波特率同步数据。你现在选的就是这个，适合电脑 / 串口助手通信。
- **Synchronous（同步模式）**：需要额外时钟线（SCLK），由主设备提供时钟，数据同步传输，速度更快但接线更复杂。
- **Single Wire (Half-Duplex)（半双工单线）**：收发共用一根线，同一时间只能单向传输，适合简化布线的场景。
- **Multiprocessor Communication（多处理器通信）**：用于多个 MCU 之间的地址帧 + 数据帧通信，实现多机联网。
- **IrDA（红外通信）**：通过红外收发数据，老式红外遥控 / 数据传输用。
- **LIN（本地互联网络）**：汽车电子里的低成本总线协议。
- **SmartCard / SmartCard with Card Clock**：用于智能卡（如 SIM 卡、IC 卡）通信。

---

#### 2. Basic Parameters（基础参数）

这些是串口通信的 “约定”，**收发双方必须完全一致**，否则会乱码：

- **Baud Rate（波特率）**：`115200 Bits/s`
    
    - 每秒传输的比特数，代表通信速度。
    - 常见值：9600、115200、921600 等，你的串口助手也要设成 115200。
    
- **Word Length（数据位长度）**：`8 Bits (including Parity)`
    
    - 表示每帧数据的有效位数，这里是 8 位（如果带校验位则包含在内）。
    
- **Parity（校验位）**：`None`
    
    - 用于检错：
        
        - `None`：无校验，速度最快。
        - `Even`：偶校验，使数据位 + 校验位中 1 的个数为偶数。
        - `Odd`：奇校验，使 1 的个数为奇数。
        
    
- **Stop Bits（停止位）**：`1`
    
    - 标识一帧数据结束的标志位，1 位是最常见配置。
    

---

#### 3. Advanced Parameters（高级参数）

- **Data Direction（数据方向）**：`Receive and Transmit`
    
    - 全双工模式，既能发也能收；也可以选仅发送（Transmit）或仅接收（Receive）。
    
- **Over Sampling（过采样率）**：`16 Samples`
    - 接收器对每一位数据采样 16 次，提高抗干扰能力和采样精度；也有 8 倍采样模式，速度更快但抗干扰稍差。


```C
MX_USART1_UART_Init();

/* USER CODE BEGIN 2 */

uint8_t byteNumber=0x5a;

uint8_t byteArray[]={1,2,3,4,5};

char ch ='a';

char *str="Hello,world";

  

HAL_UART_Transmit(&huart1, &byteNumber, 1, HAL_MAX_DELAY);

HAL_UART_Transmit(&huart1, &byteArray, 5,HAL_MAX_DELAY);

HAL_UART_Transmit(&huart1, (uint8_t*)&ch,1, HAL_MAX_DELAY);

HAL_UART_Transmit(&huart1,(uint8_t*)str,strlen(str), HAL_MAX_DELAY);

```

## 3-6 串口接收

```C
uint8_t receiveData[2];

/* USER CODE END 2 */

  

/* Infinite loop */

/* USER CODE BEGIN WHILE */

while (1)

{

HAL_UART_Receive(&huart1,receiveData,2,HAL_TIMEOUT);

OLED_ShowHexNum(1 ,1, receiveData[0], 4);

OLED_ShowHexNum(2 ,1, receiveData[1], 4);
```

![image.png](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/20260325165812660.png?imageSlim)

默认发送的是0x12，0x34，也就是十进制的18 ，52
如果用OLED_ShowNum则会输出18， 52
所以得用OLED_ShowHexNum才能正确输出

## 3-7 串口中断

普通轮询
```C
HAL_UART_Receive(&huart1,receiveData,2,HAL_MAX_DELAY);
HAL_UART_Transmit(&huart1, receiveData, 2, HAL_MAX_DELAY);
```
![image.png](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/20260325172611182.png?imageSlim)


容易占用主程序

那么我们开始学习中断模式

先打开usart的全局中断
注意到这个文件
```C
/**

* @brief Tx Transfer completed callbacks.

* @param huart Pointer to a UART_HandleTypeDef structure that contains

* the configuration information for the specified UART module.

* @retval None

*/

__weak void HAL_UART_TxCpltCallback(UART_HandleTypeDef *huart)

{

/* Prevent unused argument(s) compilation warning */

UNUSED(huart);

/* NOTE: This function should not be modified, when the callback is needed,

the HAL_UART_TxCpltCallback could be implemented in the user file

*/

}
```

所以我们的程序写成
```C
void HAL_UART_RxCpltCallback(UART_HandleTypeDef *huart)

{

HAL_UART_Transmit_IT(&huart1,receiveData,sizeof(receiveData));

HAL_UART_Receive_IT(&huart1,receiveData,5);

}

int main()
HAL_UART_Receive_IT(&huart1,receiveData,5);


```


## 3-8 串口+DMA 收发不定长数据

```C
void HAL_UARTEx_RxEventCallback(UART_HandleTypeDef *huart, uint16_t Size)

{

if(huart==&huart1)

{

HAL_UART_Transmit_DMA(&huart1,receiveData,Size);

HAL_UARTEx_ReceiveToIdle_DMA(&huart1,receiveData,sizeof(receiveData));

  

}

}



HAL_UARTEx_ReceiveToIdle_DMA(&huart1,receiveData,sizeof(receiveData));
```

![image.png](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/20260325172711806.png?imageSlim)



![](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/20250924232046.png)

![](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/20250924231507.png)

![](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/20250924232120.png)

关于GPIO的频率

![](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/20250924232229.png)


不同的输出函数
```C
void GPIO_SetBits(GPIO_TypeDef* GPIOx, uint16_t GPIO_Pin);//将指定端口置为高电平
void GPIO_ResetBits(GPIO_TypeDef* GPIOx, uint16_t GPIO_Pin);//将指定端口置为低电平
void GPIO_WriteBit(GPIO_TypeDef* GPIOx, uint16_t GPIO_Pin, BitAction BitVal);//根据第三个参数的值对指定端口输出

/*   BitAction是枚举类型，值可以是Bit_RESET==（就是0置低电平）或者Bit_SET（就是1置高电平）
This parameter can be one of the BitAction enum values:
@arg Bit_RESET: to clear the port pin
@arg Bit_SET: to set the port pin
*/
void GPIO_Write(GPIO_TypeDef* GPIOx, uint16_t PortVal);//可以设置16个端口
```
在使用函数时
```C
GPIO_SetBits(GPIOA, GPIO_Pin_0);//将A0设置为高电平
```


几种使用库函数的方法
先打开.h文件最后，看看有哪些函数，再右键转到定义，查看函数和参数的用法

LM393 电压比较器 进行模拟电压二值化

![](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/20250926170207.png)


stm32中C变量类型的新名字

![](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/20250926170548.png)


stm32中的结构体
```C

typedef struct{
char x;
int y;
float z;
} StructName_t;
//用StructName_t这个名字代指struct{ch x;int y;float z;}这个类型的结构体

StructName_t c;
StructName_t d;
//定义两个该类型的结构体 c 和 d

c.x='A'
//通过 . 来索引这个变量
``` 


 stm32中的枚举

```C
enum {MONDAY=1,TUESDAY=2,WEDNESDAY=3} Week;
//—————————————————————————————————***—————————————————————————————————
//用typedef改名后

typedef enum{
MONDAY=1,
TUESDAY=2,
WEDNESDAY=3
} Week_t;//将该类型的枚举类型变量命名为Week_t

Week_t week;

week = MONDAY;
```


buzzer 蜂鸣器


#### OLED 有机发光二极管

##### OLED通信协议

4 针脚的一般是 I2C

7 针脚的一般是 SPI、

![](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/20250926231606.png)


keil 的调试模式

中断程序
![](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/20250928154017.png)

![](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/20250928191957.png)
这个与门相当于开关
当中断屏蔽寄存器给0，则寄存器给多少都是0，即屏蔽中断
当中断屏蔽寄存器给1，则寄存器给多少就是多少，即允许中断


1与上任意一个数x等于任意数
0与上任意数等于0







电灯只有高电平低电平暗两种状态

PWM通过非常快的高低频率切换，使得最后人眼看上去是一个中等的平率
必须是惯性系统

![](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/20251001230033.png)









![](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/20251002122626.png)

串口

## 通信接口

![](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/39f3ac91ba57e0cb84399291f6113baf.jpg)

can 差分
D+和D-差分

差分稳定性高

双工就是指有一根专门发送一根专门接收数据

多设备要有寻址过程

![](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/2b7b0c9d27a61705b5d7d8b67858f9a0.png)

# 第三章：关于入门级项目的一些思考
## 思考1-关于GPIO配置的一些理解

![image.png](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/20260311210210542.png?imageSlim)

### 1. GPIO output level（GPIO 输出才管）

- **High**：表示引脚初始化后输出**高电平（逻辑 1，通常为 3.3V）**
- 若选择 **Low** 则为低电平（逻辑 0，通常为 0V）

### 2. GPIO mode（GPIO 模式）

- **Output Push Pull（推挽输出）**：
    
    - 可以主动输出高电平和低电平，驱动能力强
    - 适合直接驱动 LED、继电器等负载
    
- 其他常见选项：
    
    - **Output Open Drain（开漏输出）**：只能拉低电平，需要外部上拉电阻才能输出高电平，适合 I2C 等总线
    - **Input（输入模式）**：用于读取外部电平信号
    

### 3. GPIO Pull-up/Pull-down（GPIO是输入时才管）

- **No pull-up and no pull-down（无上拉 / 下拉）**：
    
    - 引脚内部没有连接上拉或下拉电阻，电平状态完全由外部电路决定
    
- 其他常见选项：
    - **Pull-up（上拉）**：内部电阻接至 VDD，默认电平为高
    - **Pull-down（下拉）**：内部电阻接至 GND，默认电平为低


小灯泡推挽输出是低电平点亮
但兑小灯泡正负极则情况相反

开漏输出的高电平模式是没有驱动能力
但是低电平是有的

GPIO 几种输出模式
```C
typedef enum
{ GPIO_Mode_AIN = 0x0,//模拟输入
  GPIO_Mode_IN_FLOATING = 0x04,//浮空输入
  GPIO_Mode_IPD = 0x28,//*下拉输入*
  GPIO_Mode_IPU = 0x48,//*上拉输入*
  GPIO_Mode_Out_OD = 0x14,//开漏输出
  GPIO_Mode_Out_PP = 0x10,//*推挽输出*
  GPIO_Mode_AF_OD = 0x1C,//复用开漏
  GPIO_Mode_AF_PP = 0x18//复用推挽
}GPIOMode_TypeDef;

//上面的意思是 GPIOMode_TypeDef 是一个枚举类型变量，

```

---
## 思考2-为什么`main.c认识 *HAL_GPIO_WritePin()* 函数？

### 为什么`main.c`认识 *HAL_GPIO_WritePin()* 函数？
![image.png](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/20260312205242624.png?imageSlim)

我们注意到`main.c`引用了`main.h`

![image.png](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/20260312205401566.png?imageSlim)

我们看到`main.h`引用了`stm32f1xx_hal.h`,这个文件应该很关键

![image.png](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/20260312205528941.png?imageSlim)

我们看到`stm32f1xx_hal.h`引用了`stm32f1xx_hal_conf.h`,再顺着找

![image.png](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/20260312205701084.png?imageSlim)

我们看到`stm32f1xx_hal_conf.h`引用了`stm32f1xx_hal_gpio.h`,再顺着找

![image.png](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/20260312205903596.png?imageSlim)

那么我们就找到了！
这提醒我们以后如果想使用这个函数的话就需要引用`stm32f1xx_hal.h`这个很关键的库


## 思考3-关于中断的理解

![](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/20250928201229.png)
这里我们采用标准库和HAL对照着看的方式，更直观的了解中断如何配置
配置外部中断的步骤
### 1.配置RCC时钟（EXTI不需要开启时钟，NVIC也不需要开启时钟）

### 2配置GPIO外设，输入模式上升沿或下降沿

![image.png](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/20260312195720693.png?imageSlim)

### 3.配置AFIO，选择我们用的这一路GPIO，连接到后面的EXTI

### 4.配置EXTI选择，边沿触发方式，选择触发响应方式，中断响应或事件响应

### 5.配置NVIC，给我们中断选择一个合适的优先级

标准库代码

```C
/*NVIC配置*/
NVIC_InitTypeDef NVIC_InitStructure;						//定义结构体变量
NVIC_InitStructure.NVIC_IRQChannel = EXTI15_10_IRQn;		//选择配置NVIC的EXTI15_10线
	NVIC_InitStructure.NVIC_IRQChannelCmd = ENABLE;				//指定NVIC线路使能
	NVIC_InitStructure.NVIC_IRQChannelPreemptionPriority = 1;	//指定NVIC线路的抢占优先级为1
	NVIC_InitStructure.NVIC_IRQChannelSubPriority = 1;			//指定NVIC线路的响应优先级为1
	NVIC_Init(&NVIC_InitStructure);								//将结构体变量交给NVIC_Init，配置NVIC外设
```

HAL库配置

![image.png](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/20260312195805381.png?imageSlim)


### 6.接下来写中断程序
不过该写在哪呢？
我们打开`stm32f1xx_it.c`，这是我们中断的配置程序

![image.png](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/20260312212249931.png?imageSlim)

我们来看看*HAL_GPIO_EXTI_IRQHandler(GPIO_PIN_14)* 这个函数是干啥的

![image.png](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/20260312212636914.png?imageSlim)

它先判断如果标志位非0，即有中断发生了
那么先清除标志位，防止重复中断
再运行回调函数
我们看看回调函数是干啥的

![image.png](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/20260312212132083.png?imageSlim)

它的意思是
```Note
注意：此函数不应被修改，当需要回调时，HAL_GPIO_EXTI_Callback 可以在用户文件中实现 
```
也就是它弱定义了回调函数，如果我们想写中断发生的程序，就需要在任意一个.c文件中覆写这个回调函数
像这样
```C
void HAL_GPIO_EXTI_Callback(uint16_t GPIO_Pin) 
{ 
	if(GPIO_Pin == GPIO_PIN_14) // 判断是不是 Pin 14 触发的 
	{ 
	// 在这里写你要做的事！ 
	// 例如：翻转一个LED、发送一个数据、设置一个标志位等 
	HAL_GPIO_TogglePin(GPIOA, GPIO_PIN_5); // 示例：翻转LED引脚 
	} 
	
	if(GPIO_Pin == GPIO_PIN_16)
	{
	HAL_GPIO_WritePin(GPIOC,GPIO_PIN_13,GPIO_PIN_RESET);
	}
}

```

## 思考4-延时函数

在标准库中，我们引用了Delay.h和Delay.c来实现延时函数
在HAL库中则自带了 *HAL_Delay()*  单位ms
补充知识：一秒等于1000ms
![image.png](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/20260312223540958.png?imageSlim)
## 思考5-TIM输出比较

比如我们有个72MHZ的内部时钟，经过预分频（72-1）变成了1MHz的波。
那么一个波的周期为1/1MHz，等于10^-6s，即10^-3ms,
假设我们想要获得一个0.5ms的波
我们让自动重装值为（20000-1）

![image.png](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/20260315111002775.png?imageSlim)

由于0.5/10^-3=500（个）
让CRR（输出比较值）为500

## 思考5-c8t6如何进入DFU模式

![image.png](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/20260324001239564.png?imageSlim)
![1aedd5f858577577948a36343ff5858d.jpg](https://lin01-image-1373317342.cos.ap-beijing.myqcloud.com/1aedd5f858577577948a36343ff5858d.jpg?imageSlim)
只需把跳帽放到合适位置