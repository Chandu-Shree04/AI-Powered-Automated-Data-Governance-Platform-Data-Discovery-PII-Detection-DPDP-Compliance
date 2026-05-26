import re

def classify_column(col_name, sample_values):

    col = col_name.lower()

    if "email" in col:
        return "PII"

    if "salary" in col:
        return "Sensitive Financial"

    if "phone" in col:
        return "PII"

    for value in sample_values:

        value = str(value)

        if re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', value):
            return "Email"

        if re.match(r'^\+?\d{10,13}$', value):
            return "Phone"

    return "General Data"

def classify_dataset(df):

    results = {}

    for col in df.columns:

        sample = df[col].dropna().head(20)

        results[col] = classify_column(
            col,
            sample
        )

    return results
