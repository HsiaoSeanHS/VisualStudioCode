#include <iostream>
#include <cstring>
using namespace std;
class CArray
{
    int size;  //陣列元素的個數
    int* ptr;  //指向動態分配的陣列
public:
    CArray(int s = 0);  //s代表陣列元素的個數
    CArray(CArray & a);
    ~CArray();
    void push_back(int v);  //用於在陣列尾部新增一個元素 v
    CArray & operator = (const CArray & a);  //用於陣列物件間的賦值
    int length() const { return size; }  //返回陣列元素個數
    int & operator[](int i)
    {  //用以支援根據下標存取陣列元素，如“a[i]=4;”和“n=a[i];”這樣的語句
        return ptr[i];
    };
};
CArray::CArray(int s) : size(s)
{
    if (s == 0)
        ptr = NULL;
    else
        ptr = new int[s];
}
CArray::CArray(CArray & a)
{
    if (!a.ptr) {
        ptr = NULL;
        size = 0;
        return;
    }
    ptr = new int[a.size];
    memcpy(ptr, a.ptr, sizeof(int) * a.size);
    size = a.size;
}
CArray::~CArray()
{
    if (ptr) delete[] ptr;
}
CArray & CArray::operator=(const CArray & a)
{  //賦值號的作用是使 = 左邊物件中存放的陣列的大小和內容都與右邊的物件一樣
    if (ptr == a.ptr)  //防止 a=a 這樣的賦值導致出錯
        return *this;
    if (a.ptr == NULL) {  //如果a裡面的陣列是空的
        if (ptr)
            delete[] ptr;
        ptr = NULL;
        size = 0;
        return *this;
    }
    if (size < a.size) {  //如果原有空間夠大，就不用分配新的空間
        if (ptr)
            delete[] ptr;
        ptr = new int[a.size];
    }
    memcpy(ptr, a.ptr, sizeof(int)*a.size);
    size = a.size;
    return *this;
}
void CArray::push_back(int v)
{  //在陣列尾部新增一個元素
    if (ptr) {
        int* tmpPtr = new int[size + 1];  //重新分配空間
        memcpy(tmpPtr, ptr, sizeof(int) * size);  //複製原陣列內容
        delete[] ptr;
        ptr = tmpPtr;
    }
    else  //陣列本來是空的
        ptr = new int[1];
    ptr[size++] = v;  //加入新的陣列元素
}
int main()
{
    CArray a;  //開始的陣列是空的
    for (int i = 0; i<5; ++i)
        a.push_back(i);
    CArray a2, a3;
    a2 = a;
    for (int i = 0; i<a.length(); ++i)
        cout << a2[i] << " ";
    a2 = a3;  //a2 是空的
    for (int i = 0; i<a2.length(); ++i)  //a2.length()返回 0
        cout << a2[i] << " ";
    cout << endl;
    a[3] = 100;
    CArray a4(a);
    for (int i = 0; i<a4.length(); ++i)
        cout << a4[i] << " ";
    return 0;
}