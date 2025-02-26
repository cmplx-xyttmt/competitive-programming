var HackerChallenge;


(function () {
    /* global $ */
    /* global riot */

    if (HackerChallenge === undefined) {
        HackerChallenge = {};
    }


    HackerChallenge.updatePointsCallback = function (new_points) {
        // Override this to get a callback when points are changed
        console.log("%cCongratulation. Current points = " + new_points, HackerChallenge.consoleFormat);
    }


    HackerChallenge.mobileCheck = function () {
        var check = false;
        (function (a) {
            if (/(android|bb\d+|meego).+mobile|avantgo|bada\/|blackberry|blazer|compal|elaine|fennec|hiptop|iemobile|ip(hone|od)|iris|kindle|lge |maemo|midp|mmp|mobile.+firefox|netfront|opera m(ob|in)i|palm( os)?|phone|p(ixi|re)\/|plucker|pocket|psp|series(4|6)0|symbian|treo|up\.(browser|link)|vodafone|wap|windows ce|xda|xiino/i.test(a) || /1207|6310|6590|3gso|4thp|50[1-6]i|770s|802s|a wa|abac|ac(er|oo|s\-)|ai(ko|rn)|al(av|ca|co)|amoi|an(ex|ny|yw)|aptu|ar(ch|go)|as(te|us)|attw|au(di|\-m|r |s )|avan|be(ck|ll|nq)|bi(lb|rd)|bl(ac|az)|br(e|v)w|bumb|bw\-(n|u)|c55\/|capi|ccwa|cdm\-|cell|chtm|cldc|cmd\-|co(mp|nd)|craw|da(it|ll|ng)|dbte|dc\-s|devi|dica|dmob|do(c|p)o|ds(12|\-d)|el(49|ai)|em(l2|ul)|er(ic|k0)|esl8|ez([4-7]0|os|wa|ze)|fetc|fly(\-|_)|g1 u|g560|gene|gf\-5|g\-mo|go(\.w|od)|gr(ad|un)|haie|hcit|hd\-(m|p|t)|hei\-|hi(pt|ta)|hp( i|ip)|hs\-c|ht(c(\-| |_|a|g|p|s|t)|tp)|hu(aw|tc)|i\-(20|go|ma)|i230|iac( |\-|\/)|ibro|idea|ig01|ikom|im1k|inno|ipaq|iris|ja(t|v)a|jbro|jemu|jigs|kddi|keji|kgt( |\/)|klon|kpt |kwc\-|kyo(c|k)|le(no|xi)|lg( g|\/(k|l|u)|50|54|\-[a-w])|libw|lynx|m1\-w|m3ga|m50\/|ma(te|ui|xo)|mc(01|21|ca)|m\-cr|me(rc|ri)|mi(o8|oa|ts)|mmef|mo(01|02|bi|de|do|t(\-| |o|v)|zz)|mt(50|p1|v )|mwbp|mywa|n10[0-2]|n20[2-3]|n30(0|2)|n50(0|2|5)|n7(0(0|1)|10)|ne((c|m)\-|on|tf|wf|wg|wt)|nok(6|i)|nzph|o2im|op(ti|wv)|oran|owg1|p800|pan(a|d|t)|pdxg|pg(13|\-([1-8]|c))|phil|pire|pl(ay|uc)|pn\-2|po(ck|rt|se)|prox|psio|pt\-g|qa\-a|qc(07|12|21|32|60|\-[2-7]|i\-)|qtek|r380|r600|raks|rim9|ro(ve|zo)|s55\/|sa(ge|ma|mm|ms|ny|va)|sc(01|h\-|oo|p\-)|sdk\/|se(c(\-|0|1)|47|mc|nd|ri)|sgh\-|shar|sie(\-|m)|sk\-0|sl(45|id)|sm(al|ar|b3|it|t5)|so(ft|ny)|sp(01|h\-|v\-|v )|sy(01|mb)|t2(18|50)|t6(00|10|18)|ta(gt|lk)|tcl\-|tdg\-|tel(i|m)|tim\-|t\-mo|to(pl|sh)|ts(70|m\-|m3|m5)|tx\-9|up(\.b|g1|si)|utst|v400|v750|veri|vi(rg|te)|vk(40|5[0-3]|\-v)|vm40|voda|vulc|vx(52|53|60|61|70|80|81|83|85|98)|w3c(\-| )|webc|whit|wi(g |nc|nw)|wmlb|wonu|x700|yas\-|your|zeto|zte\-/i.test(a.substr(0, 4))) check = true;
        })(navigator.userAgent || navigator.vendor || window.opera);
        return check;
    };


    HackerChallenge.getBinaryLink = function (subpath, link_name) {
        var url = HackerChallenge.binaryUrl + "/" + subpath;
        return $("<a href='" + url + "'>" + link_name + "</a>");
    };


    HackerChallenge.displayBinary = function (subpath, link_name, md5, sha256) {
        var link = HackerChallenge.getBinaryLink(subpath, link_name);
        var md5_html = $("<abbr>").text("MD5: ").append(
            $("<abbr title='" + md5 + "'>").text(md5)
        );
        var sha256_html = $("<abbr>").text("SHA256: ").append(
            $("<abbr title='" + sha256 + "'>").text(sha256.slice(0, 29) + "...")
        );
        return [
            link, $("<br>"),
            md5_html, $("<br>"),
            sha256_html, $("<br>"), $("<br>")
        ];
    };


    HackerChallenge.displayModedBinary = function (challenge_id, link_name, md5 = null, sha256 = null) {
        var url = HackerChallenge.interactChallengeUrl.replace("placeholder", challenge_id);
        var link = $(`<a href="${url}">${link_name}</a>`);
        var md5_html = null;
        var sha256_html = null;
        var ret = [link, $("<br>")];

        if (md5 != null) {
            md5_html = $("<abbr>").text("MD5: ").append(
                $("<abbr title='" + md5 + "'>").text(md5)
            );
            ret.push(md5_html, $("<br>"));
        }
        if (sha256 != null) {
            sha256_html = $("<abbr>").text("SHA256: ").append(
                $("<abbr title='" + sha256 + "'>").text(sha256.slice(0, 29) + "...")
            );
            ret.push(sha256_html, $("<br>"));
        }

        return ret;
    };


    HackerChallenge.submitAnswer = function (challenge_id, answer) {
        if (Array.isArray(answer) || typeof answer !== "string") {
            answer = JSON.stringify(answer);
        }

        return $.ajax({
            url: HackerChallenge.submitAnswerUrl,
            method: "POST",
            dataType: "json",
            data: {
                csrfmiddlewaretoken: HackerChallenge.csrfToken,
                challenge_id: challenge_id,
                answer: answer
            }
        });
    };


    HackerChallenge.resumeSession = function (account_id) {
        return $.ajax({
            url: HackerChallenge.resumeSessionUrl,
            method: "POST",
            dataType: "json",
            data: {
                csrfmiddlewaretoken: HackerChallenge.csrfToken,
                account_id: account_id
            }
        });
    };


    HackerChallenge.getChallenges = function () {
        return $.ajax({
            url: HackerChallenge.getChallengesUrl,
            dataType: "json"
        });
    };


    HackerChallenge.getChallenge = function (challenge_id) {
        var url = HackerChallenge.getChallengeUrl.replace("placeholder", challenge_id);
        return $.ajax({
            url: url,
            dataType: "json"
        });
    };


    HackerChallenge.stopTimer = function (display, reason = "timer.stop") {
        // Called to stop the timer regardless of where it is
        display.text("0");

        data = display.data();

        if (data._timerId) {
            clearInterval(data._timerId);
            data._timerId = undefined;
            if (data._timerPromise) {
                data._timerPromise.resolve(reason);
                data._timerPromise = undefined;
            }
        }
    };

    HackerChallenge.endTimer = function (display) {
        // Called if the timer completes (counts down to 0)
        HackerChallenge.stopTimer(display, reason = "timer.end");
    }

    HackerChallenge.startTimer = function (seconds, display, tick_cb = null) {
        // First, stop the current timer if there is one
        HackerChallenge.stopTimer(display);

        let timerPromise = $.Deferred();

        // Promise to return. This will be resolved when the timer runs out
        display.data("_timerPromise", timerPromise);

        seconds = Math.trunc(seconds);

        if (seconds < 0) {
            seconds = 0;
        }

        display.text(seconds);
        seconds = seconds - 1;

        var timerId = setInterval(function () {
            display.text(seconds);
            seconds = seconds - 1;

            if (tick_cb) {
                tick_cb(seconds);
            }

            if (seconds <= 0) {
                HackerChallenge.endTimer(display);
            }
        }, 1000);

        display.data("_timerId", timerId);

        return timerPromise;
    };


    HackerChallenge.formatAsSourceCode = function (text) {
        text.replace("\r\n", "<br>");
        text.replace("\n", "<br>");

        return "<div class='hackerchallenge-code'><pre><code>" + text + "</code></pre></div>";
    };
})();
