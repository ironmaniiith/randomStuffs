var generator = require('./generate');
 
var passwordLength = 8;
var password = generator.generateMultiple(passwordLength, {
	length: passwordLength,
	numbers: true,
	uppercase: true,
	// symbols: true,
});
 
for (var i = 0; i < passwordLength; i++) {
	process.stdout.write(password[i][i]);
}
console.log();
// console.log(password); // Your unique password 