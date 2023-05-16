
function Click(element) {
    element.innerText = "你還是按了";
    element.style.color = "green";
}

let Butt = document.getElementById("Butt."); //與上面的做法不同，功能相同
Butt.addEventListener("click", function(){ //變數名稱.addEventListener("偵測動作", 執行函式)
    this.innerText = "窩知道了";
    this.style.color = "red";
})

let Bu = document.getElementById("Bu.");
Bu.addEventListener("mouseover", function(){ //mouseover: 滑鼠進入物件上方區域
    this.innerText = "女子";
})
Bu.addEventListener("mouseout", function(){ //mouseout: 滑鼠離開物件上方區域
    this.innerText = "好";
})
Bu.addEventListener("click", function(){ //click: 滑鼠點擊物件
    this.innerText = "不好"; //可以運作，但游標一離開區域即會被mouseout重置狀態
    this.style.color = "blue";
})

/*2022.08.25*/