'use strict';

let isValidIPNum = (num) => {
    let numVal = parseInt(num);
    let leadingZero = num[0] === '0' && num.length > 1;
    return !leadingZero && numVal <= 255;
}
let isValidIP = (nums) => {
    return nums.every((num) => isValidIPNum(num));
}

let main = () => {
    let n = parseInt(readline());
    let digits = readline().split(' ').map(Number);
    let ips = [];
    for (let i = 1; i < n; i++) {
        for (let j = i + 1; j < n; j++) {
            for (let k = j + 1; k < n; k++) {
                let first = digits.slice(0, i).join('');
                let second = digits.slice(i, j).join('');
                let third = digits.slice(j, k).join('');
                let fourth = digits.slice(k, n).join('');
                if (isValidIP([first, second, third, fourth])) {
                    ips.push(`${first}.${second}.${third}.${fourth}`);
                }
            }
        }
    }

    print(ips.length);
    print(ips.join('\n'))
}

main();

