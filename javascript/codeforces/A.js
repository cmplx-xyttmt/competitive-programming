process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', input => inputString += input);
process.stdin.on('end', _ => {
    inputString = inputString.trim().split('\n').map(string => string.trim());
    main()
});

function readLine() {
    return inputString[currentLine++];
}

function print(arg) {
    arg = arg.toString();
    process.stdout.write(arg);
}

function solve() {
    let n = parseInt(readLine());
    let a = readLine().split(' ').map(Number);
    let maxNumber = 0;
    for (let i = 0; i < n; i += 2) {
        maxNumber = Math.max(maxNumber, a[i]);
    }
    print(`${maxNumber}\n`);
}

let main = () => {
    let t = parseInt(readLine());
    while (t--) {
        solve();
    }
}