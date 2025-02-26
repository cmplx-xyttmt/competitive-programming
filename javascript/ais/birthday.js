format_value = (value) => {
    if (value < 10) return `0${value}`
    else return `${value}`
}

all_dates = () => {
    let dates = [];
    for (let month = 1; month <= 12; month++) {
        for (let day = 1; day <= 31; day++) {
            dates.push(`${format_value(month)}/${format_value(day)}`)
        }
    }
    return dates;
}
find_birthday = async (dates) => {
    var found = false;
    let failedDates = [];
    for(const date of dates){
        if (!found) {
            const resp = await HackerChallenge.submitAnswer("birthday", date)
            if (resp.status === 200) {
                console.log(data);
                found = true;
            } else if (resp.status === 500) {
                failedDates.push(date);
            } else if(resp.status !== 400) {
                console.log("Mysterious failure!!!");
            }
        }
    }
    return {"found": found, "failedDates": failedDates}
}

const dates_ = all_dates();
find_birthday(dates_.slice(0, 3));
