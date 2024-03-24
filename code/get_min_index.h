#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#define PI 3.141592653589793



int get_min_index(float array_data[14]){

int array_index = 0;


float min_data = array_data[0];

for (int index=0;index<14;index++){

    if (min_data>array_data[index]){
        min_data = array_data[index];
        array_index= index;
    }
}
return (array_index);
}
