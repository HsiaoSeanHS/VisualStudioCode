
def add(n1, n2): #函式命名原則與變數相同: 1.只接受英文字母與數字、底線_的組合 2.不可以數字為開頭
    return int(n1) + int(n2)
n1 = input("n1: ")
n2 = input("n2: ")
print("兩數相加的結果為: " + str( add(n1, n2))) #數字相加完若要與文字合併，需要使用str轉換

def none():
    return
print(none()) #無回傳值時，輸出結果顯示None

#2022.09.06