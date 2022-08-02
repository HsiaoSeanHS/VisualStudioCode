
let abc="abcde\/fghij\"klmno/pqrst\\uvwxyz"; //若字串需要加入js保留符號，則需要在其前方輸入反斜線(\)
document.write(abc);
document.write("<br/>");

let abcde="abcde";
let fghij="fghij";
document.write(abcde+fghij+"klmno"); //字串變數或是純字串可以直接混和相加
document.write("<br/>");

document.write(abc.length); //document.write(字串變數名稱.length)獲得該字串長度
document.write("<br/>");
document.write("123456789".length); //直接輸入純字串也可以
document.write("<br/>");

let bruh="AoOni";
document.write(bruh);
document.write("<br/>");
document.write(bruh.toUpperCase()); //全轉大寫
document.write("<br/>");
document.write(bruh.toLowerCase()); //全轉小寫
document.write("<br/>");

document.write(bruh.charAt(1)); //charAt: 輸入想要顯示字串中的第幾位文字(注意:從0開始計算)
document.write("<br/>");
document.write(bruh.charAt(2));
document.write("<br/>");
document.write(bruh.charAt(5)); //超出字串長度無法顯示
document.write("<br/>");
document.write(bruh.charAt(-1)); //負方向字串長度無法顯示
document.write("<br/>");

document.write(bruh.indexOf("o")); //indexOf: 尋找指定文字的所在位置(若有複數個，只能找到最接近開頭的第一個位置)
document.write("<br/>");
document.write(bruh.indexOf("O"));
document.write("<br/>");
document.write(bruh.indexOf("z")); //不存在於字串中則顯示-1
document.write("<br/>");

document.write(bruh.substring(1,3)); //substring(開始位置,結束位置的下一位)
document.write("<br/>");
document.write(bruh.substring(1,1)); //開始位置=結束: 不顯示
document.write("<br/>");
document.write(bruh.substring(3,1)); //相反的開始與結束位置: 顯示與正常時的相同結果
document.write("<br/>");
document.write(bruh.substring(5,6)); //超出範圍的位置: 不顯示
document.write("<br/>");
document.write(bruh.substring(-1,0)); //負方向位置: 不顯示
document.write("<br/>");
document.write(bruh.substring(-10,10)); //範圍橫跨負方向與超出範圍的位置: 只顯示正常範圍內的所有文字
document.write("<br/>");
/*2022.08.02*/