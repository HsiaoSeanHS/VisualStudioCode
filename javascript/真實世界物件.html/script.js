
let Summer_Time_Rendering_ED2 = {
    Title: "失恋ソング沢山聴いて 泣いてばかりの私はもう。",
    Lable: "VIA/TOY'S FACTORY",
    Singer: [
        {
            name: "りりあ。",
            birth: [ /*複數個項目時，可搭配陣列使用[ { }, { } ] */
                {
                    year: 2000,
                    month: 11,
                    date: 27
                },
                {
                    YYMMDD: "2000.11.27"
                }
            ],
            gender_male: false
        },
        {
            name: "Nobody"
        }
    ],
    Publish_Time: [
        {
            year: 2022,
            month: 7,
            date: 18
        },
        {
            YYMMDD: "2022.07.18"
        }
    ],
    Length: "4:59",
    More_Information: "TVアニメ『サマータイムレンダ』2nd ED テーマ"
}

document.write(Summer_Time_Rendering_ED2.Title);
document.write("<br/>");
document.write(Summer_Time_Rendering_ED2.Singer[0].birth[0].date);
document.write("<br/>");
document.write(Summer_Time_Rendering_ED2.Singer[0].gender_male);
document.write("<br/>");
document.write(Summer_Time_Rendering_ED2.Singer[1].name);
document.write("<br/>");
document.write(Summer_Time_Rendering_ED2.Publish_Time[1].YYMMDD);
document.write("<br/>");
document.write(Summer_Time_Rendering_ED2.More_Information);
document.write("<br/>");

/*2022.08.13*/