#include <iostream>
using namespace std;

int main() 
{
    int g[8] = {10, 9, 8, 7, 0, -1, 12, -5}; 
    int c[8] = {3, 2, 1, 4, 2, 1, 3, 2}; 
    float m = 0; 
    int n = 0; 
    float spi = 0;
    
    for (int i = 0; i < 8; ++i) 
    {
        m += g[i] * c[i];
        n += c[i];
    }

    spi = m / n;
    cout << "The Semester Performance Index (SPI) is: " << spi << endl;
    return 0;
}
