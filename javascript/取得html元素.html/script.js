
//window為全域物件，其他物件皆是其子物件，故省略不寫
let h1 = window.document.getElementById("I don't know.");
h1.innerText = "窩知道了";
h1.style.color = "white";
h1.style.backgroundColor = "black";

let iframe = window.document.getElementById("short.");
console.log(iframe); //可以在網頁開啟後的檢查頁面，console標籤裡看到()裡指定的html程式碼內容，方便除錯
iframe.src = "https://www.youtube.com/embed/yZwlW5INhgk";
window.document.write("<br/>");

/*2022.08.23*/