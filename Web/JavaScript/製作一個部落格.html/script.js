/*未知原因無法運作*/
let title = document.getElementById("title");
let content = document.getElementById("content");
let button = document.getElementById("button");
let list = document.getElementById("list");

button.addEventListener("click", function(){
    list.innerHTML = list.innerHTML + 
    <div class="article">
        <h2>${title.value}</h2>
        <p>${content.value}</p>
    </div>
    ;
    title.value = "";
    content.value = "";
})

/*2022.08.26*/