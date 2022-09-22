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
    int length = 0;
    int longest = 0;
    length = len[0].length();
    for (int i=0; i<x; i++) {
        //cout<<len[i].length()<<endl;
        if (len[i].length() > length){
            length = len[i].length();
            longest = i;
        }
    }
    //cout<<length<<endl;
    
    //宣告二維陣列 (y值暫定為最長字串)
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
            //cout<<trivia[j]<<"."<<endl;
            n[i][j]=trivia[j];
        }
        for(int k=0; k<sizeof(n); k++){
            //cout<<i<<":"<<n[i][k]<<"!"<<endl;
        }
    }
    /*for(int i=0;i < x; i++){
        for(int j=0;j < y; j++){
            printf("%c", n[i][j]);
        }     
        cout << endl;
    }*/
    
    //偵測前段空白與最大前段
    int space[x];
    for(int i=0;i < x; i++){
        for(int j=0;j < y; j++){
            //cin.get(c);
            
            //cout<<isspace(n[i][j])<<endl;
            if((isspace(n[i][j])==8192)&& !(space[i]>=0 &&space[i]<=j)) {
                space[i]=j;
            }
            
            /*if(isspace(c)==8192){
                //cout<<"!"<<endl;
                space++;
                if((space%2==1) && (space!=1)){
                    break;
                }
            }*/
            //n[i][j] = c;
        }
        cout << endl;
        //continue;
    }
    
    /*for(int i=0;i < x; i++){
        cout << space[i];
        cout << endl;
    }*/
    int ls = space[0];
    int ls_p = 0;
    for (int i=0; i<x; i++) {
        //cout<<len[i].length()<<endl;
        if (space[i] > ls){
            ls = space[i];
            ls_p = i;
        }
    }
    //cout<<"lsp:"<<ls_p<<endl;
    
    //依據最長前段，更正二維陣列y值
    //int fspace = 0; 
    //cout<<ls_p<<endl;
    //cout<<longest<<endl;
    //fspace = space[ls_p]-space[longest];
    //cout<<space[ls_p]<<endl;
    //cout<<space[longest]<<endl;
    //cout<<fspace<<endl;
    
    //宣告新二維陣列 (y值更正)
    /*int yy = length+fspace;
    char ** nn; //array自訂名稱
    nn = new char* [x];
    for(int i=0; i<x; i++){
        nn[i] = new char[yy];
    }
    for(int i=0; i<x; i++){
        for(int j=0;j<yy; j++){
            if(j<=1){
                nn[i][j]=='\t';
                cout<<i<<j<<"!"<<endl;
            } else{
                nn[i][j]=n[i][j-2];
            }
        }
    }*/
    //cout<<sizeof(n[0])<<endl;
    //cout<<sizeof(nn[0])<<endl;
    /*for(int i=0;i < x; i++){
        for(int j=0;j < yy; j++){
            printf("%c", nn[i][j]);
        }     
        cout <<"."<< endl;
    }*/
    
    for(int i=0; i<x; i++){
        for(int j=1; j<=(space[ls_p]-space[i]); j++) {
            cout<<" ";
        }
        for(int j=0; j<y; j++){
            printf("%c", n[i][j]);
        }
        cout<<endl;
    }
    
    return 0;
}
