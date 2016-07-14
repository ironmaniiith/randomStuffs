// This should console.log() who starts typing in the opened message box in fb
// #BewareOfStalkers hahhahahhaha

function fbMessageTypingChecker(flag){
	// Check if someone starts typing in the opened message box
	// Should improve this as it users setInterval for who is typing
	a = document.getElementsByClassName('_5x7x _4a0v _4a0x');
	if (a.length){
		// I may open more than one message box for stalking. :V
		for (var i = 0; i < a.length; i++) {
			console.log(a[i].getAttribute('aria-label'));
			if(flag){
				//Send browser notification
				var notification = new Notification(a[i].getAttribute('aria-label'));
			}
		};
	}
}
var x = setInterval(fbMessageTypingChecker, 1000,true);