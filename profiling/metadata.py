def extract_metadata(df):

    metadata = {}

    for col in df.columns:
        metadata[col] = {
            "dtype": str(df[col].dtype),
            "unique_values": int(df[col].nunique()),
            "null_values": int(df[col].isnull().sum())
        }

    return metadata
