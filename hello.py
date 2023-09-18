from flask import Flask, render_template, request
from transformers import pipeline

app = Flask(__name__)

pipe = pipeline("translation", model="Helsinki-NLP/opus-mt-en-fi")

src = "en"
trg = "fi"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/translate', methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      print(result['text'])
      original_text = result['text']
      translation = pipe(original_text)
      print(translation[0]["translation_text"])
      translation_result = translation[0]["translation_text"]
      result_dict={original_text:translation_result}

      return render_template("result.html", result = result_dict)

if __name__ == '__main__':
    app.run(debug=True)
