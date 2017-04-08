var GREEN = 'rgb(124, 252, 0)',
    YELLOW = 'yellow',
    WHITE = 'white';

var slice = Array.prototype.slice;
var x = slice.call(document.getElementsByClassName('square'));
x.forEach(function(val) {
    val.addEventListener('click', function(){
        var background = this.style.background;
        if (background === YELLOW) {
            this.style.background = GREEN;
        } else if (background === GREEN) {
            this.style.background = WHITE;
        } else {
            this.style.background = YELLOW;
        }
    });
});
