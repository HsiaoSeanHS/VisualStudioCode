
let Numbers = [ //二維陣列
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

//document.write(Numbers.length);
for(let i = 0; i < Numbers.length; i++) { //巢狀陣列
    for(let j = 0; j < Numbers[i].length; j++) {
        document.write(Numbers[i][j]);
        //document.write("<br/>");
    }
    document.write("<br/>");
}
document.write("<br/>");
/*2022.08.19*/