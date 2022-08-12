
let obj = { /*let 物件名稱 = {內容，可包含文字、數字、boolean、function}*/
    text: "窩不知道", /*key鍵: value值*/
    num: 666,
    false: true,
    func_name: function(){
        document.write(this.num); /*此處的this是指函式所在的object: obj； .後方則是object內的key名稱*/
        document.write("<br/>");
    }
};

document.write(obj.text); /*呼叫object的值: object名稱.key名稱*/
document.write("<br/>");

obj.func_name(); /*呼叫object的函式: object名稱.function名稱*/

/*其實程式碼很多都可以看做是object*/
/*document.write("<br/>");*/
/*物件名稱(指令庫).取得的內部屬性名稱(指令)*/

/*2022.08.12*/