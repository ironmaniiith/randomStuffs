var page = require('webpage').create(),
    system = require('system');

page.onConsoleMessage = function(msg) {
    console.log(msg);
};

if(system.args.length<3){
    console.log("usage <inputLanguage> <outputLanguage> <text to convert>");
    phantom.exit();
}

var inputLanguage = system.args[1];
var outputLanguage = system.args[2];
var text = "";

for (var i = 3; i < system.args.length; i++) {
    text+=system.args[i];
    text+=" ";
};

text = text.replace(/ /g, "%20");
console.log(text);

page.open('https://translate.google.com/#' + inputLanguage + '/' + outputLanguage + '/' + text, function (status) {
    if (status !== "success") {
        console.log("Unable to access network");
    } else {
        page.evaluate(function(x) {
            var temp = document.getElementById('result_box');
            var finalText = temp.innerHTML.replace(/<\/span>/g, "");
            finalText = finalText.replace(/<span[^>]*>/g, "");
            console.log(finalText);
            
        });
    }
    phantom.exit();
});