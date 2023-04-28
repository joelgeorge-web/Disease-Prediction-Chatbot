// Collapsible


var coll = document.getElementsByClassName("collapsible");
const questions = ["Please enter the symptoms: "]
const sypmtoms = []

for (let i = 0; i < coll.length; i++) {
    coll[i].addEventListener("click", function () {
        this.classList.toggle("active");

        var content = this.nextElementSibling;

        if (content.style.maxHeight) {
            content.style.maxHeight = null;
        } else {
            content.style.maxHeight = content.scrollHeight + "px";
        }

    });
}

function getTime() {
    let today = new Date();
    hours = today.getHours();
    minutes = today.getMinutes();

    if (hours < 10) {
        hours = "0" + hours;
    }

    if (minutes < 10) {
        minutes = "0" + minutes;
    }

    let time = hours + ":" + minutes;
    return time;
}

// Gets the first message
function firstBotMessage() {
    let firstMessage = "Hi! I'm Medibot 😎."
    document.getElementById("botStarterMessage").innerHTML = '<p class="botText"><span>' + firstMessage + '</span></p>';

    let time = getTime();

    $("#chat-timestamp").append(time);
    document.getElementById("userInput").scrollIntoView(false);
    let secondMessage= "Please enter your Symptoms: "
    document.getElementById("botStarterMessage2").innerHTML = '<p class="botText"><span>' + secondMessage+ '</span></p>';

    time = getTime();

    $("#chat-timestamp").append(time);
    document.getElementById("userInput").scrollIntoView(false);
}

firstBotMessage();

async function getBotResponse(input) {
    // Simple responses
    // if (input == "hello" || input == "hi" || input == "hey" || input == "hola" || input == "bonjour" || input == "greetings" || input == "sup" | input == "yo" ) {
    //     return "Hello there!";
    // } else if (input == "goodbye" || input == "bye" || input == "see you later" ) {
    //     return "See you next time.";
    // } else {
    //     return "Try asking something else!";
    // }
    // response = 
    // ajax.jsonRpc('/web/dataset/call_kw', 'call', {
    //     'model': 'custom.model',
    //     'method': 'my_function',
    //     'args': [],
    //     'kwargs': {
    //         'context': {},
    //     }
    // }).then(function (data) {
    //     // Do something here
    // });
    return $.ajax({
        url:'/chat_response',
        data:{data:input},
        type:'POST' 
    });
    
    // return false;

}


// Retrieves the response
async function getHardResponse(userText) {
    let botResponse = await getBotResponse(userText);
    console.log(botResponse);
    let botHtml = '<p class="botText"><span>' + botResponse.disease + '</span></p>';
    $("#chatbox").append(botHtml);
    botHtml = '<p class="botText"><span>' + botResponse.description + '</span></p>';
    $("#chatbox").append(botHtml);
    botHtml = '<p class="botText"><span>' + botResponse.precaution + '</span></p>';
    $("#chatbox").append(botHtml);

    document.getElementById("chat-bar-bottom").scrollIntoView(true);
}

//Gets the text text from the input box and processes it
function getResponse() {
    let userText = $("#textInput").val();

    

    let userHtml = '<p class="userText"><span>' + userText + '</span></p>';

    $("#textInput").val("");
    $("#chatbox").append(userHtml);
    document.getElementById("chat-bar-bottom").scrollIntoView(true);

    setTimeout(() => {
        getHardResponse(userText);
    }, 1000)

}




// Press enter to send a message
$("#textInput").keypress(function (e) {
    if (e.which == 13) {
        getResponse();
    }
});