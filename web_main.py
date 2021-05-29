from flask import request
from flask import Flask, render_template
import Search
import sys


app = Flask(__name__)

@app.route('/')
def main_page():
    return render_template('search.html')

@app.route('/s')
def search():
    query = request.args.get('wd')
    if query:
        result = Search.run(query)
        return render_template('/result.html', text=result[0], data=result[1], num=result[2])
    if not query:
        return render_template('search.html')
        
if __name__ == '__main__':
    app.run(debug=False,port=8080)