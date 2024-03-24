/* Read binary file*/

#include <stdio.h>
#include <stdlib.h>






long get_len_binary_python(){
long len_binary;
 FILE *f;
 f = fopen("get.bin","rb");
  fseek(f, 0L, SEEK_END);
  len_binary = ftell(f);
  fclose(f);


return len_binary;

}


long get_len_array_python(){
long len;

  FILE *f = fopen("get.bin","rb");
  fseek(f, 0L, SEEK_END);
  len = ftell(f)/sizeof(float);
  fclose(f);


return len;
}





/*read binary file*/


float* read_binary_python (){

long len_binary;
long len_array;

len_array = get_len_array_python();
len_binary = get_len_binary_python();

  float *data_read = (float*)malloc(len_binary*sizeof(float));

FILE *f = fopen("get.bin","rb");

  fread(data_read, sizeof(float), len_array, f);
  fclose(f);



 return  (data_read);
}










/* write data to binary file*/
int write_binary_python(float *data,long len_array,long len_binary){





 FILE *f = fopen("get.bin","wb");


    float *data_write = (float*)malloc(len_binary);

    for (long index=0; index<len_array;index++){
        data_write[index] = data[index];



    }
    /*
    printf("\n size: %d",sizeof(data_write)/sizeof(float));
    for (long index = 0;index<50;index++){
        printf("\n %f",data_write[index]);
    }
*/



  fwrite(data_write,sizeof(float),len_array, f);
  fclose(f);


return 0;
}

