
Sample = "AoOni"

#字串換行
print("Ao\nOni") #反斜線\n表示換行
#字串內含雙引號"
print("\"AoOni\"") #\"可以在字串內打出雙引號"

#字串名稱.lower(): 整個字串都轉為小寫
print(Sample.lower())
#字串名稱.upper(): 整個字串都轉為大寫
print(Sample.upper())

#字串名稱.islower(): 偵測是否整個字串都是小寫
print(Sample.islower())
#字串名稱.isupper(): 偵測是否整個字串都是大寫
print(Sample.isupper())
#函式可以連用
print(Sample.upper().isupper())
print(Sample)

#字串名稱[]: 指定顯示某位置的字元
print(Sample[2])
print(Sample[-1]) #負數可行
#print(Sample[6]) #超出長度不可行

#字串名稱.index("字元"): 尋找指定字元第一次出現的某位置
print(Sample.index("O"))
#字串名稱.replace("被取代字元", "取代字元")
print(Sample.replace("A", "O"))

#2022.08.30