#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#define PI 3.141592653589793




float* add_IIP3 (float *data0,long len_array,float *p ){

      long len_sample = len_array/2;

      float *data_out = (float*)malloc(sizeof(float)*len_array);
      float *data = (float*)malloc(sizeof(float)*len_array);

      for (long index=0;index<len_array;index++){
        data[index] = data0[index];}


      for (long index=0;index<len_array;index = index+2){
            data_out[index] = p[0]*(pow(data[index],3)-3*data[index]*pow(data[index+1],2))  +   p[1]*(pow(data[index],2) - pow(data[index+1],2))    +   p[2]*data[index] + p[3];
            data_out[index+1] = p[0]*(-pow(data[index+1],3)+3*data[index]*pow(data[index],2))  +   p[1]*(2*data[index]*data[index+1])    +   data[index+1];



      }

 /*   for(int index = 0; index<4;index++){
        printf("\n data %f",data_out[index]);
    }*/



    return (data_out);






}

