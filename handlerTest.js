console.log('1');
const spawn = require('child_process').spawn;
const process = spawn('python', ['./firebaseTest.py']);
console.log('2');
process.stdout.on('data', data => {
    console.log(data.toString());
    console.log('worker file runs firebaseTest.py');
})
console.log('3');

// setInterval(testConsole, 10000);

// function testConsole(){
//     console.log('worker file is working');
// }
// console.log('worker file is working');

