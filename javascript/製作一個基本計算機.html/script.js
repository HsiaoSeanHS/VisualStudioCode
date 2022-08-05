
let N1 = prompt("請輸入被加數"); //prompt使網站跳出(文字)，並要求使用者輸入方格內容，資料則指向前方的標籤
let N2 = prompt("請輸入加數");
N1 = parseFloat(N1); //praseFloat使輸入的資料轉為小數，整數的小數點後不會顯示
N2 = parseFloat(N2); //praseInt則是小數強制捨棄成整數(使含有小數的加法無法正確運作)
document.write("加法的結果是: ");
document.write(N1 + N2); //小數計算會出錯
document.write("<br/>");
/*2022.08.05*/