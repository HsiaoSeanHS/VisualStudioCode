//aaa
#include<iostream>
using namespace std;

int main(){
    int n=2, m=10;
    cout<<"輸入行n: ";
    //cin>>n;
    cout<<"輸入列m: "; //應該是該行的字串長度限制
    //cin>>m;
    cout<<endl;
    
    char ** array; //array自訂名稱
    array = new char* [n];
    for(int i=0; i<n; i++){
        array[i] = new char[m];
    }
    //以下為陣列內容
    for(int i=0;i < n; i++){
        char x;
        for(int j=0;j < m; j++){
            cin>>x;
            array[i][j]=x;
            //cout << array[i][j] << "\t";
        }
        /*if(sizeof(x)<10){
            int len = 10-sizeof(x);
            for(int l=0; l<len;l++){
               x=x+*" ";
            }
        }*/
        cout<<x;
        cout<<"!";
        cout << endl;
    }
    for(int i=0;i < n; i++){
        for(int j=0;j < m; j++){
            //array[i][j]=x;
            cout << array[i][j] ;//<< "\t"換行// 
        }     
        cout << endl;
    }
    for(int i = 0; i < n; i++){
        delete [] array[i];
        delete [] array;
    }

    //cout<<"Hello";
}

//bbb