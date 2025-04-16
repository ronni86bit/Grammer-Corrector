from flask import Flask, render_template, request
from language_tool_python import LanguageTool

app = Flask(__name__)
tool = LanguageTool('en-US')

@app.route('/')
def index():
    return render_template('index.html', corrected_text='')

@app.route('/spell', methods=['POST'])
def spell_check():
    text = request.form['text']
    errors = tool.check(text)
    corrected_text = tool.correct(text)
    return render_template('index.html', corrected_text=corrected_text)

if __name__ == '__main__':
    app.run(debug=True)
