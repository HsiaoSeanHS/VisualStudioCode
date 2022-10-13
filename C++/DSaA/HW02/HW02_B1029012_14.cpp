#include <stdio.h>
#include <iostream>
#include <bits/stdc++.h>
#include <chrono>
#include <ctime>

using namespace std;

//Add Function (Program 1.35)
void Add(int** a,int** b,int** c,int m,int n){
    for(int i=0;i<m;i++){
        for(int j=0;j<n;j++){
            c[i][j] += a[i][j] * b[i][j];
        }
    }
}

int main(){
    time_t start, end;
    int m = 0;
    m = time(0) % 100;
    cout <<"m:"<< m <<'\n';
    
    for(int n_num=1;n_num<=30;n_num++){ //run 100,200, ...,3000.
        int n = n_num*100;
        
        //Array
        int **a = new int*[m];
        int **b = new int*[m];
        int **c = new int*[m];
        for(int i=0;i<m;i++){
            a[i] = new int[n];
            b[i] = new int[n];
            c[i] = new int[n];
        }
        
        for(int i=0;i<m;i++){
            for(int j=0;j<n;j++){
                a[i][j] = 1;
                b[i][j] = 1;
            }
        }
        
        //Time
        std::chrono::steady_clock::time_point begin = std::chrono::steady_clock::now();
        Add(a,b,c,m,n);
        std::chrono::steady_clock::time_point end = std::chrono::steady_clock::now();
        cout << std::chrono::duration_cast<std::chrono::nanoseconds>(end - begin).count() << endl;

        for(int i=0;i<m;i++){
            delete [] a[i];
            delete [] b[i];
            delete [] c[i];
        }
        delete [] a;
        delete [] b;
        delete [] c;
    }
    return 0;
    
}