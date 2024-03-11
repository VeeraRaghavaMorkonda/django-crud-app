var slideShowSpeed = 4000
var crossFadeDuration = 2
var Pic = new Array() 

Pic[0] = 'http://10.35.1.10/gmtrp/hindi/balaji/balaji.jpg'
Pic[1] = 'http://10.35.1.10/gmtrp/hindi/balaji/balaji1.jpg'
Pic[2] = 'http://10.35.1.10/gmtrp/hindi/balaji/balaji2.jpg'
Pic[3] = 'http://10.35.1.10/gmtrp/hindi/balaji/balaji3.jpg'


var t
var j = 0
var p = Pic.length

var preLoad = new Array()
for (i = 0; i < p; i++){
   preLoad[i] = new Image()
   preLoad[i].src = Pic[i]
}

function runSlideShow(){
   if (document.all){
      document.images.SlideShow.style.filter="blendTrans(duration=2)"
      document.images.SlideShow.style.filter="blendTrans(duration=crossFadeDuration)"
      document.images.SlideShow.filters.blendTrans.Apply()      
   }
   document.images.SlideShow.src = preLoad[j].src
   if (document.all){
      document.images.SlideShow.filters.blendTrans.Play()
   }
   j = j + 1
   if (j > (p-1)) j=0
   t = setTimeout('runSlideShow()', slideShowSpeed)
}