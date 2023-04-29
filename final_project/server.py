import machinetranslation
from machinetranslation.translator import englishToFrench, frenchToEnglish
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishFrench")
def englishFrench():
    textToTranslate = request.args.get('textToTranslate')
    translatedText = englishToFrench(textToTranslate)
    return translatedText

@app.route("/frenchEnglish")
def frenchEnglish():
    textToTranslate = request.args.get('textToTranslate')
    translatedText = frenchToEnglish(textToTranslate)
    return translatedText

@app.route("/")
def renderIndexPage():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

