#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h> 
#define size 3


//START A NEW QUEUE
void start_queue(int *start, int *end){
    *start = 0;
    *end = -1;
}


//CHECK IF QUEUE IS EMPTY
bool empty_queue(int start, int end){
    if(start > end) return true;
    else return false;
}


//CHECK IF QUEUE IS FULL
bool full_queue(int end){
    if(end == size - 1) return true;
    else return false;
}


//INSERT DATA IN QUEUE
bool Insere(int queue[],int *start, int *end, int data){
    if(*end - *start == size - 1){
        
        printf("Fail! the stack is full!\n");
        
        return false;
    }else{
        (*end)++;
        queue[*end] = data;
        return true;
    }    
}

int main() {
    int queue[size];
    int start, end;
    int data;

    
    start_queue(&start,&end);
    
    Insere(queue,&start,&end,9);
    Insere(queue,&start,&end,8);
    Insere(queue,&start,&end,7);
    
                    
}



