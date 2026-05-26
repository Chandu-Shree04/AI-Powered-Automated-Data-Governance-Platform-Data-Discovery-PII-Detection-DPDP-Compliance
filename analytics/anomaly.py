from sklearn.ensemble import IsolationForest

def detect_anomalies(df, column):

    model = IsolationForest(contamination=0.05)

    df['anomaly'] = model.fit_predict(df[[column]])

    return df
