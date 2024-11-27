#include <iostream>
using namespace std;

bool isSorted(const int arr[], int size) {
    for (int i = 1; i < size; ++i) {
        if (arr[i] < arr[i - 1]) {
            return false;
        }
    }
    return true;
}

int binarySearch(const int arr[], int low, int high, int k) {
    if (low > high) {
        return -1;
    }

    int mid = low + (high - low) / 2;

    if (arr[mid] == k) {
        return mid; 
    }

    if (k < arr[mid]) {
        return binarySearch(arr, low, mid - 1, k);
    } else {
        return binarySearch(arr, mid + 1, high, k); 
    }
}

int main() {
    const int arr[] = {10, 5, 2, 8};
    const int arraySize = sizeof(arr) / sizeof(arr[0]);
    int k;

    cout << "Enter an integer to search for: " << endl;
    cin >> k;

    if (isSorted(arr, arraySize)) {
        int result = binarySearch(arr, 0, arraySize - 1, k);

        if (result >= 0) {
            cout << "The number " << k << " was found at index " << result << " of the array." << endl;
        } else {
            cout << "The given value " << k << " does not exist in the given array." << endl;
        }
    } else {
        cout << "The array is unsorted. Binary search requires a sorted array." << endl;
    }

    return 0;
}