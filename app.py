from flask import Flask, request, jsonify, render_template
# 
# creates a Flask application with name "app"
app = Flask(__name__)

# a route to display our html page called "index.html" gotten from [react-chat-widget](https://github.com/mrbot-ai/rasa-webchat)
@app.route("/")
def index():  
    return render_template('index.html')

@app.route('/get_response')
def background_process_test():
    print ("Hello")
    return ("nothing")

# run the application
if __name__ == "__main__":  
    app.run(debug=True)

