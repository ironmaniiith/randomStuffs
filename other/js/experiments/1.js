/* 
http://www.dailymail.co.uk/sciencetech/article-3033455/How-good-colour-vision-KukuKube-app-tests-ability-subtle-differences-shade-leave-cross-eyed.html
*/
var win = function (){
	var a = Array.prototype.slice.call(document.getElementById('box').getElementsByTagName('span'));
	var d = {};
	a.forEach(function(val, index){
		var color = val.style['backgroundColor'];
		d[color] ? d[color][index] = index : d[color] = {'index': index, 'count': 0};
		d[color]['count'] += 1;
	});
	for(var i in d){if (!(d[i]['count']^1)){a[d[i]['index']].click()}};
}
var x = setInterval(win, 100);