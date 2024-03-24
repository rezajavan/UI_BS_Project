#include <stdio.h>
#include <stdlib.h>
#include "read_data.h"
#include "CFO.h"
#include <math.h>
#include "Time_frequency_offset.h"
#include "Iq_Imbalance.h"
#include "Phase_noise.h"
#include <math.h>
#include "Multipath.h"
#include "Doppler.h"
#include "add_IIP3.h"
#include "read_data_python.h"
int main()
{
    long len_array_python = get_len_array_python();
    long len_array = get_len_array();
    long len_binary = get_len_binary();


    printf("\n len is: %d",len_array_python);
    printf("\n len data is: %d",len_array);

    float *read_data = (float*)malloc(len_binary);
    float *last_data = (float*)malloc(len_binary);

    float *read_data_python = (float*)malloc(len_array_python*sizeof(float));

    read_data_python = read_binary_python();
    read_data = read_binary_F();

    if (read_data !=NULL){

        printf("\n read data from binary file was successful. _/ \n");
    }
    else {
        printf("\n read data from binary file was fail. \n");

    }


    float st_CFO,st_TFO,st_IQ,st_PN,st_Doppler,st_IIP3,st_multipath,SamplingRate,CFO,TFO_delay,IQ_A,IQ_P,PN_var,PN_offset,IIP3_0,IIP3_1,IIP3_2,IIP3_3,Doppler,size_multipath,mode_multipath;
    float multipath_delay[7];
    float multipath_gain_A[7];
    float multipath_gain_P[7];
    /* assign variable */

    st_CFO = read_data_python[0];
    st_TFO = read_data_python[1];
    st_IQ = read_data_python[2];
    st_PN = read_data_python[3];
    st_Doppler = read_data_python[4];
    st_IIP3 = read_data_python[5];
    st_multipath = read_data_python[6];
    SamplingRate = read_data_python[7]*pow(10,6);
    CFO = read_data_python[8];
    TFO_delay = read_data_python[9];
    IQ_A = read_data_python[10];
    IQ_P = read_data_python[11];
    PN_var = read_data_python[12];
    PN_offset = read_data_python[13];
    IIP3_0 = read_data_python[14];
    IIP3_1 = read_data_python[15];
    IIP3_2 = read_data_python[16];
    IIP3_3 = read_data_python[17];
    Doppler = read_data_python[18];
    size_multipath = read_data_python[19];
    mode_multipath = read_data_python[20];
    /* read delay */
    for (int index = 21;index <= 27; index++){
      multipath_delay[index-21] = read_data_python[index];
    /*  printf("\n delay is %f", multipath_delay[index-21]);*/
    }
    for (int index = 28;index <= 34; index++){
      multipath_gain_A[index-28] = pow(10,read_data_python[index]/10) ;
    /*  printf("\n gain_A is %f", multipath_gain_A[index-27]);*/
    }
    for (int index = 35;index <= 41; index++){
      multipath_gain_P[index-35] = read_data_python[index];
    /*  printf("\n Phase is %f", multipath_gain_P[index-33]);*/
    }



    if (st_CFO == 1){
        read_data = add_CFO(read_data,len_array,CFO);
        printf("\n CFO : %f",CFO);

    }
        if (st_TFO == 1){
        read_data = Time_offset(read_data,len_array,TFO_delay,SamplingRate);
        printf("\n TFO*SamplingRate : %f",TFO_delay*SamplingRate/pow(10,6));

    }
        if (st_IQ == 1){
        read_data = IQ_Imbalance (read_data,len_array,IQ_A,IQ_P);
        printf("\n IQ_A : %f",IQ_A);

    }

        if (st_PN == 1){
        read_data = add_Phase_noise(read_data,len_array,PN_var,PN_offset,SamplingRate);
        printf("\n PN_var : %f",PN_var);

    }
        if (st_Doppler == 1){
        read_data = add_Doppler(read_data,len_array,Doppler,SamplingRate);
        printf("\n Doppler : %f",Doppler);

    }

        if (st_IIP3 == 1){
        float p [4] = {IIP3_0,IIP3_1,IIP3_2,IIP3_3};
        read_data = add_IIP3 (read_data,len_array,p);
        printf("\n p[0] : %f",p[0]);
        printf("\n p[3] : %f",p[3]);

    }
        if (st_multipath == 1){
                if (mode_multipath != -1){
        read_data = add_multipath_S(read_data,len_array,mode_multipath,SamplingRate,size_multipath,multipath_delay,multipath_gain_A,multipath_gain_P);
                }

        printf("\n mode_multipath : %f",mode_multipath);

    }





    last_data = read_data;

    int result_write = write_binary_F(last_data,len_array,len_binary);

    if (result_write == 0){
        printf("\n write data was successful. _/ \n");

    }
        else{
            printf("\n write data was fail \n");
        }









    for (long index = 0; index<len_array_python;index++){

        printf("\n data is :%f",read_data_python[index]);
    }


    return 0;

}
