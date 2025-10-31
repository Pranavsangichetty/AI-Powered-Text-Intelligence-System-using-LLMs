import streamlit as st
import sqlite3
import pandas as pd
from sql_generator import generate_sql_query
from text_classifier import classify_text
from preprocess import clean_text

st.set_page_config(page_title="AI-Powered Text Intelligence System", layout="wide")

st.title("AI-Powered Text Intelligence System using LLMs")
st.markdown("### Combine Natural Language to SQL Generation & Text Classification")

# Tabs for functionality
tab1, tab2 = st.tabs(["Text Classification", "Natural Language to SQL"])

# Database setup
conn = sqlite3.connect("database.db")
cur = conn.cursor()

# Create dummy table if not exists
cur.execute("""
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY,
    name TEXT,
    department TEXT,
    salary INTEGER
)
""")
conn.commit()

# --- TAB 1: Text Classification ---
with tab1:
    st.subheader("Text Classification")
    user_text = st.text_area("Enter text to analyze", placeholder="Type here...")

    if st.button("Classify Text"):
        if user_text.strip():
            cleaned = clean_text(user_text)
            result = classify_text(cleaned)
            st.success(f"Prediction: **{result['label']}** (Confidence: {result['confidence']})")
        else:
            st.warning("Please enter text before classification.")

# --- TAB 2: Natural Language to SQL ---
with tab2:
    st.subheader("NL → SQL Conversion & Execution")

    nl_query = st.text_input("Ask your database in plain English", placeholder="e.g., Show me employees in IT department")

    if st.button("Generate SQL"):
        if nl_query.strip():
            sql = generate_sql_query(nl_query)
            st.code(sql, language="sql")

            try:
                data = pd.read_sql_query(sql, conn)
                st.dataframe(data)
            except Exception as e:
                st.error(f"Error executing SQL: {e}")
        else:
            st.warning("Please enter a natural language query.")
