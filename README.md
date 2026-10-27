🤖 AI-Powered Text Intelligence System using LLMs

An interactive Streamlit application that combines Natural Language to SQL (NL2SQL) with text classification. Ask questions about a SQLite database in plain English, inspect the generated SQL, view query results, and classify text with a pre-trained transformer model.

🚀 Live Demo
🔗 Open the Streamlit App

Replace the placeholder above with the app's actual Streamlit Community Cloud URL. I could not verify a public deployment URL from the repository.

✨ Features

- Natural Language to SQL: Generates SQL from plain-English prompts using the defog/sqlcoder-7b-2 model.

- SQL execution and results: Attempts to execute generated SQL against a SQLite database and displays the results in the app.

- Text classification: Uses a pre-trained DistilBERT sentiment-classification model to return a label and confidence score.

- Interactive interface: Offers separate tabs for text classification and natural-language database queries.

- Modular Python code: Separates the Streamlit interface, SQL generation, text classification, preprocessing, and data/database logic.

Model note: The current text-classification model is fine-tuned for sentiment analysis. It should not be presented as a validated malicious-content, spam, or cybersecurity-risk detector without changing and evaluating the model. Review generated SQL before execution, particularly when using non-demo data.

🧰 Tech Stack

Component	Technology

Interface	Streamlit

Language	Python

Natural-language-to-SQL model	defog/sqlcoder-7b-2 (Transformers)

Text classification	distilbert-base-uncased-finetuned-sst-2-english

Database	SQLite

Data display	Pandas

🗂️ Project Structure
.
├── app.py             # Streamlit interface
├── sql_generator.py   # Natural-language-to-SQL generation
├── text_classifier.py # Text classification pipeline
├── preprocess.py      # Text preprocessing
├── data.py            # Data utilities
├── database.db        # SQLite database
├── requirement.txt    # Python dependencies
└── README.md

⚙️ Run Locally

1. Clone the repository
git clone https://github.com/Pranavsangichetty/AI-Powered-Text-Intelligence-System-using-LLMs.git
cd AI-Powered-Text-Intelligence-System-using-LLMs

2. Create a virtual environment (recommended)
Windows PowerShell
python -m venv .venv
.venv\Scripts\Activate.ps1
macOS / Linux
python -m venv .venv
source .venv/bin/activate

3. Install dependencies
The repository's dependency file is named requirement.txt (singular):
pip install -r requirement.txt
Install compatible versions of PyTorch and Transformers for your operating system if needed.

4. Run the app
streamlit run app.py
Streamlit will show a local URL in the terminal, usually http://localhost:8501.

🧭 How It Works

Text classification

1. Open the Text Classification tab.

2. Enter text to analyze.

3. Select Classify Text.

4. Review the predicted sentiment label and confidence score.

Natural Language to SQL

1. Open the Natural Language to SQL tab.

2. Enter a question in plain English.

3. Select Generate SQL.

4. Review the generated SQL and the displayed query results.

Generated SQL may be inaccurate or incompatible with the database schema. Inspect it before use; this demo should not be used with sensitive or production data without additional safeguards.

🔭 Potential Improvements

- Validate generated SQL and restrict execution to read-only statements.

- Load the language model once rather than reloading it for each request.

- Add robust handling for model downloads, inference, and database errors.

- Evaluate the text classifier and choose a model aligned with the intended labels.

- Add tests and pin compatible dependency versions.

👤 Author

Pranav Sangichetty

- Email: sangichettypranav@gmail.com

- LinkedIn: Pranav Sangichetty

- GitHub: Pranavsangichetty

- Portfolio: pranav-lilac.vercel.app

If you use or adapt this project, review the repository's license and the relevant model licenses before redistribution.
