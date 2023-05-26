from model import predictDisease
import re
from flask import Flask, request, jsonify, render_template
import webbrowser
import threading

app = Flask(__name__)

@app.route("/")
def index():  
    return render_template('index.html')

@app.route('/chat_response',methods=['GET','POST'])
def python_logic2():
    if(request.method == 'POST'):
        try:
            sym1 = request.form.get("data")
            sym1 = re.split(r'[,]', sym1)
            sym2 = []
            for i in sym1:
                i.title()
                sym2.append(i.title())
            print(sym2)
            
            a = ",".join(sym2)
            
            a = a.replace(", ", ",")
            result = predictDisease(a)
            print(result["Disease"])
            print(result["Description"])
            print(result["Precaution"])
            return jsonify({'aisease': result['Disease'], 'description': result['Description'], 'precaution': result['Precaution']})
        except:
            return jsonify({'disease':'Disease not found!'})
    else:
        return jsonify({})
    



def open_browser():
    webbrowser.open_new('http://127.0.0.1:5000/')

if __name__ == '__main__':
    threading.Timer(1.25, open_browser).start()
    app.run(host='0.0.0.0',port = 5000)
