
let Questions = [
    {
        prompt: "窩不是機器人\n(A)是\n(B)不是", //反斜線\n為換行，/br不能用
        Ans: "A"
    },
    {
        prompt: "1000-7=?",
        Ans: 993
    },
    {
        prompt: "這是第幾題?\n(A)1\n(B)2\n(C)3\n請以阿拉伯數字回答。",
        Ans: 3
    },
    {
        prompt: "還有沒有問題?\n(A)沒有\n(B)有",
        Ans: "B"
    }
]

let score = 0;
for(let n = 0; n < Questions.length; n++) {
    let input = prompt(Questions[n].prompt);
    if(input = Questions[n].Ans){
        alert("答對了，加1分。");
        score++;
    }
    else {
        alert("答錯了，扣1分。");
        score--;
    }
}

alert("問答結束。\n你總共得到" + score + "分。"); //score原本是數字屬性，不過為了與前後的字串相加，這裡自動轉換為字串

if(score = 4) {
    alert("Average.");
}
else if(score = 3) {
    alert("Below average.");
}
else if(score = 2) {
    alert("Can't eat dinner.");
}
else if(score = 1) {
    alert("Don't come home.");
}
else if(score = 0) {
    alert("Eat dust.");
}
else {
    alert("Find a new family.")
}

/*2022.08.18*/