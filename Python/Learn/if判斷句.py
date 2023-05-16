
def Max_N(N1,N2,N3):
    if not(N1==N2 and N2==N3):
        if N1>N2 and N1>N3:
            return N1
        
        elif(N2>N1 and N2>N3):
            return N2
        
        else:
            return N3
    else:
        return "All numbers are equal. 所以沒有哪個數"
    


N1 = input("請輸入要比較的第一個數")
N2 = input("請輸入要比較的第二個數")
N3 = input("請輸入要比較的第三個數")

N1 = float(N1)
N2 = float(N2)
N3 = float(N3)
#轉換成浮點數: 用於小數比較大小

print(str(Max_N(N1,N2,N3)) + "是最大數。")

#2022.09.07