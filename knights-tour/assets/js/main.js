/** Globals or cache methods */
ROWS = parseInt(prompt("Enter the size of the board"));
COLS = ROWS;
var slice = Array.prototype.slice,
    toString = Object.prototype.toString,
    D = document,
    max_length = 5.3 * 8, // Calculated for standard 8x8 chess board that fits on browser
    board = [];

var KNIGHT = 'assets/img/knight.svg';
var KNIGHT_IMAGE = D.createElement('img'); // Use a single instance so as to not remove the already placed knight
KNIGHT_IMAGE.src = KNIGHT;

function getSingleRow(no_of_cols, idOffset, tdClass, trClass) {
    var tr = D.createElement('tr');
    idOffset = idOffset || 0;
    no_of_cols = no_of_cols || COLS;
    tr.className = trClass || 'row';
    var rowArray = [];
    for (var i = 0; i < no_of_cols; i++) {
        var td = D.createElement('td');
        var id = i + idOffset;
        td.id = setBlockId(id);
        setBlockCss(td);
        td.className = tdClass || 'square ' + (((i + idOffset / ROWS)% 2 === 0) ? 'white' : 'black');
        tr.appendChild(td);
        rowArray.push(td);
    }
    return { 'tr': tr, 'rowArray': rowArray };
}

function setBlockCss(td) {
    td.style.width = max_length / ROWS + 'em';
    td.style.height = max_length / ROWS + 'em';
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

(function main(){
    var table = D.getElementById('board');
    for (var i = 0; i < ROWS; i++) {
        var row = getSingleRow(ROWS, i * ROWS);
        table.appendChild(row.tr);
        board.push(row.rowArray);
    }
})();

function putKnight(id, counter) {
    var block = getBlockById(id);
    if (block) {
        block.appendChild(KNIGHT_IMAGE);
        var span = D.createElement('span');
        span.innerHTML = counter;
        var font_size = (max_length) / (1.8 * ROWS);
        span.style['font-size'] = font_size + 'em';
        span.style.top = font_size / (ROWS * ROWS) + 'em';
        span.className = 'text';
        block.appendChild(span);
    }
}
