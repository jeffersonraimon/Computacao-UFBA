
#include <stdio.h>
#include <stdlib.h>
#include "stackfunctions.h"

//int stack[100],size=100,top=-1;

void push(int val);
void pop();
void show();

int main(){

    int ch = 0, val = 0, test = 1;

    do{
    system("cls");    
    printf("\nMenu");
    printf("\n1. PUSH Element");
    printf("\n2. POP ");
    printf("\n3. SHOW Stack");
    printf("\n4. Exit");
    printf("\nEnter your choice 1 to 4: ");
    scanf("%d", &ch);
    switch (ch){

    case 1:


        do{
        
        printf("Enter value to be Pushed: ");
        scanf("%d", &val);
        push(val);
        printf("Continue?: 1 - YES | 2 - NO: ");
        scanf("%d", &test);
        } while (test == 1);
        
        break;
        
    case 2:
        pop();
        
        break;

    case 3:
        show();
        break;
    case 4:
        exit(0);
        break;

    default:
        printf("Invalid choice !");
        break;
    }

    }while (ch<=3);

    system("pause");
    return -1;
}