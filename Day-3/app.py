from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')

def home():

    query = request.args.get('Query')
    # print(query)
    if query!=None:
        response = 'We got query'
    else:
        response = ''

    # response = 'Response of Abhinandan Singh'
    # return "Hi! This is comming from Abhinandan Singh"
    return render_template('index.html', result=response)

@app.route('/chatbot')

def chat():
    return "<h2>Chat Bot</h2>"

app.run(debug=True) # debug = true : don't need to restart server... work after save


