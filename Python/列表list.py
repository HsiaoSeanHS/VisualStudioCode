
Number = [5, 5, 5, 5, 5, 4, 4, 4, 4, 3, 3, 3, 2, 2, 1]
Text = ["窩不知道", "Apple", "123"]
Boolean = [True, False]
Blend = [666, "呵呵呵", False] #資料類型可以混合使用

print(Text[-1]) #-1表示倒數第一個數據
#print(Text[-4]) #超出範圍不可行
print(Text[1:-1]) #[從這個位置開始取:取到這個位置前一位]，這裡的1是Apple，而-1則是123，故取到前一位的Apple
print(Number[-10:-1])
print(Number[-1:-10]) #無法取得數據
print(Number[-10:])
print(Number[:-1])
#字串可使用相同邏輯選取字元

Number.extend(Text) #延伸列表: 被接的列表.extend(接上的列表)
print(Number)

Number.clear() #清除列表: 即[]
print(Number)

Number = [5, 5, 5, 5, 5, 4, 4, 4, 4, 3, 3, 3, 2, 2, 1]
Number.append(0) #新增值: (加在最後面的新值)
print(Number)

Text.insert(1, "aranara") #插入新值: (插入的位置, 新增值)
print(Text)

Number.remove(5) #移除第一個指定值
print(Number)

Number.pop() #移除列表最後一位數值
print(Number)

Number.sort() #值由小到大排列
print(Number)

Number.reverse() #列表反轉 #剛好恢復sort前的原狀
print(Number)

print(Number.index(4)) #找到第一個指定值的位置

print(Number.count(3)) #計算指定值出現的次數

#2022.09.04