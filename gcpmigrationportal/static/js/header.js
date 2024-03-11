var speed = 50;
var cycledelay = 2000;
var maxsize = 28;

var x = 0;
var y = 0;
var themessage, size;
var esize = "</font>";

function initArray() {
this.length = initArray.arguments.length;
for (var i = 0; i < this.length; i++) {
this[i] = initArray.arguments[i];
   }
}
var themessage2 = new initArray(
"<font color=red>तिरूपति एस.एस.ए में आपका हार्दिक स्‍वागत है ।</font>",
"<font color=blue>WELCOME TO TIRUPATI SSA</font>",
"<font color=green>తిరుపతి ఎస్.ఎస్.ఎ కి హ్రుధయపూర్వక స్వాగతము</font>"
);
if(navigator.appName == "Netscape")
document.write('<layer id="wds"></layer><br>');
if (navigator.appVersion.indexOf("MSIE") != -1)
document.write('<span id="wds"></span><br>');
function upwords(){ 
themessage = themessage2[y];
if (x < maxsize) {
x++;
setTimeout("upwords()",speed);
}
else setTimeout("downwords()",cycledelay);

if(navigator.appName == "Netscape") {
size = "<font point-size='"+x+"pt'>"; 
document.wds.document.write(size+"<center>"+themessage+"</center>"+esize);
document.wds.document.close();
}
if (navigator.appVersion.indexOf("MSIE") != -1){
wds.innerHTML = "<center>"+themessage+"</center>";
wds.style.fontSize=x+'px'
   }
} 
function downwords(){
if (x > 1) {
x--;
setTimeout("downwords()",speed);
}
else {
setTimeout("upwords()",cycledelay);
y++;
if (y > themessage2.length - 1) y = 0;
}
if(navigator.appName == "Netscape") {
size = "<font point-size='"+x+"pt'>"; 
document.wds.document.write(size+"<center>"+themessage+"</center>"+esize);
document.wds.document.close();
}
if (navigator.appVersion.indexOf("MSIE") != -1){
wds.innerHTML = "<center>"+themessage+"</center>";
wds.style.fontSize=x+'px'
   }
}
setTimeout("upwords()",speed);