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
void InsertLast(addrNode *First, infotype X){
    addrNode NewNode = NodeAllocation(X);
    addrNode temp;
    temp = *First;
    while (Next(temp) != Nil){
        temp = Next(temp);
    }
    Next(temp) = NewNode;
}
void DeleteFirst(addrNode *First){
    addrNode temp = *First;
    *First = Next(*First);
    Next(temp) = Nil;
    NodeDeallocation(temp);
}
void DeleteAfter(addrNode *pred){
    addrNode temp;
    temp = Next(*pred);
    Next(*pred) = Next(temp);
    NodeDeallocation(temp);
}
void DeleteLast(addrNode *First){
    addrNode temp, predTemp;
    predTemp = Nil;
    temp = *First;
    while (Next(temp) != Nil){
        predTemp = temp;
        temp = Next(temp);
    }
    DeleteAfter(&predTemp);
}
void InsertValue(addrHash hash_table, infotype X){
    int index = X % MaxEl;
    addrNode *First = &(First(hash_table,index));

    if(IsEmptyFirst(*First)){
        InsertFirst(First, X);
    } else {
        InsertLast(First, X);
    }
}
void DeleteValue(addrHash hash_table, infotype X){
    int index = X % MaxEl;
    addrNode *First;
    *First = (First(hash_table, index));

    if(IsEmptyFirst(*First)){
        cout << "Alamat menunjuk Nil.";
    } else {
        if((*First)->info == X){
            DeleteFirst(First);
        } else {
            addrNode temp;
            temp = *First;

            while(Next(temp) != Nil){
                temp = Next(temp);
                if(Info(temp) == X){
                    break;
                }
            }
            if(Next(temp) == Nil && Info(temp) != X){
                cout << "Pada index ke-" << index << " tidak ditemukan data " << X << ".";
            } else {
                if(Next(temp) == Nil){
                    DeleteLast(First);
                }
            }
        }
    }
}
void GetValue(addrHash hash_table, infotype X){
    int index = X % MaxEl;
    addrNode First;
    First = First(hash_table, index);
    
    bool ketemu = false;

    if(IsEmptyFirst(First)){
        cout << "Alamat menunjuk Nil, data tidak ditemukan.";
    } else {
        addrNode temp = First;
        while(temp != Nil){
            if(Info(temp) == X){
                ketemu = true;
            }
            temp = Next(temp);
        }
        if(ketemu  == true){
            cout << "Data ditemukan.";
        } else {
            cout << "Data tidak ditemukan.";
        }
    }
}

int main(){
    Hash hashTable[MaxEl];
    CreateEmptyHash(hashTable);

    InsertValue(hashTable, 1);
    InsertValue(hashTable, 2);
}