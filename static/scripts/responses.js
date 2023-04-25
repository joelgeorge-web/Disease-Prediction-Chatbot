function getBotResponse(input) {
    Simple responses
    if (input == "hello" || input == "hi" || input == "hey" || input == "hola" || input == "bonjour" || input == "greetings" || input == "sup" | input == "yo" ) {
        return "Hello there!";
    } else if (input == "goodbye" || input == "bye" || input == "see you later" ) {
        return "See you next time.";
    } else {
        return "Try asking something else!";
    }
    $.getJSON('/get_response',
        function(data) {
            //do nothing
        }
    );
    return false;

}