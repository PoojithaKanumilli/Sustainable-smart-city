import pandas as pd
from sklearn.linear_model import LinearRegression
from io import StringIO

def forecast_from_uploaded_csv(content: str, kpi: str) -> dict:
    df = pd.read_csv(StringIO(content))

    if 'year' not in df.columns or kpi not in df.columns:
        return {"error": "Missing 'year' or KPI column in uploaded CSV."}

    model = LinearRegression()
    model.fit(df[['year']], df[[kpi]])

    next_year = df['year'].max() + 1
    prediction = model.predict(pd.DataFrame([[next_year]], columns=['year']))

    return {
        "predicted_year": int(next_year),
        "kpi": str(kpi),
        "predicted_value": float(round(prediction[0][0], 2))
    }