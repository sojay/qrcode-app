import awsgi
from flask import Flask, render_template, request
from qr import make_qr

app = Flask('app', template_folder='templates')

@app.route('/', methods = ['GET', 'POST'])
def hello_world():
  return render_template("index.html")

@app.route('/about', methods = ['GET', 'POST'])
def about():
  return render_template("about.html")

@app.route('/form', methods = ['GET', 'POST'])
def form_function():
    if request.method == 'POST':
        data = request.form
        url = data["entryurl"]
        make_qr(url)

        return render_template("qrpage.html")
    
def lambda_handler(event, context):
    return awsgi.response(app, event, context, base64_content_types={"image/png"})

        
app.run(host='0.0.0.0', port=5001)
