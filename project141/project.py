
import csv
from flask import jsonify, Flask,request
all_articles = []

with open("articles.csv",encoding='utf8') as f:
    reader = csv.reader(f)
    data = list(reader)
    all_articles = data[1:]

liked_articles = []
not_liked_articles = []

app = Flask(__name__)
@app.route('/')
def get_articles():
   return jsonify({all_articles[0]}) 

@app.route('/liked_articles',methods = ['POST'])
def post_articles():
  article = all_articles[0]
  liked_articles.append(article)
  all_articles.pop(0)
  return jsonify({"status":"success"}),201

@app.route('/not_liked_articles',methods = ['POST'])
def post__articles():
  article = all_articles[0]
  not_liked_articles.append(article)
  all_articles.pop(0)
  return jsonify({
        "status": "success"
    }), 201
  

if __name__ == "__main__":
    app.run(debug=True)
