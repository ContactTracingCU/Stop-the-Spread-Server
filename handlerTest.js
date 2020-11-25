const express = require('express');
const ip = require('ip');
const app = express();
const ipAddress = ip.address();
const port = 3000;

const spawn = require('child_process').spawn;
const process = spawn('python', ['./firebaseTest.py']);

process.stdout.on('data', data => {
    console.log(data.toString());
    console.log('worker file runs firebaseTest.py');
})

// app.get('/', (req, res) => res.send('Worker reached.'));

// app.listen(port, () => {
//     console.log(`Worker access @ ${ipAddress} : ${port}`);
// })



// setInterval(testConsole, 10000);

// function testConsole(){
//     console.log('worker file is working');
// }
// console.log('worker file is working');

