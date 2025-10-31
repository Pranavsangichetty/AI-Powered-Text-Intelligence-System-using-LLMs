🤖 AI-Powered Text Intelligence System using LLMs
📘 Project Overview

This project presents a unified AI system that combines Natural Language to SQL (NL2SQL) generation and text classification using Large Language Models (LLMs).
The system is designed to interpret natural language queries, generate corresponding SQL commands, and analyze or classify textual data for risk or malicious activity detection.

It provides an interactive interface for seamless user interaction and a backend that executes queries and classifications efficiently, making it ideal for data analysts, cybersecurity researchers, and AI-driven business intelligence applications.

🧩 Core Modules
1. 🧠 Natural Language to SQL

Converts user input in natural language (e.g., “Show me all users with high transaction value”) into valid SQL queries.

Executes queries on the connected database and displays results.

2. 🔍 Text Classification

Classifies textual data (e.g., documents, messages, or logs) into predefined categories.

Detects potential malicious, spam, or risky content using transformer-based models.

3. 💻 Streamlit Interface

Simple and interactive web-based UI built using Streamlit.

Allows users to input queries, view SQL results, and analyze text classification outputs in real time.

4. 🗄️ Database Integration

Uses SQLite as a lightweight backend for executing SQL queries.

Can be extended to connect with MySQL, PostgreSQL, or other databases.

⚙️ Tech Stack

Frontend: Streamlit
Backend: Python
LLM Model: Transformer-based models (e.g., Gemini, GPT, or similar LLMs)
Database: SQLite
Libraries: Transformers, LangChain, SQLAlchemy, Pandas

🚀 Features

✅ Converts natural language queries into SQL commands
✅ Executes and displays query results directly in the interface
✅ Detects and classifies malicious or risky text content
✅ Interactive and user-friendly web UI
✅ Modular structure for easy scalability and customization

🛠️ Environment Setup
🧩 Prerequisites

Ensure you have:

Python 3.8 or above

pip (Python package manager)

⚙️ Install Dependencies

Run the following command in your terminal:
pip install streamlit transformers pandas sqlalchemy langchain

▶️ Run the Application

Start the Streamlit app by running:
streamlit run app.py

This will open the interactive dashboard in your default browser.

🧠 System Workflow

User Input:
The user enters a natural language query or text for classification.

Processing:
The system uses an LLM to:

Convert NL queries into SQL statements, or

Analyze text and classify its intent or threat level.

Execution & Output:

SQL queries are executed on the database, and results are shown.

Text classification results are displayed with confidence scores.

📈 Future Enhancements

Integrate advanced LLMs like GPT-4 or Gemini Pro for improved accuracy.

Add voice-based query support.

Implement a multi-database selection feature.

Deploy as a full-stack web app using Flask/Django + Streamlit.

Include API endpoints for programmatic access.

💬 Feedback & Support

For questions or feedback, contact:
📧 sangichettypranav@gmail.com

🏁 License

This project is released under the MIT License.
You are free to use, modify, and distribute it for research or educational purposes.
