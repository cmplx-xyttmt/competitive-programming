'use strict';
let main = () => {
    let n = parseInt(readline());
    let cubesUsed = 0;
    let counter = 1;
    let level = 1;
    let height = 0;
    while (cubesUsed + level <= n) {
        height += 1;
        cubesUsed += level;
        counter += 1
        level += counter;
    }
    print(height);
}

main();
