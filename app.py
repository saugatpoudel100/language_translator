from flask import Flask, render_template, request
from transformers import M2M100ForConditionalGeneration, M2M100Tokenizer

app = Flask(__name__)

model_name = "facebook/m2m100_418M"
tokenizer = M2M100Tokenizer.from_pretrained(model_name)
model = M2M100ForConditionalGeneration.from_pretrained(model_name)

@app.route('/', methods=['GET', 'POST'])
def index():
    translated_text = ''
    if request.method == 'POST':
        input_text = request.form['input_text']
        source_lang = request.form['source_lang']
        target_lang = request.form['target_lang']

        tokenizer.src_lang = source_lang
        encoded = tokenizer(input_text, return_tensors="pt")
        generated_tokens = model.generate(**encoded, forced_bos_token_id=tokenizer.get_lang_id(target_lang))
        translated_text = tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)[0]

    return render_template('index.html', translated_text=translated_text)

if __name__ == '__main__':
    app.run(debug=True)
