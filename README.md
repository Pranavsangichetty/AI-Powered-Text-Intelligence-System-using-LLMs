# 🤖 AI-Powered Text Intelligence System using LLMs

An interactive **Streamlit** application combining Natural Language to SQL (NL2SQL) with text classification. Ask questions about a SQLite database in plain English, inspect the generated SQL, view query results, and classify text using a pre-trained transformer model.

## 🚀 Live Demo

👉 **[Launch the AI-Powered Text Intelligence System](https://ai-powered-text-intelligence-system-using-llms-4yzrmeyj2zrp2fg.streamlit.app/)**

## ✨ Features

- **Natural Language to SQL:** Generates SQL from plain-English prompts using the `defog/sqlcoder-7b-2` model.

- **SQL execution and results:** Attempts to execute the generated query against a SQLite database and displays the results.

- **Text classification:** Uses a pre-trained DistilBERT sentiment-classification model to return a label and confidence score.

- **Interactive interface:** Offers separate tabs for text classification and natural-language database queries.

- **Modular Python code:** Separates the Streamlit interface, SQL generation, text classification, preprocessing, and data/database logic.

> **Model note:** The current text-classification model is fine-tuned for sentiment analysis. It should not be treated as a validated malicious-content, spam, or cybersecurity-risk detector without selecting and evaluating a model for those purposes. Generated SQL may be inaccurate; review it before execution, especially with non-demo data.

## 🧰 Tech Stack

| Component | Technology |
|---|---|
| User interface | Streamlit |
| Programming language | Python |
| Natural-language-to-SQL model | `defog/sqlcoder-7b-2` (Transformers) |
| Text classification | `distilbert-base-uncased-finetuned-sst-2-english` |
| Database | SQLite |
| Data display | Pandas |

## 🗂️ Project Structure

```text
.
├── app.py             # Streamlit interface
├── sql_generator.py   # Natural-language-to-SQL generation
├── text_classifier.py # Text classification pipeline
├── preprocess.py      # Text preprocessing
├── data.py            # Data utilities
├── database.db        # SQLite database
├── requirement.txt    # Original dependency file
├── requirements.txt   # Deployment dependency file
└── README.md
```

## ⚙️ Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/Pranavsangichetty/AI-Powered-Text-Intelligence-System-using-LLMs.git
cd AI-Powered-Text-Intelligence-System-using-LLMs
```

### 2. Create and activate a virtual environment (recommended)

**Windows PowerShell**

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

**macOS / Linux**

```bash
python -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Start the application

```bash
python -m streamlit run app.py
```

Streamlit will print a local address, usually `http://localhost:8501`.

## 🧭 How to Use

### Text Classification

1. Open the **Text Classification** tab.

2. Enter the text you want to analyze.

3. Select **Classify Text**.

4. Review the predicted sentiment label and confidence score.

### Natural Language to SQL

1. Open the **Natural Language to SQL** tab.

2. Enter a question in plain English.

3. Select **Generate SQL**.

4. Review the generated SQL and displayed query results.

**Safety note:** Generated SQL can be incorrect or incompatible with the database schema. Inspect it before use. Do not use this demo with sensitive or production data without adding appropriate safeguards, including read-only query validation.

## 🔭 Potential Improvements

- Validate generated SQL and restrict execution to read-only statements.

- Load the language model once rather than reloading it for every request.

- Improve error handling for model downloads, inference, and database operations.

- Evaluate the text classifier and use a model aligned with the intended labels.

- Add automated tests and pin compatible dependency versions.

## 👤 Author

**Pranav Sangichetty**

- **Email:** [sangichettypranav@gmail.com](mailto:sangichettypranav@gmail.com)

- **LinkedIn:** [Pranav Sangichetty](https://www.linkedin.com/in/pranav-sangichetty/)

- **GitHub:** [Pranavsangichetty](https://github.com/Pranavsangichetty)

- **Portfolio:** [Visit portfolio](https://portfolio-pranav-lilac.vercel.app/)

---

Please review the repository and relevant model licenses before redistributing or deploying modified versions.
