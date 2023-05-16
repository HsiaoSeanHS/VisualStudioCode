
let password = 19283746; //正確的密碼
let input; //使用者的輸入密碼
let remain = 3; //剩餘登入次數

    input=prompt("請輸入密碼");
while(password != input && remain != 0) { //密碼輸入錯誤且剩餘次數為零時，跳出while迴圈
    input=prompt("請重新輸入密碼，剩餘嘗試次數:" + remain + "次");
    remain--;
}

if(remain == 0) { //嘗試次數使用完時，顯示登入失敗
    alert("登入失敗!");
} else { //只要輸入正確(跳出while迴圈且不符合if的失敗條件)，則顯示登入成功
alert("登入成功!");
}

/*2022.08.16*/