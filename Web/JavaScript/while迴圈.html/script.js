
let i = 0;

do{
    document.write(i);
    document.write("<br/>");
    i++; //若移除此行，則網頁將持續Loading(網頁無回應)，什麼都不會顯示
}while(i <= 3);

/*2022.08.14*/