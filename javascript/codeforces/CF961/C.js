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

function solve() {
    let n = parseInt(readLine());
    let a = readLine().split(' ').map(Number)

    let prevTimes = 0;
    let prev = 0;
    let times = 0;
    let cant = false;
    a.forEach(num => {
        let newTimes = 0;
        if(cant || (num === 1 && prev > num)) {
           cant = true;
        } else {
            if(prev >= 2) {
                newTimes = 0;
                newTimes = Math.max(0, Math.ceil(prevTimes + Math.log2(Math.log2(prev) / Math.log2(num))));
            }
            times += newTimes;
        }
        // console.log(num, prev)
        prev = num;
        prevTimes = newTimes;
    });

    if(cant) {
        print(-1);
    } else print(times);
}
// comparison:
// log (x ^ 2i) < (y ^ 2j)
// 2i log x < 2j log y
// (2i log x / (2 * log y)) < j


let main = () => {
    let t = parseInt(readLine());
    while (t--) {
        solve();
    }
}
