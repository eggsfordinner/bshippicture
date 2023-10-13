from flask import Flask, render_template, request, jsonify, make_response
import time
from uuid import uuid4
import json

app = Flask(__name__, template_folder='static')

# Initialize a global string
global answers
answers = {}

def update_global_string():
    global global_string
    while True:
        # Update the global string every second
        global_string = "Updated value: " + str(time.time())
        time.sleep(1)

# Start a separate thread to update the global string
from threading import Thread
update_thread = Thread(target=update_global_string)
update_thread.daemon = True
update_thread.start()

@app.route('/')
def home():
    global answers
    
    session_id = request.cookies.get('session_id')
    if not session_id or session_id == None:
        session_id = str(uuid4())
        response = make_response(render_template('index.html'))
        response.set_cookie('session_id', session_id)
        print(session_id)
        answers[session_id] = {'text': "", 'finished': False}
        return response
    print(session_id)
    answers[session_id] = {'text': "", 'finished': False}
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    user_input = request.form['user_input']
    session_id = request.cookies.get('session_id')
    print(session_id)
    global answers
    answers[session_id] = "Processing request: " + session_id
    print(session_id)
    # Perform some processing on the user input (you can replace this with your own logic)
    processed_output = user_input.upper()
    return jsonify({'processed_output': "text"})
    #return render_template('index.html', user_input=user_input, processed_output=processed_output)

@app.route('/get_global_string', methods=['GET'])
def get_global_string():
    global answers
    text = ""
    session_id = request.cookies.get('session_id')
    if session_id in answers.keys():
    	text = answers[session_id]['text']
    return jsonify({'global_string': text})

@app.route('/set_global_string', methods=['POST'])
def set_global_string():
    session_id = request.json['session_id']
    text = request.json['text']
    finished = request.json['finished']
    
    global answers
    answers[session_id] = {'text': text, 'finished': finished}
    
    return jsonify({'message': 'Global string updated'})

if __name__ == '__main__':
    app.run(debug=True)
