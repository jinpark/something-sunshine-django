$(document).ready(function(){
   var sheet = document.createElement('style'),
       $rangeInput = $('.seekbar'),
       prefs = ['webkit-slider-runnable-track', 'moz-range-track', 'ms-track'];

   document.body.appendChild(sheet);

   var getTrackStyle = function (el) {
       var curVal = el.value,
           style = '';

       for (var i = 0; i < prefs.length; i++) {
           style += '.seekbar::-' + prefs[i] + '{background: linear-gradient(to right, #ffab40 0%, #ffab40 ' + curVal + '%, #ddd ' + curVal + '%, #ddd 100%) !important; }';
       }

       return style;
   }

   $rangeInput.on('change', function () {
       sheet.textContent = getTrackStyle(this);
   }); 
})
