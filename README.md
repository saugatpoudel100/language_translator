# 🌍 Language Translator Web App

A simple and responsive **language translation web application** built using **Flask** (Python backend), **Tailwind CSS** (frontend), and **Facebook AI's M2M100 multilingual model** via Hugging Face. The app allows users to translate text between various languages using an open-source transformer model.

---

## 📁 Project Structure

```bash
language_translator/
├── app.py                  # Main Flask backend application
├── templates/
│   └── index.html          # Frontend page using Tailwind CSS
├── static/
│   └── styles.css          # (Optional) Extra Tailwind styles if needed
├── requirements.txt        # Python dependencies
└── README.md               # This project documentation

```markdown
 🚀 Features
Translate between 100+ languages using M2M100

Fast, responsive UI with Tailwind CSS

Easy to extend and modify

No need for English as a pivot language

Fully open source and local (no third-party translation APIs)

⚙️ Technologies Used
Python 3.7+

Flask – Lightweight Python web framework

Hugging Face Transformers – NLP models and tokenizer

Tailwind CSS – Modern utility-first CSS framework

Facebook M2M100 Model – Multilingual transformer model

🔧 Setup Instructions
✅ 1. Clone the Repository
git clone https://github.com/saugatpoudel10/language_translator.git
cd language_translator
✅ 2. Create a Virtual Environment (Optional but Recommended)
python -m venv venv
# Activate on Windows
venv\Scripts\activate
# Activate on Linux/macOS
source venv/bin/activate
✅ 3. Install Dependencies
pip install -r requirements.txt
📦 requirements.txt
txt
Copy code
Flask==2.3.2
transformers==4.41.1
torch
sentencepiece
You can install them manually with:
pip install Flask transformers torch sentencepiece
▶️ Run the App
python app.py
Open your browser and visit: http://127.0.0.1:5000/

🌐 Supported Languages
Use ISO language codes in the dropdown (e.g., en, fr, hi, es).
Supported examples:

English (en)

French (fr)

Hindi (hi)

Spanish (es)

German (de)

Arabic (ar)

Chinese (zh)

... and many more.

📄 Full list: facebook/m2m100_418M

⚠️ Notes
The first time you run the app, the model (~1.94 GB) will be downloaded automatically.

On Windows, you might see a symlink warning. It's safe to ignore it.

For faster downloads, install:
pip install huggingface_hub[hf_xet]
💡 Future Improvements
Auto language detection using langdetect

Add text-to-speech for output

Add voice input (speech-to-text)

User session history of translations

Dockerize and deploy to Heroku/Render

🧠 Credits
Facebook AI Research – M2M100 Model

Hugging Face Transformers

Flask Web Framework

Tailwind CSS

📜 License
This project is open source and available under the MIT License.






