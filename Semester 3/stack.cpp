#include <iostream>
using namespace std;

const int MaxEl=10;
const int Nil=-1;

typedef int infotype;
typedef int address;
typedef struct {
    infotype Data[MaxEl+1];
    address TOP;
} stack;

#define TOP(S) (S).TOP
#define InfoTop(S) (S).Data[(S).TOP]

void CreateEmpty(stack *S) {
    TOP(*S) = Nil;
}

bool IsEmpty(stack S) {
    return (TOP(S) == Nil);
}

bool IsFull(stack S) {
    return (TOP(S) == MaxEl);
}

void Push(stack *S, infotype X) {
    if (!IsFull(*S)) {
        TOP(*S)++;
        InfoTop(*S) = X;
    } else {
        cout << "Stack Penuh";
    }

}

void Pop(stack*S,infotype *x){
    if(!IsEmpty(*S)){
        *x = InfoTop(*S);
        TOP(*S)--;
    }
    else{
        cout<<"stak kosong cik";
    }
}

int main(){
    int n;
    stack DataTest;
    infotype dataHapus;
    CreateEmpty(&DataTest);

    for(int i = MaxEl; i > 0; i--){
        cin >> n;
        Push(&DataTest, n);
    }
     
    while(!IsEmpty(DataTest)){
        Pop(&DataTest, &dataHapus);
        cout << dataHapus << endl;
    }

}