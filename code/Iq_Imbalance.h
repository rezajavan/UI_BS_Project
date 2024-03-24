#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#define PI 3.141592653589793




float* IQ_Imbalance (float *data0,long len_array,float Amplitude, float Phase_imbalance){

      long len_sample = len_array/2;
      float *sin_sample = (float*)malloc(sizeof(float)*len_sample);
      float *cos_sample = (float*)malloc(sizeof(float)*len_sample);
      float *gain_A = (float*)malloc(sizeof(float)*len_array);
      float *data_out = (float*)malloc(sizeof(float)*len_array);
      float *data = (float*)malloc(sizeof(float)*len_array);

      for (long index=0;index<len_array;index++){
        data[index] = data0[index];

      }
      printf("write Amplitude imbalance (dB):  ");
  /*    float Amplitude;    /* offset/SampleRate*/
 /*     float Phase_imbalance;

      scanf("%f",&Amplitude);*/


 /*     printf("write Phase imbalance (degree):  ");
      scanf("%f",&Phase_imbalance);*/

      if (Amplitude != 0){

for (long index =0;index<len_array;index = index+2) { /*create Amplitude vector */

    gain_A[index] = pow(10,0.5*Amplitude/20);
    gain_A[index+1] = pow(10,-1*0.5*Amplitude/20);

}

for (int index =0; index<6;index++){
    printf("\n pow gain %f:  ",gain_A[index]);

}




for (long index = 0;index<len_array;index = index+2){ /* apply Amplitude to data */

    data[index] = data[index]*gain_A[index];
    data[index+1] = data[index+1]*gain_A[index+1];


}

if (data != NULL){
        printf("\n Amplitude Imbalance apply was successful. _/\n");

}
else {
    printf("\n Amplitude Imbalance apply was fail.\n");
}

      }



if (Phase_imbalance !=0){

      for (long index=0;index<len_sample;index++){

        sin_sample[index] = sin(0.5*Phase_imbalance*PI/180);
        cos_sample[index] = cos(0.5*Phase_imbalance*PI/180);
      }



      if (sin_sample != NULL)  {
        printf("\n create Phase-vector was successful. _/ \n");
      }
      else{
        printf("\n create Phase-vector was fail. \n");
      }




    long index1 = 0;
    long index_sample = 0;


    for(long index=0;index<len_array;index = index+2){ /* apply Phase imbalance */


        data_out[index] = data[index]*cos_sample[index_sample]-data[index+1]*sin_sample[index_sample]; /* change Real-part of sample*/
          data_out[index+1] = -1*data[index]*sin_sample[index_sample]+data[index+1]*cos_sample[index_sample]; /* change Image-part of sample*/

               /* data_out[index1] = data[index1]*0.0002;
                data_out[index1+1] = data[index1+1]*0.0002;*/

                 /*  data_out[index1] = data[index1]*cos(-1*index_sample*2*PI*ratio_offset)-data[index1+1]*sin(-1*index_sample*2*PI*ratio_offset);
         data_out[index1+1] = data[index1]*sin(-1*index_sample*2*PI*ratio_offset)+data[index1+1]*cos(-1*index_sample*2*PI*ratio_offset);
*/



            index_sample = index_sample +1;


    }
    if (data_out !=NULL){
    printf("\n Phase Imbalance apply was successful. _/\n");
    }
    else{
        printf("\n Phase Imbalance apply was fail.\n");
    }


}


else {
    data_out = data;
    printf("Phase Imbalance is 0(Phase do not apply).");
}


    if (data_out !=NULL){
    printf("\n Imbalance apply was successful. _/\n");
    }
    else{
        printf("\n Imbalance apply was fail.\n");
    }
    return (data_out);











}
