
class Personal_Information { //模板建立區(class+名稱)
    constructor(name, birth, gender, address, is_human){ //決定輸入變數
        this.name = name; //指標
        this.birth = birth;
        this.gender = gender;
        this.address = address;
        this.is_human = is_human;
    }
    age() { //模板內函式
        return 2022 - this.birth;
    }
}

let _1 = new Personal_Information("AsobiAsobase", 2017, "both", "Nihongo", false); //輸入模板資訊(名稱 = new 模板名稱(各項變數輸入))
let _2 = new Personal_Information("Name", 666, "Gender", "Address", "Is human");
let _3 = new Personal_Information("希留耶", 2006, "female", "Princess Connect", true);

document.write(_1.name); //呼叫模板資訊(名稱.物件名)
document.write("<br/>");
document.write(_2.is_human);
document.write("<br/>");
document.write(_3.age());
document.write("<br/>");

/*2022.08.22*/