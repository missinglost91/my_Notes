#include <iostream>
#include <cuda_runtime.h>
#include <stdio.h>
#include <string.h>  // 补充memset/memcpy头文件

int main()
{
    int size = 10;
    int nByte = size * sizeof(float);

    //malloc——地址当返回值
    float* arr1; 
    arr1 = (float*)malloc(nByte); 

    //cudaMalloc——地址当参数
    float* arr2; 
    cudaMalloc((float**)&arr2, nByte); 

    //memset清零（置0对float安全）
    memset(arr1, 0, nByte);
    cudaMemset(arr2, 0, nByte);

    //主机内存拷贝
    float* arr3 ;
    arr3 = (float*)malloc(nByte);
    memcpy(arr3, arr1 , nByte);
    
    //主机数据异步拷贝到GPU显存
    float* arr4 ;
    cudaMalloc((float**)&arr4, nByte);
    cudaMemcpy(arr4, arr1 , nByte, cudaMemcpyHostToDevice);
    cudaDeviceSynchronize(); // 等待异步传输结束

    //释放CPU主机内存
    free(arr1);
    free(arr3);
    
    //释放GPU显存
    cudaFree(arr4);
    cudaFree(arr2);

    // 修正函数名：cudaDeviceReset()
    cudaDeviceReset();
    return 0;
}