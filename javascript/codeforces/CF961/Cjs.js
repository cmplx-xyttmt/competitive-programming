'use strict';
let main = () => {
    let t = parseInt(readline());
    while (t--) {
        solve();
    }
}

let solve = () => {
    let n = parseInt(readline());
    let a = readline().split(' ').map(Number)

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

main();
