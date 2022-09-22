#include<iostream>
#include<cstdlib>
#include<ctype.h>

using namespace std;

int main() {
    int x, y;
    cout<<"輸入x: ";//字串數量限制
    cin>>x;
    cout<<"輸入y: "; //字串長度限制
    cin>>y;
    cout<<endl;
    
    char ** n; //array自訂名稱
    n = new char* [x];
    for(int i=0; i<x; i++){
        n[i] = new char[y];
    }

    //陣列
    //New
    char c;
    int space = 0;
    for(int i=0;i < x; i++){
        int j = 0;
        do{
            cin.get(c);
            if(isspace(c)==8192){
                if(space==0){
                    space++;
                    break;
                } else if(space>=1){
                    space++;
                    break;
                }
            }else{
                if(space==1){
                    i=0;
                    space++;
                }
                n[i][j] = c;
            }
            j++;
        } while(j <= y);
        continue;
    }
    //Malloc
    char **m = (char **) malloc(sizeof(char *) * x);
    for (int i = 0; i < x; i++) {
        m[i] = (char *) malloc(sizeof(char) * y);
        for (int j = 0; j < y; j++) {
            m[i][j] = n[i][j];
        }
    }

    //Bubble sort，ASCII由大而小
    for (int d = 0; d < x; d++) {
        for (int e = d + 1; e < x; e++) {
            if (int(m[d][0]) < int(m[e][0])) {
                char* temp = m[d];
                m[d] = m[e];
                m[e] = temp;
            }
        }
    }
    
    //輸出
    cout << endl;
    for(int i=0;i < x; i++){
        for(int j=0;j < y; j++){
            printf("%c", m[i][j]);
        }     
        cout << endl;
    }

    //釋放記憶體
    for(int i = 0; i < x; i++){
        delete [] n[i];
        delete [] n;
    }
    for (int i = 0; i < x; i++) {
        free(m[i]);
        free(m);
    }
}