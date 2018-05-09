from flask import Flask, render_template, url_for, jsonify
import random
import csv
import os

app = Flask(__name__)


@app.context_processor
def overrider_url_for():
    return dict(url_for=dated_url_for)


def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                     endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
        return url_for(endpoint, **values)


data_set = "C:\Users\hrutv\Desktop\Jokes\src\jokes-twitter.csv"
my_hash = {}

with open(data_set) as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        my_hash2 = {
            row[0]: {
                "author": row[6],
                "q": row[3],
                "a": row[4]
            }
        }
        my_hash.update(my_hash2)


def new_joke(jokes_file):
    num = random.randint(2, 133992)
    num = str(num)
    author = "Reddit User: " + jokes_file[num]['author']
    data = {
        'author': author,
        'q': jokes_file[num]['q'],
        'a': jokes_file[num]['a']
    }
    return jsonify(data)


@app.route('/')
def hello_method():
    return render_template('index.html')


@app.route('/reddit-Jokes')
def rand_joke():
    return new_joke(my_hash)


if __name__ == '__main__':
    app.run()
