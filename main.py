
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/details/<id>')
def details(id):
  return render_template('detail.html', id=id)

@app.route('/form', methods=['GET', 'POST'])
def form():
  if request.method == 'POST':
    return redirect(url_for('success'))
  return render_template('form.html')

@app.route('/success')
def success():
  return render_template('success.html')

if __name__ == '__main__':
  app.run(debug=True)
