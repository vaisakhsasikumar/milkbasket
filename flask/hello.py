from flask import Flask, render_template, request
app = Flask(__name__)
import csv
import sys

@app.route('/hello/')
def hello():
	return render_template('form.html')

@app.route('/hello/hi/',methods = ['POST'])
def hello_name():
	if request.method == 'POST':
		number = request.form['name']
		user = request.form['name']
	else:
		number = request.args.get('name')
	#input number you want to search
	#number = user
	try:
		ifile  = open('C:\\Users\\far\\Downloads\\medium-master\\medium-master\\items-recommender\\output\\option1_recommendation.csv', "r")
		read = csv.reader(ifile)
		for row in read :
			if number == row[0]:
				result = row
		products = (result[1].split('|'))
		return render_template('test.html', name = products, user= user)
	except:
		return render_template('error.html')
		        

if __name__ == '__main__':
   app.run(host= '0.0.0.0')