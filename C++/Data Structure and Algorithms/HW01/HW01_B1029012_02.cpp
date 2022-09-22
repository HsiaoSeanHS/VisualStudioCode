#include<iostream>
#include<ctype.h>

using namespace std;

int main() {
    int x, y=100;
    cout<<"輸入x: ";//字串數量限制
    cin>>x;
    //cout<<"輸入y: "; //字串長度限制
    //cin>>y;
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
        for(int j=0;j < y; j++){
            cin.get(c);
            //cout<<isspace(c)<<endl;
            if(isspace(c)==8192){
                //cout<<"!"<<endl;
                space++;
                if((space%2==1) && (space!=1)){
                    break;
                }
            }
            n[i][j] = c;
        }
        cout << endl;
        continue;
    }

    //輸出
    for(int i=0;i < x; i++){
        for(int j=0;j < y; j++){
            printf("%c", n[i][j]);
        }     
        cout << endl;
    }

    //釋放記憶體
    for(int i = 0; i < x; i++){
        delete [] n[i];
        delete [] n;
    }
}