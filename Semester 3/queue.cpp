#include <iostream>
using namespace std;

#define Nil 0
#define MaxEl 5
typedef int infotype;
typedef int address;
typedef struct {
    infotype T[MaxEl+1];
    address HEAD;
    address TAIL;
} Queue;
#define Head(Q) (Q).HEAD
#define Tail(Q) (Q).TAIL
#define InfoHead(Q) (Q).T[(Q).HEAD]
#define InfoTail(Q) (Q).T[(Q).TAIL]

bool isEmpty(Queue Q){
    return (Head(Q) == MaxEl);
}
bool isFull(Queue Q){
    return(NbElmt(Q) == MaxEl);
}
void CreateEmpty(Queue *Q){
    Head(*Q) = Nil;
    Tail(*Q) = Nil;
}
int NbElmt(Queue Q){
    if(isEmpty(Q)){
        return 0;
    } else {
        if (Head(Q) <= Tail(Q)) {
            return (Tail(Q)-Head(Q)+1);
        } else {
            return (MaxEl-Head(Q)+Tail(Q)+1);
        }
    }
}
void Add(Queue *Q, infotype x){
    if(!isFull(*Q)){
        Head(*Q) = 1;
        Tail(*Q) = 1;
    } else {
        if (Tail(*Q) == MaxEl) Tail(*Q) = 1;
        else Tail(*Q)++;
    }
}
void Del(Queue *Q, infotype *hapus){
    *hapus = InfoHead(*Q);
    if(Tail(*Q) == Head (*Q)){
        Head(*Q) = Nil;
        Tail(*Q) = Nil;
    } else {
        if (Head(*Q) == MaxEl){
            Head(*Q) = 1;
        }
        else Head(*Q)++;
    }
}

int main(){
    Queue DataAntrian;
    int i;
    infotype hapus;

    CreateEmpty(&DataAntrian);
}