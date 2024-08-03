'use strict';

const mod = 1000000007;
const maxIntegerValue = Number.MAX_SAFE_INTEGER;

// let mod_pow = (x, n, m) => {
//     if (n === 0) {
//         return 1;
//     }
//     let u = mod_pow(x, Math.floor(n / 2), m);
//     u = (u * u) % m;
//     if(n % 2 === 1) u = (u * x) % m;
//     return u;
// }
//
// let mod_inverse = (x, m) => {
//     return mod_pow(x, m - 2, m);
// }

let main = () => {
    let nk = readline().split(' ').map(Number);
    let array = readline().split(' ').map(Number);

    let n = nk[0];
    let k = nk[1];

    let currentProduct = 1;
    for (let i = 0; i < k; i++) {
        currentProduct = (currentProduct * array[i]) % mod;
    }

    let maxProduct = currentProduct;
    for (let i = k; i < n; i++) {
        currentProduct = (currentProduct * array[i]) % mod;
        currentProduct = Math.floor(currentProduct / array[i - k]);

        maxProduct = Math.max(maxProduct, currentProduct);
    }

    print(maxProduct);
}

main();
