import os, time
from datetime import datetime
from GetData import place_order,send_to_telegram,get_signal,get_signal_fast

if __name__ == '__main__':
    os.system("clear") # For macOS
    print(f'BTC Trading')
    while True:# 持續執行
        side,n1,n2 = get_signal_fast() # 取得交易訊號
        CurrentTime = datetime.now().strftime('%H:%M:%S %m-%d') # 時間
        print(f'{side} {CurrentTime}') #打印信息
        # print(f'signal:{side} n1:{n1} n2:{n2}')
        
        # if side != 'PASS': # 判斷是否出現方向
            # send_to_telegram(message=side)# 發送電報
            # place_order(side) # 根據訊號方向下單
        time.sleep(60*15) # 等15分鐘出現下一根k棒
        # os.system("cls") # 清除屏幕
        # time.sleep(60)