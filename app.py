# from flask import Flask, request, jsonify, render_template
from model import predictDisease

# app = Flask(__name__)


# @app.route("/")
# def index():  
#     return render_template('index.html')

# @app.route('/get_response')
# def background_process_test():
#     symptoms = request.args.get('symptoms')
#     result = predictDisease(symptoms)
#     return jsonify(result)


# # run the application
# if __name__ == "__main__":  
#     app.run(debug=True)
from flask import Flask, request, jsonify, render_template
# 
# creates a Flask application with name "app"
app = Flask(__name__)

# a route to display our html page called "index.html" gotten from [react-chat-widget](https://github.com/mrbot-ai/rasa-webchat)
@app.route("/")
def index():  
    return render_template('index.html')

# @app.route('/',methods=["POST"])
# def python_logic(request):
#     data = request.get_json()
#     arg1 = data["arg1"]
#     result = predictDisease(arg1)
#     return jsonify(result)
@app.route('/chat_response',methods=['GET','POST'])
def python_logic2():
    if(request.method == 'POST'):
        # data = request.get_json()
        # arg1 = data["arg1"]
        # result = predictDisease(arg1)
        print(request.json['data'])
        # q = {"What are the symptoms: "}
        return jsonify({"res":"some"})
    else:
        return jsonify({})
    

# run the application
if __name__ == "__main__":  
    app.run(debug=True)
