/*
Nama : Faiq Ghozy Erlangga
NIM : 123140139
Kelas : Praktikum ASD RC
*/

#include <iostream>
using namespace std;

void heapify(int arr[], int n, int i) {
    int largest = i;          // Anggap root adalah yang terbesar
    int left = 2 * i + 1;     // Anak kiri
    int right = 2 * i + 2;    // Anak kanan

    // Jika anak kiri lebih besar dari root
    if (left < n && arr[left] > arr[largest])
        largest = left;

    // Jika anak kanan lebih besar dari yang terbesar sejauh ini
    if (right < n && arr[right] > arr[largest])
        largest = right;

    // Jika yang terbesar bukan root
    if (largest != i) {
        swap(arr[i], arr[largest]); // Tukar
        heapify(arr, n, largest);  // Heapify ulang subtree
    }
}

void buildHeap(int arr[], int n) {
    // Mulai dari node terakhir yang memiliki anak
    for (int i = n / 2 - 1; i >= 0; i--)
        heapify(arr, n, i);
}

void printArray(int arr[], int n) {
    for (int i = 0; i < n; i++)
        cout << arr[i] << " ";
    cout << endl;
}

void hapusTerbesar(int arr[], int& n) {
    if (n == 0) {
        cout << "Heap sudah kosong" << endl;
        return;
    }

    cout << "Elemen terbesar yang dihapus: " << arr[0] << endl;

    arr[0] = arr[n - 1];
    n--;
    heapify(arr, n, 0);
}

int main() {
    int arr[] = {30, 20, 5, 10, 15};
    int n = sizeof(arr) / sizeof(arr[0]);
    cout << "Heap setelah penyisipan: ";
    printArray(arr, n);
    buildHeap(arr, n);
    cout << "heap setelah buildHeap: " ;
    printArray(arr, n);
    hapusTerbesar(arr, n);
    printArray(arr, n);
    
    



    return 0;
}
