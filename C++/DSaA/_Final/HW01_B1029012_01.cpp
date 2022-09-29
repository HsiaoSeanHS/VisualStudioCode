#include <iostream>
#include <string>
#include <cstdlib>

using namespace std;

int main() {
    int x, y;
    cout<<"x: "; //字串數量限制
    cin>>x;
    cout<<"y: "; //字串長度限制
    cin>>y;
    
    int o = 0;
    string l[x];
    int i = 0;
    for(int i=0; i<x; i++){
        if(o ==1){ //排除getline讀取到cin>>x的Enter
            i--;
            o++;
        }else if((sizeof(l[0])==32)&&(o==0)){
            o++;
        }
        getline(cin,l[i]);
    }

	//宣告二維陣列
	char ** n; //array自訂名稱
    n = new char* [x];
    for(int i=0; i<x; i++){
        n[i] = new char[y];
    }
    
    //將string轉成二維陣列
    for (int i=0; i<x; i++) {
        const char *t=l[i].data();
        for(int j=0; j<y; j++){
            n[i][j] = t[j];
        }
    }

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
            		char* temp = m[d];
                	m[d] = m[e];
                	m[e] = temp;	
            }
        }
    }
    
    //輸出
    cout << endl;
    for(int i=0; i<x; i++){
        for(int j=0; j<y; j++){
			printf("%c", m[i][j]);
        }     
        cout << endl;
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
    system("pause");
}