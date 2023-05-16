
/*函式定義*/
function add(a, b){ //function 函式名稱(函式內部使用變數名稱，沒有用到則空白){函式內容}
    let c = a + b;
    return c; //return後方為函示執行至此回傳值，可指定為任意值(文字、數值、boolean)或是函式的運算結果
    document.write("窩不知道"); //定義中，程式執行遇到return將立即停止，寫在後方的程式碼都不會運作
}

let a = parseFloat(prompt("請輸入被加數")); 
let b = parseFloat(prompt("請輸入加數"));

/*函式呼叫*/
document.write(add(a, b));
document.write("<br/>");

function ouo(){
    //document.write("窩不知道");
    return "窩不知道";
}
document.write(ouo()); //純文字示範
document.write("<br/>");

/*2022.08.07*/