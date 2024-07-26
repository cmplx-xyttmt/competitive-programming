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

const bigIntMax = (...args) => args.reduce((m, e) => e > m ? e : m);
const bigIntMin = (...args) => args.reduce((m, e) => e < m ? e : m);

function petals(costLimit, a, aNum, a1Num) {
   let aNum_ = bigIntMin(aNum, costLimit / a);
    let a1Num_ = bigIntMin(a1Num, costLimit / (a + BigInt(1)));
    let maxPetals = a * aNum_ + (a + BigInt(1)) * a1Num_;
    // if(limitCopy === BigInt(10330)) {
    //     console.log(`${a} ${aNum} ${a1Num} -> ${ans}`);
    // }
    if(maxPetals <= costLimit) {
        return maxPetals;
    }

    let ans = aNum_ * a;
    let remainder = costLimit - ans;
    let a1Add = remainder / (a + BigInt(1));
    ans += (a1Add * (a + BigInt(1)));

    let remA1 = a1Num_ - a1Add;
    let diff = costLimit - ans;
    ans += bigIntMin(aNum_, diff, remA1);
    return ans;
}

function solve() {
    let [n, m] = readLine().split(' ').map(BigInt);
    let petalNums = readLine().split(' ').map(BigInt);
    let quantity = readLine().split(' ').map(BigInt);
    const numCount = {};
    petalNums.forEach((p, i) => numCount[p] = quantity[i]);

    let eachPetals = petalNums.map((p) => {
        let p1 = (p + BigInt(1)) in numCount ? numCount[p + BigInt(1)] : BigInt(0);
        return petals(m, p, numCount[p], p1);
    });
    // console.log(eachPetals)

    let maxPetals = Number.NEGATIVE_INFINITY;
    eachPetals.forEach(petal => {
        maxPetals = bigIntMax(maxPetals, petal);
    });
    print(maxPetals);
}

let main = () => {
    let t = readLine();
    while (t--) {
        solve();
    }
}