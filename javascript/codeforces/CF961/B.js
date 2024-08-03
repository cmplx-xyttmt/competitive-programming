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

function petals(costLimit, a, aNum, a1Num) {
    // console.log(`${a} -> ${aNum} ; ${a + 1} -> ${a1Num}`);
    let aNum_ = Math.min(aNum, Math.floor(costLimit / a));
    let a1Num_ = Math.min(a1Num, Math.floor(costLimit / (a + 1)));
    let maxPetals = a * aNum_ + (a + 1) * a1Num_;
    if(maxPetals <= costLimit) {
        return maxPetals;
    }

    let ans = aNum_ * a;
    let remainder = costLimit - ans;
    let a1Add = Math.floor(remainder / (a + 1));
    ans += (a1Add * (a + 1));

    let remA1 = a1Num_ - a1Add;
    let diff = costLimit - ans;
    ans += Math.min(aNum_, diff, remA1);
    return ans;
}

function solve() {
    let line1 = readLine().split(' ').map(Number);
    let n = line1[0];
    let m = line1[1];
    let array = readLine().split(' ').map(Number);
    const numCount = {}
    array.forEach(num => {
        if (num in numCount) {
            numCount[num] += 1;
        } else {
            numCount[num] = 1;
        }

    });
    let eachPetals = Object.keys(numCount).map((aString) => {
        let a = parseInt(aString);
        return petals(m, a, numCount[a], ((a + 1) in numCount ? numCount[a + 1] : 0));
    });
    let maxPetals = Number.NEGATIVE_INFINITY;
    eachPetals.forEach(petal => {
        maxPetals = Math.max(maxPetals, petal);
    })
    print(maxPetals);
}

let main = () => {
    let t = readLine();
    while (t--) {
        solve();
    }
}
