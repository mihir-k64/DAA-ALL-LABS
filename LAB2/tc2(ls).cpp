#include <iostream>
using namespace std;

int linearSearch(const int arr[], int size, int k) {
    for (int i = 0; i < size; ++i) {
        if (k == arr[i]) {
            return i;
        }
    }
    return -1;
}

int main() {
    const int arr[] = {10, 20, 30};
    const int arraySize = sizeof(arr) / sizeof(arr[0]);
    int k;

    cout << "Enter an integer: " << endl;
    cin >> k;

    int result = linearSearch(arr, arraySize, k);
    if (result >= 0) {
        cout << "The number " << arr[result] << " was found at index " 
             << result << " of the array." << endl;
    } else {
        cout << "The number " << k << " was not found." << endl;
    }

    return 0;
}