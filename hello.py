from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/')
def hello():
	#return "hello"
	user = {"username":"Rohith","age":"22"}
	user_details = open("user_details.txt","r")
	user_name = user_details.read().strip()
	user_details.close()
	return render_template('index.html',title='Home',user_name=user_name)

if __name__=="__main__":
	app.run()