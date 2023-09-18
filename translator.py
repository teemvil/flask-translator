from flask import Flask, render_template, request
from transformers import pipeline

app = Flask(__name__)

# initialize the translator pipeline; using pre-trained model
pipe = pipeline("translation", model="Helsinki-NLP/opus-mt-en-fi")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/translate', methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      # Extract text from the post from UI
      original_text = result['text']
      # Translate using the pipeline
      translation = pipe(original_text)
      # Extract the text from the translation result
      translation_result = translation[0]["translation_text"]
      # Create new dict to send to UI
      result_dict={original_text:translation_result}

      return render_template("result.html", result = result_dict)

if __name__ == '__main__':
    app.run(debug=True)
