/** Globals or cache methods */
var slice = Array.prototype.slice,
    toString = Object.prototype.toString,
    D = document,
    ROWS = 16,
    COLS = 16,
    board = [];

function getSingleRow(no_of_cols, idOffset, tdClass, trClass) {
    var tr = D.createElement('tr');
    idOffset = idOffset || 0;
    no_of_cols = no_of_cols || 16;
    tr.className = trClass || 'row';
    var rowArray = [];
    for (var i = 0; i < no_of_cols; i++) {
        var td = D.createElement('td');
        td.id = setBlockId(i + idOffset);
        td.className = tdClass || 'square';
        tr.appendChild(td);
        rowArray.push(td);
    }
    return { 'tr': tr, 'rowArray': rowArray };
}

function setBlockId(id) {
    return 'block-' + id;
}

function getBlockById(id) {
    return D.getElementById('block-' + id);
}

function setCss(property, style, el){
    var elements = slice.call(arguments, 2);
    elements.forEach(function(el) {
        el.style[property] = style;
    });
}

function setBorder() {
    var wallBorder = '1px solid red',
        length = board.length;

    for (var i = 0; i < length; i++) {
        var blocks = new Array(4);
        blocks[0] = ['border-top', wallBorder, board[0][i]],
        blocks[1] = ['border-bottom', wallBorder, board[length - 1][i]],
        blocks[2] = ['border-left', wallBorder, board[i][0]],
        blocks[3] = ['border-right', wallBorder, board[i][length - 1]];
        blocks.forEach(function(block) {
            setCss.apply(null, block);
        });
        delete blocks;
    }
}

function constructBorder() {
    constructHorizontalBorder(horizontal_lines);
    constructVerticalBorder(vertical_lines);
}

function constructHorizontalBorder(horizontal_lines) {
    var wallBorder = '1px solid red';
    if (toString.call(horizontal_lines) === '[object Array]') {
        horizontal_lines.forEach(function(val) {
            var index1 = val[0] * ROWS + val[1];
                index2 = index1 + COLS;

            var topBlock = getBlockById(index1),
                bottomBlock = getBlockById(index2),
                bottom = ['border-bottom', wallBorder, topBlock],
                top = ['border-top', wallBorder, bottomBlock];

            setCss.apply(null, bottom);
            setCss.apply(null, top);
        });
    }
}

function constructVerticalBorder(vertical_lines) {
    var wallBorder = '1px solid red';
    if (toString.call(vertical_lines) === '[object Array]') {
        vertical_lines.forEach(function(val) {
            var index1 = val[0] * ROWS + val[1];
                index2 = index1 + 1;

            var leftBlock = getBlockById(index1);
                rightBlock = getBlockById(index2);
                right = ['border-right', wallBorder, leftBlock];
                left = ['border-left', wallBorder, rightBlock];
            setCss.apply(null, right);
            setCss.apply(null, left);
        });
    }
}

(function main(){
    var no_of_rows = 16,
        no_of_cols = 16,
        table = D.getElementById('board');

    for (var i = 0; i < no_of_rows; i++) {
        var row = getSingleRow(16, i * 16);
        table.appendChild(row['tr']);
        board.push(row['rowArray']);
    }
    setBorder();
    constructBorder();
})();
