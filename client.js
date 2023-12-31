const net = require("net");
const config = require('./config.json');
const { resolve } = require("path");
const server_address = config['filepath'];

const client = new net.Socket();

const request = {
    method: "",
    params: "",
    id: ""
};

function readUserInput(question) {
    const readline = require('readline').createInterface({
        input: process.stdin,
        output: process.stdout
    });

    return new Promise((resolve, reject) => {
        readline.question(question, (answer) => {
            resolve(answer);
            readline.close();
        });
    });
}

(async function main() {

    method = await readUserInput('Input Method is selecting a number\n 1 : floor, 2 : nroot, 3 : reverse, 4 : validAnagram, 5 : sort \n-- > ');
    params = await readUserInput('Input params --> ');
    id = await readUserInput('Input Id --> ');

    method = config['function'][method]
    request.method = method == "" ? request.method : method;
    request.params = params == "" ? request.params : params;
    request.id = id == "" ? request.id : id;

    console.log(request);

    client.connect(server_address, () => {
        console.log('Connected to server');

        client.write(JSON.stringify(request));
    });

    client.on('data', (data) => {
        const response = JSON.parse(data);

        if (response.error) {
            console.error('Error:', response.error);
        } else {
            console.log(response);
        }

        client.end();
    });

    client.on('close', () => {
        console.log('Connection closed');
    });

    client.on('error', (error) => {
        console.error('Error:', error);
    });

})();