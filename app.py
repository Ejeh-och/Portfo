from flask import Flask, render_template, redirect, request
from easygui import msgbox
import csv

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')


def write_to_file(data):
    with open('database.txt', encoding='UTF-8', mode='a') as database:
        name = data['name']
        email = data['email']
        filename = database.write(f'\n{name}, {email}')
    return filename


def write_to_csv(data):
    with open('database.csv', encoding='UTF-8', mode='a', newline='') as database2:
        name = data['name']
        email = data['email']
        csv_writer = csv.writer(database2, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([name, email])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_file(data)
            write_to_csv(data)
            msgbox('Submitted Successfully!', title='Thanks')
            return redirect('/')
        except:
            return 'Did not save to data base'
    else:
        return 'Something Went Wrong. Try again!'
