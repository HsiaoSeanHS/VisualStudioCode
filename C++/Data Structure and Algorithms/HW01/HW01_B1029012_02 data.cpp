#include <iostream>
#include <string>
#include <cstdlib>
#include <ctype.h>

using namespace std;

int main()
{
    int x;
    cout<<"輸入x: ";//字串數量限制
    cin>>x;
    
    //輸入名字
    int length = 0;
    int space = 0;
    int none = 0;
    string len[x];
    int i=0;
    for(int i=0; i<x; i++){
        
        if(none ==1){
            i--;
            none++;
            //cout<<"1"<<endl;
        } else if((sizeof(len[0])==32)&&(none==0)){
            none++;
            //cout<<"2"<<endl;
            //break;
        }
        getline(cin,len[i]);
        //cout<<"3"<<endl;
        //cout<<i<<":"<<len[i]<<"."<<endl;
        //cout<<sizeof(len[i])<<endl;
        //continue;
        //cout<<"4"<<endl;
    }
    //cout<<"5"<<endl;
    //cout<<"="<<len[0]<<"="<<endl;
    /*for(int i=0; i<x; i++){
        cout<<len[i]<<endl;
    }*/
    
    //找出最大總長度
    //length = sizeof(len[0]);
    for (int i=0; i<x; i++) {
        //cout<<len[i].length()<<endl;
        if (len[i].length() > length)
            length = len[i].length();
    }
    //cout<<length<<endl;
    
    int y = length;
    char ** n; //array自訂名稱
    n = new char* [x];
    for(int i=0; i<x; i++){
        n[i] = new char[y];
    }
    
    //將string轉入二維陣列
    for (int i=0; i<x; i++) {
        const char *trivia=len[i].data();
        //cout<<p<<endl;
        //cout<<len[i].length()<<endl;
        //char n[len[i].length()];
        for(int j=0; j<len[i].length(); j++){
            cout<<trivia[j]<<"."<<endl;
            n[i][j]=trivia[j];
        }
        for(int k=0; k<sizeof(n); k++){
            cout<<i<<":"<<n[i][k]<<"!"<<endl;
        }
    }
    
    //
    return 0;
}
