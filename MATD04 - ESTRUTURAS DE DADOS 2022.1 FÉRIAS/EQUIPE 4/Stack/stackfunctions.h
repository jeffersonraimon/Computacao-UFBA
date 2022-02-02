int stack[100],size=100,top=-1;


void push(int val)
{
if(top>=size-1)
printf("Overflow: Stack is full \n");
else
{
    top++;
    stack[top] = val;
}

}
void pop()
{
    if(top<=-1)
    {
        printf("Stack Underflow \n");
    }
    else
    {
        printf("The popped element = %d\n", stack[top]);
        top--;
        system("pause");
    }
    

}

void show()
{

    
    if(top>=0){
        printf("Stack Elements are\n");
        for(int i=0;i<=top;i++){
            printf("%d  ",stack[i]);
        }
            printf("\n");
            system("pause");
        }
        else{
        printf("Stack is Empty\n"); 
        system("pause");
    }

}

