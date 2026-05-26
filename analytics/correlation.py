def generate_correlation(df):
    return df.corr(numeric_only=True)