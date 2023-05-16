
function Max_N(N1,N2,N3){
    if(!(N1==N2 && N2==N3)){ //或的用法: ||
        if(N1>N2 && N1>N3){
            return N1;
        } 
        else if(N2>N1 && N2>N3){
            return N2;
        }
        else{
            return N3;
        }
    }
    else{
        return "All numbers are equal. 所以沒有哪個數";
    }
}

let N1 = prompt("請輸入要比較的第一個數");
let N2 = prompt("請輸入要比較的第二個數");
let N3 = prompt("請輸入要比較的第三個數");
N1 = parseFloat(N1);
N2 = parseFloat(N2);
N3 = parseFloat(N3);

document.write(Max_N(N1,N2,N3) + "是最大數。");
document.write("<br/>");

/*2022.08.08*/