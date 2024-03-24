#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#define PI 3.141592653589793
#include "get_min_index.h"
#include <time.h>

float *add_Phase_noise(float *data0,long len_array,float Level,float offset,float SamplingRate){
long len_sample = len_array/2;

float *data_out = (float*)malloc(sizeof(float)*len_array);
float *data = (float*)malloc(sizeof(float)*len_array);
for (long index=0;index<len_array;index++){
        data[index] = data0[index];

      }

int min_index;

/*float Level = -20;
float offset = 30;
float SamplingRate =15360000;*/

float ratio_offset;
ratio_offset = SamplingRate/offset;
float num = sqrt(2*PI*offset*pow(10,Level/10));
float ratioVec[14]  = {10,50,100,500,1e3,5e3,1e4,5e4,1e5,5e5,1e6,5e6,1e7,5e7};
/*float nCoeffVec = 2.^[7 7 7 7 7 10 10 11 12 15 16 18 19];*/
float nCoeff;
float delta_vec[14];
for (long index =0; index<14;index++){

    delta_vec[index] = abs(ratio_offset-ratioVec[index]);


}

min_index = get_min_index(delta_vec);

/*printf("\n ratio : %f",ratio_offset);
printf("\n min : %f",min_index);*/

if (min_index<=4){
    nCoeff = pow(2,7);
}
if (min_index==5 || min_index==6){
    nCoeff = pow(2,10);
}
if (min_index == 7){
    nCoeff = pow(2,11);
}
if (min_index==8){
    nCoeff = pow(2,12);
}
if (min_index==9){
    nCoeff = pow(2,15);
}
if (min_index==10){
    nCoeff = pow(2,16);
}
if (min_index==11){
        nCoeff = pow(2,18);

}
if (min_index==12){
    nCoeff = pow(2,19);
}
if (min_index == 13){

    printf("\n error: offset is very small. SamplingRate/offset = %f >> 1e7 ",ratio_offset);
}



float *den = (float*)malloc(sizeof(float)*nCoeff);

den[0] = 1;
for (long index =1;index<nCoeff;index++){

    den[index] = (index+1-2.5)*(den[index-1])/(index);

    /*printf("\n den = %f",den[index-1]);*/

}


/* Create random_nosie */
unsigned long len_binary_noise;
unsigned long len_data_noise;
 FILE *f;
 f = fopen("random_data.bin","rb");
  fseek(f, 0L, SEEK_END);
  len_binary_noise = ftell(f);
  fclose(f);

  len_data_noise = len_binary_noise/sizeof(float);

    float *data_noise_read = (float*)malloc(len_data_noise*sizeof(float));
    float *data_noise = (float*)malloc(sizeof(float)*len_sample);

    f = fopen("random_data.bin","rb");

   fread(data_noise_read, sizeof(float), len_data_noise, f);
   fclose(f);


   /*        */


    unsigned long random_index;
    float random;
    srand((unsigned int)time(NULL));

    float a = 1.0;
    for (unsigned long index=0;index<len_sample;index++){

        random =  ((float)rand()/(float)(RAND_MAX)) * a;

        if (random*len_sample < len_data_noise){

        random_index= (long)(random*len_sample);}
        else{
            random_index = (long)(random*len_sample);
            random_index = random_index%len_data_noise;
        }

    data_noise[index] = data_noise_read[random_index];

}

/*         */
/*          */
/*
 f = fopen("data_noise_read.bin","wb");


    float *data_write = (float*)malloc(len_sample*sizeof(float));

    for (long index=0; index<len_sample;index++){
        data_write[index] = data_noise[index];}

 fwrite(data_write,sizeof(float),len_sample, f);
  fclose(f);*/

float *filtnoise = (float*)malloc(sizeof(float)*len_sample);

/*filtnoise = num.*data_noise;*/

for(unsigned long index=0; index<len_sample;index++){
    filtnoise[index] = num*data_noise[index];

}

for (int index = 0;index<10;index++){
    printf("\n filtnoise: %f",filtnoise[index]);
}
for( long n=0; n<len_sample;n++){
    for( long m=1;m<nCoeff;m++){
        if((n-m)>= 0){
            filtnoise[n] =filtnoise[n]-den[m]*filtnoise[n-m];
            /*printf("\n if be run.");*/
            }


        else{
                /*printf("\n break.");*/
            break;

        }

  /*  printf("\n filtnoise : %f",filtnoise[n]);
    printf("\n n: %d",n);
    printf("\n m: %d",m);
    printf("\n n-m: %d",n-m);*/





}
  /*  printf("\n filtnoise after loop m : %f",filtnoise[n]);
    printf("\n n after loop m: %d",n);*/

    if (n%100000==0){
        printf("\n turn n: %d",len_sample-n);
    }
}

/*
f = fopen("data_noise_read.bin","wb");


    float *data_write = (float*)malloc(len_sample*sizeof(float));

    for (long index=0; index<len_sample;index++){
        data_write[index] = filtnoise[index];
        }

 fwrite(data_write,sizeof(float),len_sample, f);
  fclose(f);

*/

float *sin_sample = (float*)malloc(sizeof(float)*len_sample);
float *cos_sample = (float*)malloc(sizeof(float)*len_sample);

     for (long index=0;index<len_sample;index++){

        sin_sample[index] = sin(filtnoise[index]);
        cos_sample[index] = cos(filtnoise[index]);
      }

long index1 = 0;
long index_sample = 0;

for(long index0=0;index0<len_array;index0 = index0+2){
            index1 = index0;

        data_out[index1] = data[index1]*cos_sample[index_sample]-data[index1+1]*sin_sample[index_sample]; /* change Real-part of sample*/
          data_out[index1+1] = data[index1]*sin_sample[index_sample]+data[index1+1]*cos_sample[index_sample]; /* change Image-part of sample*/

index_sample = index_sample +1;
}


return data_out;
}
