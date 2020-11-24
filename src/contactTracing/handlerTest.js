const express = require('express')
const app = express()

app.use(
    express.urlencoded({
        extended = true
    })
)
app.use(express.json());
console.log(app);
// const spawn = require('child_process').spawn;
// const process = spawn('python', ['./firebaseTest.py']);

// process.stdout.on('data', data => {
//     console.log(data.toString());
// })

// setInterval(testConsole, 10000);

// function testConsole(){
//     console.log('worker file is working');
// }
console.log('worker file is working');

