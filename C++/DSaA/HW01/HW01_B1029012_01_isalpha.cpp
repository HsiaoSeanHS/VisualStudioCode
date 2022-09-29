#include <iostream>
#include <cstdlib>
#include <ctype.h>

using namespace std;

int main() {
    int x, y;
    cout<<"x: ";//字串數量限制
    cin>>x;
    cout<<"y: "; //字串長度限制
    cin>>y;
    
    char ** n; //array自訂名稱
    n = new char* [x];
    for(int i=0; i<x; i++){
        n[i] = new char[y];
    }
    for(int i=0;i < x; i++){
        for(int j=0;j < y; j++){
			n[i][j]=9;
        }     
    }

    //New
    char c;
    //char dot = ".";
    //int z=-1;
    int len[x];
    int space = 0;
    for(int i=0; i<x; i++){
        int j = 0;
        do{
        	//z++;
			cin.get(c);
			//cout<<endl<<"i="<<i<<", j="<<j<<endl;
			//cout<<space<<endl;
			//cout<<"is"<<isalpha(c)<<endl;
			if(isspace(c)==8){
                //if(space>=0){
                    space++;
                    break;
                //}
            }else{
                if(space==1){
                    i=0;
                    space++;
                    n[i][j] = c;
                }else if((space>=2)&&(j==y)&&(isalpha(c)==2)){
					//cout<<"zzz"<<endl;
					cin.ignore();
					//space++;
					j--;
				}else{
					n[i][j] = c;
				}
				
			}
            j++;
            len[i]=j;
        }while(j<=y);
		//z = 0;
    }
    //cout<<int(n[1][0])<<endl;
    /*for(int i=0;i < x; i++){
        for(int j=0;j < y; j++){
            printf("%c", n[i][j]);
            //cout<<endl<<"i="<<i<<", j="<<j<<endl;
        }     
        cout << endl;
    }*/

    //Malloc
    char **m = (char **) malloc(sizeof(char *) * x);
    for(int i=0; i<x; i++){
        m[i] = (char *) malloc(sizeof(char) * y);
        for(int j=0; j<y; j++){
            m[i][j] = n[i][j];
        }
    }

    //Bubble sort，ASCII由大而小
    for(int d=0; d<x; d++){
        for(int e=d+1; e<x; e++){
            if(int(m[d][0]) < int(m[e][0])){
                char* temp = m[d]; int tlen= len[d];
                m[d] = m[e]; len[d] = len[e];
                m[e] = temp; len[e] = tlen;
            }
        }
        cout<<endl;
    }
    
    //輸出
    cout<< endl;
    for(int i=0; i<x; i++){
        for(int j=0; j<len[i]; j++){
            printf("%c", m[i][j]);
        }     
        cout<< endl;
    }

    //釋放記憶體
    for(int i=0; i<x; i++){
        delete [] n[i];
        free(m[i]);
    }
    delete [] n;
    free(m);

	//程式輸出視窗保留
    cin.get();
}