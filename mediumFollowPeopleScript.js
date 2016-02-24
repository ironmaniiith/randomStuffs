envs : {
	browser: true;
}
var followButtons;
var showMorePeople;

var clickShowMore = function(pressButton, successCB, errorCB) {
	if(pressButton.length){
		pressButton[0].click();
		if(successCB){
			successCB();
		}
	}
	else{
		if(errorCB){
			errorCB();
		}
	}
}

var hasClass = function (element, cls) {
    return (' ' + element.className + ' ').indexOf(' ' + cls + ' ') > -1;
}

var clickFollow = function(pressButton, successCB, errorCB) {
	if(!pressButton) {
		if(errorCB)	errorCB();
	}
	else {
		pressButton.click();
		if(successCB){
			successCB();
		}
	}
}

var indexOfFollowButtons = 1;

var x = setInterval(function(x) {
	
	followButtons = document.getElementsByClassName('button-label  button-defaultState js-buttonLabel');
	
	for(var i=indexOfFollowButtons;i<followButtons.length; i++){
		// if(followButtons[i].innerHTML.indexOf("Following") < 0 && followButtons[i].innerHTML.indexOf("Follow") >= 0){
			if(hasClass(followButtons[i].closest('button'), 'is-active')){
				console.log("Is already active, skipping...")
				continue;
			}
			else{
				clickFollow(followButtons[i], function(){
					console.log("Followed");
				}, function(){
					console.log("Some error occured");
				});
			}
		// }
	}

	indexOfFollowButtons = followButtons.length;
	showMorePeople = document.getElementsByClassName('button button--small button--withChrome js-buttonMoreFollows');
	if(showMorePeople.length){
		clickShowMore(showMorePeople, function(){
			console.log("Opened follow links for more people");
		}, function(){
			console.log("Some error occured");
		});
	}

}, 5000);