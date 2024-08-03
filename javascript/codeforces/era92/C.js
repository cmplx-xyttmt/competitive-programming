'use strict';
process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', input => inputString += input);
process.stdin.on('end', _=> {
    inputString = inputString.trim().split('\n').map(string => string.trim());
    main()
});

function readLine() {
    return inputString[currentLine++];
}

function print(arg) {
    arg = arg.toString();
    process.stdout.write(`${arg}\n`);
}

let main = () => {
    let n = parseInt(readLine());
    let params = [];
    let problems = [];
    let answer = 0;
    for (let i = 0; i < n; i++) {
        let inefficientPairs = 0;
        let line = readLine().split(' ').map(Number);
        let k = line[0];
        let a1 = BigInt(line[1]);
        let x = BigInt(line[2]);
        let y = BigInt(line[3]);
        let m = BigInt(line[4]);

        let newProblem = a1;
        let prevProblem = -1;
        for (let j = 0; j < k; j++) {
            if (newProblem < prevProblem) {
                inefficientPairs += 1;
            }
            if (problems.length < 200000) {
                problems.push([inefficientPairs, newProblem, i]);
            }
            // print("debug", prevProblem, newProblem, inefficientPairs);
            prevProblem = newProblem;
            newProblem = (prevProblem * x + y) % m;
        }
        answer = Math.max(answer, inefficientPairs);
    }
    print(answer);
    if(problems.length <= 200000) {
        problems.sort((p1, p2) => {
            if (p1[0] === p2[0]) {
                return Number(p1[1] - p2[1]);
            }
            return Number(p1[0] - p2[0]);
        });
        problems.forEach((problemArray) => {
            print(`${problemArray[1]} ${problemArray[2] + 1}`);
        })
    }
}
