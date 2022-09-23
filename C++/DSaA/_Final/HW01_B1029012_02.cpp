#include <iostream>
#include <string>
#include <cstdlib>
#include <ctype.h>

using namespace std;

int main()
{
    int x = 0;
    cout<<"輸入x: ";//字串數量限制
    cin>>x;
    
    //輸入名字
    int none = 0;
    string len[x];
    int i=0;
    for(int i=0; i<x; i++){
        if(none ==1){ //排除getline讀取到cin>>x的Enter
            i--;
            none++;
        }else if((sizeof(len[0])==32)&&(none==0)){
            none++;
        }
        getline(cin,len[i]);
    }
    
    //找出最大總長度
    int length = 0;
    int longest = 0;
    length = len[0].length();
    for(int i=0; i<x; i++){
        if(len[i].length() > length){
            length = len[i].length();
            longest = i;
        }
    }
    
    //宣告二維陣列 (y值暫定為最長字串)
    int y = length;
    char ** n; //array自訂名稱
    n = new char* [x];
    for(int i=0; i<x; i++){
        n[i] = new char[y];
    }
    
    //將string轉成二維陣列
    for (int i=0; i<x; i++) {
        const char *trivia=len[i].data();
        for(int j=0; j<len[i].length(); j++){
            n[i][j]=trivia[j];
        }
    }
    
    //偵測前段空白長度
    int space[x];
    for(int i=0; i<x; i++){
        int o = 0;
        for(int j=0; j<y; j++){
            if((isspace(n[i][j])==8192)&&(o==0)){
                space[i]=j;
                o++;
            }
        }
        cout << endl;
    }
    
    //找出最大前段
    int ls = space[0];
    int ls_p = 0;
    for(int i=0; i<x; i++){
        if(space[i] > ls){
            ls = space[i];
            ls_p = i;
        }
    }
    
    //空白修正+輸出
    for(int i=0; i<x; i++){
        for(int j=1; j<=(space[ls_p]-space[i]); j++){
            cout<<" ";
        }
        for(int j=0; j<y; j++){
            printf("%c", n[i][j]);
        }
        cout<<endl;
    }
    
    //釋放記憶體
    for(int i=0; i<x; i++){
        delete [] n[i];
    }
    delete [] n;
}