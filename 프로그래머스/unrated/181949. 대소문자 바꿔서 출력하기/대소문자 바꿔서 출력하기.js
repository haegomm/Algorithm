const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input = [];

rl.on('line', function (line) {
    input = [line];
}).on('close',function(){
    str = input[0];
    const regex = /[A-Z]/
    console.log([...str].map((v)=> regex.test(v) ? v.toLowerCase() 
		: v.toUpperCase()).join(''))
});