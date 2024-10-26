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
    return ((Head(Q) == Nil) && (Tail(Q) == Nil));
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
bool isFull(Queue Q){
    return(NbElmt(Q) == MaxEl);
}
void CreateEmpty(Queue *Q){
    Head(*Q) = Nil;
    Tail(*Q) = Nil;
}
void Add(Queue *Q, infotype x){
    if(!isFull(*Q)){
        if(isEmpty(*Q)){
            Head(*Q) = 1;
            Tail(*Q) = 1;
        } else {
            if (Tail(*Q) == MaxEl) Tail(*Q)=1;
            else Tail(*Q)++;
        }
        InfoTail(*Q) = x;
    } else {
        cout << "Queue Penuh" << endl;
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
    Add(&DataAntrian, 1);
    Add(&DataAntrian, 2);
    Add(&DataAntrian, 3);
    Add(&DataAntrian, 4);
    Add(&DataAntrian, 5);
    Add(&DataAntrian, 6);
    Del(&DataAntrian, &hapus);
    Del(&DataAntrian, &hapus);

    while (Head(DataAntrian) != Nil) {
        cout << InfoHead(DataAntrian) << endl;
        Del(&DataAntrian, &hapus);
    }
}