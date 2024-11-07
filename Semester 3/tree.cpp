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
int NbDaun(BinTree P);
int NbDaun(BinTree P){
    if(IsTreeOneElmt(P)){
        return 1;
    } else {
        if(IsUnerLeft(P)){
            return (NbDaun(Left(P)));
        } else if (IsUnerRight(P)){
            return (NbDaun(Right(P)));
        } else {
            return (NbDaun (Left(P)) + NbDaun(Right(P)));
        }
    }
}
int Tinggi (BinTree P){
    int tleft, tright;
    if(IsTreeEmpty(P)){
        return 0;
    } else {
        tleft = Tinggi(Left(P));
        tright = Tinggi(Right(P));
        if(tleft > tright){
            return (1 + tleft);
        } else {
            return (1 + tright);
        }
    }
}
void AddDaunTerkiri(BinTree *P, infotype X){
    if(IsTreeEmpty(*P)){
        *P = Tree(X, Nil, Nil);
    } else {
        AddDaunTerkiri(&(Left(*P)), X);
    }
}
void DelDaunTerkiri(BinTree *P, infotype *X){
    addrNode PDel;
    if(IsTreeOneElmt(*P)){
        *X = Akar(*P);
        PDel = *P;
        *P = Nil;
        DealokNode(PDel);
    } else {
        if(IsUnerRight(*P)){
            DelDaunTerkiri(&(Right(*P)), &(*X));
        } else {
            DelDaunTerkiri(&(Left(*P)), &(*X));
        }
    }
}

int main(){
    BinTree pohon;
    pohon = Tree(1, Nil, Nil);

    AddDaunTerkiri(&pohon, 2);
    AddDaunTerkiri(&pohon, 3);

    BinTree rightNode = AlokNode(4);
    Right(pohon) = rightNode;

    cout << "PreOrder : ";
    PreOrder(pohon);
    cout << endl << endl;
    cout << "InOrder : ";
    InOrder(pohon);
    cout << endl << endl;
    return 0;
}