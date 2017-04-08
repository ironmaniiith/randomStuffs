/** Knight's tour solver */
var board_size, board = [];
var steps = [
    [-1, 2],
    [1, 2],
    [2, 1],
    [2, -1],
    [1, -2],
    [-1, -2],
    [-2, -1],
    [-2, 1]
];
var step_duration = 250; // in ms

function initializeBoard(n) {
    board_size = n;
    var i = -1, j = -1;
    while (++i < board_size) {
        board[i] = [];
        // initialize a 2d array
        j = -1;
        while (++j < board_size)
            board[i][j] = 0;
    }
}

function printBoard() {
    var indices = [];
    var i, j, val, counter = -1;
    for (i = 0; i < board_size; i++) {
        for (j = 0; j < board_size; j++) {
            val = board[i][j];
            indices[val] = i * board_size + j;
        }
    }
    var runner_idx = 0; // Yes, it's 0, not -1
    var runner = setInterval(function() {
        if (++runner_idx > board_size * board_size)
            clearInterval(runner);
        else {
            putKnight(indices[runner_idx], runner_idx);
        }
    }, step_duration);
}

function updateBoard(i, j, counter) {
    board[i][j] = counter;
}

function isUnvisited(i, j) {
    return board[i][j] === 0;
}

function totalPaths(x, y, checker) {
    checker = checker || isUnvisited;
    var i, j, path_count = 0, idx = -1, len = steps.length;
    while (++idx < len) {
        i = x + steps[idx][0];
        j = y + steps[idx][1];
        if (isValid(i, j) && checker(i, j))
            path_count++;
    }
    return path_count;
}

function isValid() {
    var args = slice.call(arguments);
    for (var i = 0; i < args.length; i++)
        if (args[i] < 0 || args[i] >= board_size)
            return false;
    return true;
}

function knights_tour(x, y, counter) {
    updateBoard(x, y, counter);
    if (counter === board_size * board_size)
        return true;
    var paths = [], idx = -1, len = steps.length;
    var i, j, path_count, path;
    
    while (++idx < len) {
        i = x + steps[idx][0];
        j = y + steps[idx][1];
        if (isValid(i, j) && isUnvisited(i, j)) {
            path_count = totalPaths(i, j);
            paths.push({
                count: path_count,
                i: i,
                j: j
            });
        }
    }
    len = paths.length;
    if (len) {
        paths.sort(function(a, b) {
            return a.count - b.count;
        });
        idx = -1;
        while (++idx < len) {
            path = paths[idx];
            i = path.i;
            j = path.j;
            if (knights_tour(i, j, counter + 1))
                return true;
            else
                updateBoard(i, j, 0); // Backtrack
        }
    }
    return false;
}

function solver(size) {
    initializeBoard(size);
    if (knights_tour(0, 0, 1))
        printBoard();
    else
        alert('No knight tour found for N = ' + size);
}
setTimeout(function() {
    solver(ROWS);
}, 3000);