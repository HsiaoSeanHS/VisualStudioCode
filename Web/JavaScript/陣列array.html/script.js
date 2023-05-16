
let string_array = ["窩", "不", "知道"]; //宣告變數名稱後以中括號填入陣列內容
let num_array = [9, 8, 7, 6, 5];
let boolean_array = [true, false];
let whatever = ["啊", 666, false]; //可以混和不同類型的變數

document.write(string_array); //陣列內容一次全部顯示，每項由逗點分隔
document.write("<br/>");
document.write(num_array);
document.write("<br/>");
document.write(boolean_array);
document.write("<br/>");
document.write(whatever);
document.write("<br/>");

document.write(whatever[1]); //使用中括號[]單獨提取項目，順序由左至右且從零開始
document.write("<br/>");
document.write(whatever[5]); //超出陣列範圍將顯示undefined
document.write("<br/>");

whatever[1] = 777; //改變指定位置值的方法
document.write(whatever[1]); 
document.write("<br/>");

whatever[3] = "阿阿"; //可以新增原本未使用的位置
document.write(whatever);
document.write("<br/>");
whatever[5] = true; //也可以跳號
document.write(whatever); //未使用的位置將直接不顯示(只有逗號)
document.write("<br/>");

document.write(whatever.length); //陣列名稱.length: 取得陣列內容數
document.write("<br/>");
/*2022.08.06*/