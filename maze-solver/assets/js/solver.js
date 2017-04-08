var HORIZONTAL = {},
    VERTICAL = {};

var hasOwnProperty = Object.prototype.hasOwnProperty;

var STEPS = {
    'up': [-1, 0],
    'down': [1, 0],
    'right': [0, 1],
    'left': [0, -1]
}

var ROWS = 16;
var COLS = 16;
var board = new Array(ROWS);
for (var i = 0; i < board.length; i++) {
    board[i] = new Array(COLS);
}

function check(x, y) {
    return (x >=0 && y >= 0) && (x < ROWS && y < COLS);
}

function isBlocked(x, y, dir) {
    step = STEPS[dir];
    if (dir === 'up' || dir === 'left') {
        coordinate = mergeAndAdd([x, y], step);
        x = coordinate['x'];
        y = coordinate['y'];
    }
    var ans;
    if (dir === 'up' || dir === 'down') {
        ans = !!HORIZONTAL['' + x + '-' + y];
    } else {
        ans = !!VERTICAL['' + x + '-' +  y];
    }
    return ans;
}

function colorIt(coordinate, color, over_write) {
    color = color || YELLOW;
    var block = getBlockById(coordinate[0] * ROWS + coordinate[1]);
    if (!block.style.background || over_write)
        block.style.background = color;
}

function mergeAndAdd(a, b) {
    return {
        'x': a[0] + b[0],
        'y': a[1] + b[1]
    }
}

function setup() {
    horizontal_lines.forEach(function(coordinate) {
        var x = coordinate[0],
            y = coordinate[1];
        HORIZONTAL['' + x + '-' + y] = true;
    });
    vertical_lines.forEach(function(coordinate) {
        var x = coordinate[0],
            y = coordinate[1];
        VERTICAL['' + x + '-' + y] = true;
    });
    colorIt(start, YELLOW);
    solutions.forEach(function(solution) {
        colorIt(solution, GREEN);
    });
}

var start = [15, 0];
var solutions = [[7, 7], [7, 8], [8, 7], [8, 8]];
var stack = slice.call(solutions);
var counter = 0;
setup();
var PRINTING_SPEED = 50;
var SETTING_SPEED = 50;
function setCounter() {
    if (!(board[start[0]][start[1]] === undefined)) {
        counter--;
        printSolution();
        return;
    }
    var nextValues = [];
    while (stack.length) {
        var val = stack.pop();
        var x = val[0],
            y = val[1],
            index = x * ROWS + y;
        board[x][y] = counter;
        var block = getBlockById(val[0] * ROWS + val[1]);
        block.innerHTML = counter;
        colorIt(val);
        nextValues.push(val);
    }
    while (nextValues.length) {
        var val = nextValues.pop();
        for (var dir in STEPS) {
            if (hasOwnProperty.call(STEPS, dir)) {
                var coordinates = mergeAndAdd(val, STEPS[dir]),
                    x = coordinates['x'],
                    y = coordinates['y'];
                if (check(x, y) && !isBlocked(val[0], val[1], dir) && board[x][y] === undefined) {
                    stack.push([x, y]);
                }
            }
        }
    }
    counter++;
    setTimeout(setCounter, SETTING_SPEED);
};
setCounter();

function printSolution() {
    if (board[start[0]][start[1]] === 0) {
        return;
    }
    colorIt(start, GREEN, true);
    var values = [];
    var final_coordinates = [];
    for (var dir in STEPS) {
        if (hasOwnProperty.call(STEPS, dir)) {
            var coordinates = mergeAndAdd(start, STEPS[dir]),
                x = coordinates['x'],
                y = coordinates['y'];
            if (check(x, y) && board[x][y] !== undefined && !isBlocked(start[0], start[1], dir)) {
                values.push(board[x][y]);
                final_coordinates.push([x, y]);
            }
        }
    }
    var index = values.indexOf(--counter);
    start = final_coordinates[index];
    setTimeout(printSolution, PRINTING_SPEED);
}