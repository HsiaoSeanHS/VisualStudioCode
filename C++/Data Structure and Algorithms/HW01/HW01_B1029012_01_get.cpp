#include<iostream>
#include<cstdlib>
#include<ctype.h>
//#include<array>

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
                    //cout<<"1"<<endl;
                    break;
                /*} else if(space==1){
                    i=0;j=0;
                    space++;
                    cout<<"2"<<endl;
                    break;*/
                } else if(space>=1){
                    space++;
                    //cout<<"3"<<endl;
                    break;
                }
                
            }else{
                if(space==1){
                    i=0;
                    space++;
                    //cout<<"No."<<endl;
                }
                //cout<<"i="<<i<<endl;
                //cout<<"j="<<j<<endl;
                //cout<<"c="<<c<<endl;
                n[i][j] = c;
                //cout<<"4"<<endl;
            }
            j++;
        } while(j <= y);
        
        //cout<<"i="<<i<<endl;
        //cout<<"5"<<endl;
        continue;
    }
    /*for(int i=0;i < x; i++){
        for(int j=0;j < y; j++){
            printf("%c", n[i][j]);
            //cout<<endl<<"i="<<i<<", j="<<j<<endl;
        }     
        cout << endl;
    }*/

    //Malloc
    char **m = (char **) malloc(sizeof(char *) * x);
    for (int i = 0; i < x; i++) {
        m[i] = (char *) malloc(sizeof(char) * y);
        for (int j = 0; j < y; j++) {
            m[i][j] = n[i][j];
        }
    }
    //cout<<"6"<<endl;

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
    
    //cout<<"7"<<endl;
    
    //輸出
    cout << endl;
    for(int i=0;i < x; i++){
        for(int j=0;j < y; j++){
            printf("%c", m[i][j]);
            //cout<<endl<<"i="<<i<<", j="<<j<<endl;
        }     
        cout << endl;
    }
    
    //cout<<"8"<<endl;

    //釋放記憶體
    for(int i = 0; i < x; i++){
        delete [] n[i];
        delete [] n;
    }
    for (int i = 0; i < 3; i++) {
        free(m[i]);
        free(m);
    }
}