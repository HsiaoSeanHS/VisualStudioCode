
whatever = { "I don't know.": "窩不知道", 0: 1234.5678, 1: True, True: 0, False: 1}

print(whatever) #後半顯示不明
print(whatever["I don't know."])
print(whatever[0]) #未正確顯示
print(whatever[1]) #未正確顯示
print(whatever[True])
print(whatever[False])

#2022.09.09