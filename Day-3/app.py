from flask import Flask, render_template, request
from nltk.chat.util import Chat, reflections

qn1 = r'how are you'  # raw string (more f-string, b-string...)
ans1 = [
    'all well',
    'I am good',    
    'awesome' 
]

qn2 = r'(.*)what (.*)do(.*)'
ans2 = [    
    'I can reply to your queries',    
    'I am here to answer your questions',    
    'I can chat with you'
]

qn3 = r'(.*)your name'
ans3 = [    
    'my name is chatty',    
    'I am chatty'
]

qn4 = r'(.*)mausam(.*)ba[a]*rish'  # aaj mausam kaisa hai, kya baarish hogi?
ans4 = [    
    'it looks it will rain today',    
    'baarish ka mausam hai',  
    'baarish ho sakti hai mausam kharab hai'
]

# Pairing qns with ans 
qa_pair = [
    (qn1, ans1),
    (qn2, ans2),
    (qn3, ans3),
    (qn4, ans4),
]
chatbot = Chat(qa_pair)

app = Flask(__name__)

@app.route('/')

def home():
    global chatbot
    query = request.args.get('Query')
    # print(query)
    if query!=None:
        response = chatbot.respond(query) # respond with stored 
        if response == None:
            response = 'Sorry, I am not sure'
    else:
        response = ''

    # response = 'Response of Abhinandan Singh'
    # return "Hi! This is comming from Abhinandan Singh"
    return render_template('index.html', result=response)

@app.route('/chatbot')

def chat():
    return "<h2>Chat Bot</h2>"

app.run(debug=True) # debug = true : don't need to restart server... work after save


