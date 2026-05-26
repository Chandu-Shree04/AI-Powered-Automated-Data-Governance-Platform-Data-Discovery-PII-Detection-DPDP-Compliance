import streamlit as st
import pandas as pd

from ingestion.csv_loader import load_csv
from profiling.profiler import generate_profile
from profiling.metadata import extract_metadata

from analytics.correlation import generate_correlation
from analytics.anomaly import detect_anomalies
from analytics.visualization import plot_histogram
from classification.classifier import classify_dataset
from ai.llm_query import ask_llm
from ai.summarizer import summarize_profile

from catalog.catalog_manager import (
    initialize_catalog,
    store_metadata
)

st.set_page_config(page_title="AI Data Discovery Platform")

st.title("AI-Powered Automated Data Discovery")

initialize_catalog()

uploaded_file = st.file_uploader(
    "Upload CSV File",
    type=["csv"]
)

if uploaded_file:

    df = load_csv(uploaded_file)

    st.subheader("Dataset Preview")
    st.dataframe(df.head())

    profile = generate_profile(df)

    metadata = extract_metadata(df)

    store_metadata(metadata)

    st.subheader("Dataset Summary")

    st.write(summarize_profile(profile))

    st.subheader("Metadata")

    st.json(metadata)

    st.subheader("Correlation Matrix")

    corr = generate_correlation(df)

    st.dataframe(corr)

    numeric_cols = df.select_dtypes(include='number').columns

    if len(numeric_cols) > 0:

        selected_column = st.selectbox(
            "Select Column",
            numeric_cols
        )

        plot_histogram(df, selected_column)

        anomaly_df = detect_anomalies(
            df,
            selected_column
        )

        st.subheader("Anomaly Detection")

        st.dataframe(
            anomaly_df[
                anomaly_df['anomaly'] == -1
            ]
        )

    classification = classify_dataset(df)
    st.subheader("Data Classification")
    st.json(classification)
    st.subheader("Ask AI About Dataset")

    question = st.text_input(
        "Ask your question"
    )

    if question:

        response = ask_llm(
            question,
            metadata
        )

        st.write(response)