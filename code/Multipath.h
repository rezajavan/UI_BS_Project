#include <stdlib.h>
#include<stdio.h>
#include<math.h>

#define PI 3.141592653589793

/*



float *multiply (float R1,float I1,float R2,float I2){

    float *mul;


    float R_o;
    float I_o;

    R_o = R1*R2 - I1*I2;
    I_o = R1*I2 + R2*I1;

    return mul;


}
*/



float *add_multipath_S(float *data0,long len_array,int state, float SamplingRate,int size_multipath,float *mul_delay,float *mul_gain_A,float *mul_gain_P){

      long len_sample = len_array/2;
   /* float *sin_sample = (float*)malloc(sizeof(float)*len_sample);
      float *cos_sample = (float*)malloc(sizeof(float)*len_sample);*/
      float *data_out = (float*)malloc(sizeof(float)*len_array);
      float *data_h = (float*)malloc(sizeof(float)*len_array);
      float *data = (float*)malloc(sizeof(float)*len_array);

      int len_filter;

        for (long index=0;index<len_array;index++){
        data[index] = data0[index];
        }





      /* define delay  */

      float delay_EPA [7] =  {0,0.0300,0.0700,0.0900,0.1100,0.1900,0.4100};
      for (int index=0;index<7;index++){
            delay_EPA [index] = delay_EPA [index]* pow(10,-6);}

      float delay_EVA [9] = {0,0.0030,0.0150,0.0310,0.0370,0.0710,0.1090,0.1730,0.2510};
      for (int index=0;index<9;index++){ delay_EVA [index] = delay_EVA [index]* pow(10,-5);}

      float delay_ETU [9] = {0,0.0050,0.0120,0.0200,0.0230,0.0500,0.1600,0.2300,0.5000};
      for (int index=0;index<9;index++){ delay_ETU [index] = delay_ETU [index]* pow(10,-5);}


      /* define gain */
      float gain_EPA [14] = {-0.2198,0.9755,-0.8070,-0.2673,0.0207, 0.2247,-0.0008,-0.1941,0.0668,-0.0447, 0.0616,0.0943,0.0873,-0.0584};

      float gain_EVA [18] = {-0.2198,0.9755,-0.7619,-0.2523,0.0222,0.2407,-0.0007,-0.1812,0.1565,-0.1046,0.1566,0.2397,0.4273,-0.2859,-0.0843,0.1093,0.0114,0.0100};

      float gain_ETU [18] = {-0.2198,0.9755,-0.9055,-0.2999,0.0261,0.2828,-0.0013,-0.3077,0.1881,-0.1258,0.5008,0.7667,0.7599,-0.5084,-0.2118,0.2745,0.0402,0.0351};

/*

     for (int index = 0; index<14;index = index +2){
        printf("\n Phase_EPA = %f",atan(gain_EPA[index+1]/gain_EPA[index])*(180/PI) );
      }



      float d;
      for (int index = 0; index<14;index = index +2){
        d = sqrt(pow(gain_EPA[index],2) + pow(gain_EPA[index+1],2) );
        d = 10*log(d)/log(10);


         printf("\n abs_EPA = %f", d);
       }


*/



      int *delay = (int*)malloc(sizeof(int)*9);
      float *gain = (float*)malloc(sizeof(float)*18);


      /* EPA */
      if (state == 0){
        len_filter = 7;


        for (int index=0;index<len_filter;index++){ delay[index] = (int)(delay_EPA[index]*SamplingRate) ;}
        for (int index=0;index<2*len_filter;index++){ gain[index] = gain_EPA[index] ;}



      }

      /* EVA */

     else if (state == 1){
        len_filter = 9;
        printf("state is 1.");



        for (int index=0;index<len_filter;index++){ delay[index] = (int)(delay_EVA[index]*SamplingRate) ;}
        for (int index=0;index<2*len_filter;index++){
                gain[index] = gain_EVA[index] ;

        }

      }

      /* ETU */

      else if (state == 2){
        len_filter = 9;


        for (int index=0;index<len_filter;index++){ delay[index] = (int)(delay_ETU[index]*SamplingRate) ;}
        for (int index=0;index<2*len_filter;index++){ gain[index] = gain_ETU[index] ;}
      }

      else if (state == 3){
        len_filter = size_multipath;
        for (int index=0;index<len_filter;index++){ delay[index] = (int)(mul_delay[index]*SamplingRate*pow(10,-6)) ;}

        for (int index = 0; index<2*len_filter;index = index +2){
            gain[index] = cos(mul_gain_P[index/2]*(PI/180))*mul_gain_A[index/2];
            gain[index+1] = sin(mul_gain_P[index/2]*(PI/180))*mul_gain_A[index/2];

        }

      }

      else {
        len_filter = 0;
        printf(" error: Multipath input is invalid.");
      }





        /* delay channel = 7 */

    int offset_ratio_sample = 0;

    for(long index=2*offset_ratio_sample;index<len_array-2*offset_ratio_sample;index++){


        data_h[index] = data[index-2*offset_ratio_sample];

    }/* end for*/
    for (long index=0;index<2*offset_ratio_sample;index++){
        data_h[index] = 0;
    }




        float R_o;
        float I_o;
        float R1,I1,R2,I2;



        for (long index = 0; index<len_sample;index = index+2){




        R1 = data_h[index];
        I1 = data_h[index+1];

        R2 = gain[0];
        I2 = gain[1];

        R_o = R1*R2 - I1*I2;
        I_o = R1*I2 + R2*I1;

        data_out[index] = R_o;
        data_out[index+1] = I_o;

   /*     if ((index%100000) == 0){
            printf("turn : %d",index);
        }*/



                }






for (int index = 0; index<2*len_filter;index++){
  printf("\n gain_is is = %f",gain[index]);
}
for (int index = 0; index < len_filter;index++){
  printf("\n delay_is is = %d",delay[index]);
}




long n_sample;


for (long n=0;n<len_array;n = n+2){
        n_sample = n/2;
   for (long counter=1;counter<len_filter;counter++){

       if (n_sample-delay[counter]>=0){

        R1 = data_h[n-2*delay[counter]];
        I1 = data_h[(n-2*delay[counter])+1];

        R2 = gain[2*counter];
        I2 = gain[2*counter+1];

        R_o = R1*R2 - I1*I2;
        I_o = R1*I2 + R2*I1;

        data_out[n] = data_out[n] + R_o;
        data_out[n+1] = data_out[n+1] + I_o;





          /* y(n) = y(n) + gain(counter)*x(n-delay(counter));*/

}



}


}
/*
                for (int index=0;index<50;index++){
                    printf("\n data : %f",data_out[index]);
                }*/


return data_out;







}
