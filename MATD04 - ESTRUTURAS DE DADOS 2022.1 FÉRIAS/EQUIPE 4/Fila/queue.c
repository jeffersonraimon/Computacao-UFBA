#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h> 


typedef struct node{
    int value;
    struct node *next;
} node;


typedef struct {
    node *head;
    node *tail;
}queue;


void init_queue(queue *q){
    q -> head = NULL;
    q -> tail = NULL;
}

bool enqueue(queue *q, int value){

    //create a new node
    node *newnode = malloc(sizeof(node));
    if (newnode == NULL) return false;
    newnode -> value = value;
    newnode -> next = NULL;

    if (q -> tail != NULL){
        q ->tail ->next = newnode;
    }
    q -> tail = newnode;

    if (q -> head == NULL){
        q -> head = newnode;
    }
    return true;
}


int main(){

    queue q1;

    init_queue(&q1);
    enqueue(&q1, 9);
    enqueue(&q1, 8);
    enqueue(&q1, 7);
    
    return 0;

}