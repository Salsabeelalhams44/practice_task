import  requests
import json
from flask import Flask, render_template
import jinja2

app = Flask(__name__)
@app.route ("/student_template.html")

def home():
    result = requests.get('http://staging.bldt.ca/api/method/build_it.test.get_students')
    data = result.text
    data = json.loads(data)
    print(data['status'])
    context ={}
    context['title'] = 'Salsabeel'
    context['data'] = data['data']
    print(data['data'])
    return render_template('student_template.html',**context)
    # return context
    # return  "Hello"
app.run(debug=True)