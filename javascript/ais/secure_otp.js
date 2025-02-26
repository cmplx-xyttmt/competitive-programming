/**
 * =============+SOLUTION START==================
 */

let resp;
const get_values = () => {
    const n_digit_vals = (prev_vals) => {
        let new_vals = []
        for (let val of prev_vals) {
            for (let i = 0; i < 10; i++) {
                new_vals.push(`${val}${i}`)
            }
        }
        return new_vals;
    }

    let one_digit = n_digit_vals([""])
    return n_digit_vals(n_digit_vals(n_digit_vals(n_digit_vals(n_digit_vals(one_digit)))));
}

// HackerChallenge.submitAnswer("secure_otp", "679044")
//     .then((response) => {
//         resp = response;
//     })
//     .catch((error) => {
//         console.error('Error: ', error);
//     })
const guess_answer = (guesses) => {
    for (let guess in guesses) {
        HackerChallenge.submitAnswer("secure_otp", guess)
            .then((response) => {
                console.log("The answer is: ", guess)
            })
            .catch((error) => {
                const responseJson = error["responseJSON"];
                console.log(responseJson.error)
                console.log(responseJson.hc_challenge["hint"]);
                console.log(responseJson.hc_challenge["last_error"]);
                console.log(responseJson.hc_challenge["seed"]);
            })
    }
}


console.log(get_values().slice(0, 10))
