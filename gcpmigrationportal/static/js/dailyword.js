

function changeword(){
    var x=document.getElementById('myTable').rows
    var hindi=new Array();
    var english=new Array();
    var today=new Date()
    var day=today.getDate()   
    var month=today.getMonth() + 1
    var year=today.getFullYear()

    hindi[1]=" दैनिक ";
    hindi[2]=" सामयिक विषय ";
    hindi[3]=" वांछनीय ";
    hindi[4]=" पता लगाना ";
    hindi[5]="संलग्नक";
    hindi[6]="स्वच्छ प्रति";
    hindi[7]=" उचित मूल्य की दुकान ";
    hindi[8]=" प्रमाण-पत्र ";
    hindi[9]=" पहचान-पत्र ";
    hindi[10]=" सत्यनिष्टा ";
    hindi[11]="सिंचाई";
    hindi[12]="जानबूझकर/जानते हुए";
    hindi[13]="प्रश्नावली";
    hindi[14]="स्मरण करना";
    hindi[15]="पारिश्रमिक";
    hindi[16]="वरिष्ठता सूची";
    hindi[17]="स्फूर्त कार्रवाई";
    hindi[18]="मोहर";
    hindi[19]="आशुलिपि";
    hindi[20]="सफल प्रयास";
    hindi[21]="अन्यान्य ऋणी";
    hindi[22]="अधिवर्षिता";
    hindi[23]="अस्थायी रूप से";
    hindi[24]="परीक्षणालय";
    hindi[25]="जाँच परीक्षण";
    hindi[26]="शब्दावली";
    hindi[27]="मान्यता तिथि";
    hindi[28]="निधि का  उपयोग ";
    hindi[29]="पहरा व निगरानी";
    hindi[30]="आभारी";
    hindi[31]="निविदाकार";
       
    english[1]="DAILY";
    english[2]="CURRENT TOPICS";
    english[3]="DESIRABLE";
    english[4]="DISCOVER";
    english[5]="ENCLOSURE";
    english[6]="FAIR COPY";
    english[7]="FAIR PRICE SHOP";
    english[8]="CERTIFICATE";
    english[9]="IDENTITY CARD";
    english[10]="INTEGRITY";
    english[11]="IRRIGATION";
    english[12]="KNOWINGLY";
    english[13]="QUESTIONNAIRE";
    english[14]="RECOLLECT";
    english[15]="REMUNERATION";
    english[16]="SENIORITY LIST";
    english[17]="SPONTANEOUS ACTION";
    english[18]="STAMP";
    english[19]="STENOGRAPHY";
    english[20]="SUCCESSFUL EFFORTS";
    english[21]="SUNDRY DEBTORS";
    english[22]="SUPERANNUATION";
    english[23]="TEMPORARILY";
    english[24]="TEST HOUSE";
    english[25]="TEST CHECK";
    english[26]="TERMINOLOGY";
    english[27]="VALIDITY DATE";
    english[28]="UTILISATION OF FUNDS";
    english[29]="WATCH AND WARD";
    english[30]="GRATEFUL";
    english[31]="TENDERER";

    var y=x[1].cells
    
   if(day==1 && month==8 && year==2012) {
	    y[0].innerHTML=hindi[1]
	    y[1].innerHTML=english[1]
    }else if(day==2 && month==8 && year==2012) {
	    y[0].innerHTML=hindi[2]
	    y[1].innerHTML=english[2]
    }else if(day==3 && month==8 && year==2012) {
	    y[0].innerHTML=hindi[3]
	    y[1].innerHTML=english[3]
    }else if(day==4 && month==8 && year==2012) {
	    y[0].innerHTML=hindi[4]
	    y[1].innerHTML=english[4]
    }else if(day==5 && month==8 && year==2012) {
	    y[0].innerHTML=hindi[5]
	    y[1].innerHTML=english[5]
    }else if(day==6 && month==8 && year==2012) {
	    y[0].innerHTML=hindi[6]
	    y[1].innerHTML=english[6]
    }else if(day==7 && month==8 && year==2012) {
	    y[0].innerHTML=hindi[7]
	    y[1].innerHTML=english[7]
    }else if(day==8 && month==8 && year==2012) {
	    y[0].innerHTML=hindi[8]
	    y[1].innerHTML=english[8]
    }else if(day==9 && month==8 && year==2012) {
	    y[0].innerHTML=hindi[9]
	    y[1].innerHTML=english[9]
    }else if(day==10 && month==8 && year==2012) {
	    y[0].innerHTML=hindi[10]
	    y[1].innerHTML=english[10]
    }else if(day==11 && month==8 && year==2012) {
	    y[0].innerHTML=hindi[11]
	    y[1].innerHTML=english[11]
    }else if(day==12 && month==8 && year==2012) {
	    y[0].innerHTML=hindi[12]
	    y[1].innerHTML=english[12]
    }else if(day==13 && month==8 && year==2012) {
	    y[0].innerHTML=hindi[13]
	    y[1].innerHTML=english[13]
    }else if(day==14 && month==8 && year==2012) {
	    y[0].innerHTML=hindi[14]
	    y[1].innerHTML=english[14]
    }else if(day==15 && month==8 && year==2012) {
	    y[0].innerHTML=hindi[15]
	    y[1].innerHTML=english[15]
    }else if(day==16 && month==8 && year==2012) {
	    y[0].innerHTML=hindi[16]
	    y[1].innerHTML=english[16]
    }else if(day==17 && month==8 && year==2012) {
	    y[0].innerHTML=hindi[17]
	    y[1].innerHTML=english[17]
    }else if(day==18 && month==8 && year==2012) {
	    y[0].innerHTML=hindi[18]
	    y[1].innerHTML=english[18]
    }else if(day==19 && month==8 && year==2012) {
	    y[0].innerHTML=hindi[19]
	    y[1].innerHTML=english[19]
    }else if(day==20 && month==8 && year==2012) {
	    y[0].innerHTML=hindi[20]
	    y[1].innerHTML=english[20]
    }else if(day==21 && month==8 && year==2012) {
	    y[0].innerHTML=hindi[21]
	    y[1].innerHTML=english[21]
    }else if(day==22 && month==8 && year==2012) {
	    y[0].innerHTML=hindi[22]
	    y[1].innerHTML=english[22]
    }else if(day==23 && month==8 && year==2012) {
	    y[0].innerHTML=hindi[23]
	    y[1].innerHTML=english[23]
    }else if(day==24 && month==8 && year==2012) {
	    y[0].innerHTML=hindi[24]
	    y[1].innerHTML=english[24]
    }else if(day==25 && month==8 && year==2012) {
	    y[0].innerHTML=hindi[25]
	    y[1].innerHTML=english[25]
    }else if(day==26 && month==8 && year==2012) {
	    y[0].innerHTML=hindi[26]
	    y[1].innerHTML=english[26]
    }else if(day==27 && month==8 && year==2012) {
	    y[0].innerHTML=hindi[27]
	    y[1].innerHTML=english[27]
    }else if(day==28 && month==8 && year==2012) {
	    y[0].innerHTML=hindi[28]
	    y[1].innerHTML=english[28]
    }else if(day==29 && month==8 && year==2012) {
	    y[0].innerHTML=hindi[29]
	    y[1].innerHTML=english[29]
    }else if(day==30 && month==8 && year==2012) {
	    y[0].innerHTML=hindi[30]
	    y[1].innerHTML=english[30]
    }else if(day==31 && month==8 && year==2012) {
	    y[0].innerHTML=hindi[31]
	    y[1].innerHTML=english[31]
    }

}
