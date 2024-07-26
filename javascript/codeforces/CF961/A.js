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
    process.stdout.write(arg);
}

function solve() {
    let [n, k] = readLine().split(' ').map(Number);
    let currentCells = n;
    let occupiedDiagonals = 0
    while (k > 0 && currentCells > 0) {
        k -= currentCells;
        occupiedDiagonals += 1
        if(currentCells < n && k > 0) {
            occupiedDiagonals += 1
            k -= currentCells;
        }
        currentCells -= 1;
    }

    print(`${occupiedDiagonals}\n`);
}

let main = () => {
    let t = parseInt(readLine());
    while (t--) {
        solve();
    }
}
