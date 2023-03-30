from flask import Flask, render_template

app = Flask(
  __name__,
  template_folder='templates',
  static_folder='static'
)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/1')
def page_1():
	return render_template('test1.html')

@app.route('/2')
def page_2():
	return render_template('test2.html')

@app.route('/3')
def page_3():
	return render_template('test3.html')

@app.route('/4')
def survey():
	return render_template('survey.html')

@app.route('/5')
def results():
	return render_template('results.html')

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)


