import requests
import pandas as pd

def load_api(url):
    response = requests.get(url)
    data = response.json()
    return pd.DataFrame(data)
