//單行摘要
/*多行摘要*/

//宣告變數let (常數使用const宣告)
//變數取名規則: 只能是數字英文與_或是$搭配，且不能以數字開頭
let _string="不知道";
let number2333=123;
let $boolean$=false;

//改變變數內容
document.write("窩" + _string); //字串相加，直接合併
document.write("<br/>");
{
    let _string="知道了"; //改變let值必須隔至少一個大括號
    document.write("窩" + _string);
    document.write("<br/>");
}

document.write(number2333);
document.write("<br/>");
let number3332=321-number2333;
{
    //let number2333=321-number2333; 無作用
    document.write(number3332);
    //let number2333=number3332; 無作用
    document.write("<br/>");
    //運算數值需直接換一個新的變數
}

{
    let $boolean$=true;
    document.write($boolean$);
}
//布林值可以直接改變
/*2022.07.31*/