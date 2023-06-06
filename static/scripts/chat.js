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
    let hours = today.getHours();
    let minutes = today.getMinutes();
    let ampm = hours >= 12 ? 'PM' : 'AM';

    // Convert hours to 12-hour format
    hours = hours % 12;
    hours = hours ? hours : 12;

    if (hours < 10) {
        hours = "0" + hours;
    }

    if (minutes < 10) {
        minutes = "0" + minutes;
    }

    let time = hours + ":" + minutes + " " + ampm;
    console.log(time);
    return time;
}


// Gets the first message
function firstBotMessage() {
    let firstMessage = "Hi! I'm Medibot 😎."
    document.getElementById("botStarterMessage").innerHTML = '<p class="botText"><span>' + firstMessage + '</span></p>';

    let time = getTime();

    $("#chat-timestamp").append(time);
    document.getElementById("userInput").scrollIntoView(false);
    let secondMessage= "Please enter your symptoms: "
    document.getElementById("botStarterMessage2").innerHTML = '<p class="botText"><span>' + secondMessage+ '</span></p>';

    // time = getTime();

    // $("#chat-timestamp").append(time);
    document.getElementById("userInput").scrollIntoView(false);
}

firstBotMessage();

async function getBotResponse(input) {
  
    return $.ajax({
        url:'/chat_response',
        data:{data:input},
        type:'POST' 
    });
    
    

}



async function getHardResponse(userText) {
    let botResponse = await getBotResponse(userText);
    console.log(botResponse);
    Object.values(botResponse).forEach(function (value) {
        let botHtml = '<p class="botText"><span>' + value + '</span></p>';
        $("#chatbox").append(botHtml);
    })


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