#include<iostream>
#include<cstdlib>

using namespace std;

/*char BubbleSort(int n,char a[]) {
    
    int i=0,j=0;
    for (i = 0; i < n; i++) {
        for (j = i + 1; j < n; j++) {
            if (a[i] < a[j]) {
                char temp = a[i];
                a[i] = a[j];
                a[j] = temp;
            }
        }
        
    }
    cout<< a[0]<<"?";
    return 0;
}*/

int main(){
    int n, m;
    cout<<"輸入行n: ";
    cin>>n;
    cout<<"輸入列m: "; //應該是該行的字串長度限制
    cin>>m;
    cout<<endl;
    
    char ** array; //array自訂名稱
    array = new char* [n];
    for(int i=0; i<n; i++){
        array[i] = new char[m];
    }
    //以下為陣列內容
    char x;
    for(int i=0;i < n; i++){
        for(int j=0;j < m; j++){
            cin>>x;
            if(x>122||x<65){
                break;
            }
            array[i][j] = x;
            //cout << array[i][j] << "\t";
        }
        /*if(sizeof(x)<10){
            int len = 10-sizeof(x);
            for(int l=0; l<len;l++){
               x+".";
            }
        }*/
        //cout<<sizeof(array[i]); //全滿大小為8
        cout << endl;
        continue;
    }
    //每行為單位顯示
    for(int i=0;i < n; i++){
        for(int j=0;j < m; j++){
            //array[i][j]=x;
            //cout << array[i][j] ;//<< "\t"換行// 
        }     
        //cout << endl;
    }
    char **p = (char **) malloc(sizeof(char *) * n);
    for (int i = 0; i < n; i++) {
        p[i] = (char *) malloc(sizeof(char) * m);
        for (int j = 0; j < m; j++) {
            p[i][j] = array[i][j];
        }
    }
    /*for(int i=0;i < n; i++){
        for(int j=0;j < m; j++){
            //array[i][j]=x;
            printf("%c", p[i][j]);
        }     
        cout << endl;
    }*/
    //氣泡排序
    //cout<<"氣泡排序" << endl;
    for (int d = 0; d < n; d++) {
        for (int e = d + 1; e < n; e++) {
            if (int(p[d][0]) < int(p[e][0])) {
                char* temp = p[d];
                p[d] = p[e];
                p[e] = temp;
            }
        }
    }
    //for(int i=0;i < n; i++){
        //cout<<array[i]<<endl;
        //cout<<BubbleSort(n,array[i])<<"!"<<endl;
    //}
    for(int i=0;i < n; i++){
        for(int j=0;j < m; j++){
            //array[i][j]=x;
            printf("%c", p[i][j]);
        }     
        cout << endl;
    }
    for(int i = 0; i < n; i++){
        delete [] array[i];
        delete [] array;
    }
    for (int i = 0; i < 3; i++) {
        free(p[i]);
    }
    free(p);
    
    //cout<<"Hello";
}