#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#define PI 3.141592653589793




float* add_Doppler(float *data0,long len_array,float Doppler,float SamplingRate){

      long len_sample = len_array/2;
      float *sin_sample = (float*)malloc(sizeof(float)*len_sample);
      float *cos_sample = (float*)malloc(sizeof(float)*len_sample);
      float *data_out = (float*)malloc(sizeof(float)*len_array);
      float *data = (float*)malloc(sizeof(float)*len_array);

      for (long index=0;index<len_array;index++){
        data[index] = data0[index];

      }
      printf("write offset ratio (offset/SampleRate):  ");
      float ratio_offset;    /* offset/SampleRate*/

      ratio_offset = Doppler;



      for (long index=0;index<len_sample;index++){

        sin_sample[index] = sin(index*2*PI*ratio_offset);
        cos_sample[index] = cos(index*2*PI*ratio_offset);
      }



      if (sin_sample != NULL)  {
        printf("\n create sin-vector was successful. _/ \n");
      }
      else{
        printf("\n create sin-vector was fail. \n");
      }

      /*  test_code
      printf("\n sin");
      for (int a =100; a<105;a++){
        printf("\n %f",sin_sample[a]);
      }
      printf("\n cos");
            for (int a =100; a<105;a++){
        printf("\n %f",cos_sample[a]);
      }

     /* apply CFO*/
     /*          */

    long index1 = 0;
    long index_sample = 0;

    for(long index0=0;index0<len_array;index0 = index0+2){
            index1 = index0;

        data_out[index1] = data[index1]*cos_sample[index_sample]-data[index1+1]*sin_sample[index_sample]; /* change Real-part of sample*/
          data_out[index1+1] = data[index1]*sin_sample[index_sample]+data[index1+1]*cos_sample[index_sample]; /* change Image-part of sample*/





            index_sample = index_sample +1;


    }/* end for*/

    /* test_code
    printf("\n sample %d \n",index_sample);
    printf("\n data");
    for(int b=100; b<105;b++){
      printf("\n %f",data_out[b]);
      printf("\n %f",data[b]);
    }*/


    if (data_out !=NULL){
    printf("\n CFO apply was successful. _/\n");
    }
    else{
        printf("\n CFO apply was fail.\n");
    }
    return (data_out);











}

