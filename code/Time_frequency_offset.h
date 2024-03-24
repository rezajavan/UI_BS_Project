#include <stdlib.h>
#include <stdio.h>
#include <math.h>

float* Time_offset (float *data0,long len_array,float time_offset,float SampleRate){

      /*int len_sample = len/2;*/


      float *data = (float*)malloc(sizeof(double)*len_array);

      for (long index=0;index<len_array;index++){
        data[index] = data0[index];

      }
      printf("\n write offset time (micro sec): ");
  /*    float time_offset;    /* offset/SampleRate*/
    /*  scanf("%f",&time_offset);*/

      if(time_offset>0){

      printf("write SampleRate frequency (MHz): ");
    /*  float SampleRate;
      scanf("%f",&SampleRate);*/
      
      SampleRate = SampleRate / pow(10,6);
      int offset_ratio_sample = (int)(time_offset*SampleRate);
      printf("\n offset_ratio_sample = %d \n",offset_ratio_sample);





      float *data_out = (float*)malloc(sizeof(double)*len_array);




     /* apply CFO*/
     /*          */

     data_out = data;
    for(long index=0;index<len_array-2*offset_ratio_sample;index++){

        data_out[index] = data[index+2*offset_ratio_sample];

    }/* end for*/
    for (long index=len_array-2*offset_ratio_sample;index<len_array;index++){
        data_out[index] = 0;
    }



    if (data_out !=NULL){
    printf("\n Time_offset apply was successful. _/\n");
    }
    else{
        printf("\n Time_offset apply was fail.\n");
    }
    return (data_out);
}
else{
    printf("\n Time_offset is 0. \n");
    return (data0);
}










}
