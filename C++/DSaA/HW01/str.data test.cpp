#include <iostream>
#include <string>

using namespace std;

int main()
{
    string str="abc"; 
    const char *trivia=str.data();
    //cout<<p<<endl;
    cout<<str.length()<<endl;
    char n[str.length()];
    for(int i=0; i<str.length(); i++){
        n[i]=trivia[i];
        cout<<trivia[i]<<"."<<endl;
    }
    for(int i=0; i<sizeof(n); i++){
        cout<<n[i]<<"!"<<endl;
    }

    return 0;
}
