#include <iostream>
using namespace std;

#define Nil NULL
#define MaxEl 10

typedef int infotype;
typedef struct tNode *addrNode;
typedef struct tNode {
    infotype info;
    addrNode next;
} Node;
typedef struct tHash *addrHash;
typedef struct tHash {
    addrNode first;
} Hash;

#define Info(P) (P)->info
#define Next(P) (P)->next
#define First(H, i) (H) [i].first

void CreateEmptyHash(addrHash hash_table){
    for(int i = 0; i < MaxEl; i++){
        First(hash_table, i) = Nil;
    }
}
addrNode NodeAllocation(infotype X){
    addrNode NewNode;
    NewNode = (Node*) malloc (sizeof(Node));

    NewNode->info = X;
    Next(NewNode) = Nil;

    return NewNode;
}
void NodeDeallocation(addrNode hapus){
    free(hapus);
}
bool IsEmptyFirst(addrNode First){
    return (First == Nil);
}
void InsertFirst(addrNode *First, infotype X){
    addrNode NewNode = NodeAllocation(X);
    Next(NewNode) = *First;
    *First = NewNode;
}  
void Ins






int main(){

}