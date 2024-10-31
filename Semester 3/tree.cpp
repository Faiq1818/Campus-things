#include <iostream>
using namespace std;

typedef int infotype;
typedef struct tNode *addrNode;
typedef struct tNode {
    infotype info;
    addrNode left;
    addrNode right;
} Node;

typedef addrNode BinTree;

#define Akar(P) (P)->info
#define Left(P) (P)->left
#define Right(P) (P)->right

#define Nil NULL

addrNode AlokNode(infotype X) {
    addrNode newNode = new Node;
    if (newNode != Nil) {
        newNode->info = X;
        newNode->left = Nil;
        newNode->right = Nil;
    }
    return newNode;
}

BinTree Tree(infotype A, BinTree L, BinTree R) {
    BinTree P = AlokNode(A);
    if (P != Nil) {
        Left(P) = L;
        Right(P) = R;
    }
    return P;
}

void DealokNode(addrNode P) {
    if (P != Nil) {
        DealokNode(Left(P));
        DealokNode(Right(P));
        delete P;
    }
}

bool IsTreeEmpty(BinTree P){
    return (P == Nil);
}

bool IsTreeOneElmt(BinTree P){
    if(P != Nil){
        return (Left(P) == Nil && Right(P) == Nil);
    } else {
        return false;
    }
}

bool IsUnerLeft(BinTree P){
    if(P != Nil){
        return (Left(P) != Nil && Right(P) == Nil);
    } else {
        return false;
    }
}

bool IsUnerRight(BinTree P){
    if(P != Nil){
        return (Left(P) == Nil && Right(P) != Nil);
    } else {
        return false;
    }
}

bool IsBiner(BinTree P){
    if(P != Nil){
        return (Left(P) != Nil && Right(P) != Nil);
    } else {
        return false;
    }
}

void PreOrder(BinTree P){
    if(IsTreeEmpty(P)){}
    else {
        cout << Akar(P);
        PreOrder(Left(P));
        PreOrder(Right(P));
    }
}

void InOrder(BinTree P){
    if(IsTreeEmpty(P)){

    } else {
        InOrder(Left(P));
        cout << Akar(P);
        InOrder(Right(P));
    }
}

void PostOrder(BinTree P){
    if(IsTreeEmpty(P)){

    } else {
        PostOrder(Left(P));
        PostOrder(Right(P));
        cout << Akar(P);
    }
}
int NbElmt(BinTree P);
int NbElmt(BinTree P){
    if(IsTreeEmpty(P)){
        return 0;
    } else {
        return(1 + NbElmt(Left(P)) + NbElmt(Right(P)));
    }
}
int main(){
    BinTree P = Tree(1, 
                    Tree(2, AlokNode(4), AlokNode(5)),
                    Tree(3, AlokNode(6), AlokNode(7))
                    );

    
    return 0;
}