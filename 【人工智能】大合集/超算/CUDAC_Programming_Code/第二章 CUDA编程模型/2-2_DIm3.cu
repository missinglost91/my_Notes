#include <stdio.h>
#include <cuda_runtime.h>

__global__ void helloFromGPU (void)
{
              printf("Hello World from GPU!\n");
}


int main(void)
{

    dim3 Grid(2,1,1); //或写作dim3 Grid(2);
    dim3 Block(2, 2, 2);
    helloFromGPU <<<Grid, Block>>>();

    printf("Grid: %d, %d, %d\n", Grid.x, Grid.y, Grid.z);
    printf("Block: %d, %d, %d\n", Block.x, Block.y, Block.z);

    cudaDeviceReset();
    return 0;
}