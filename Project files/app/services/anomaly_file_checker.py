import pandas as pd
from io import StringIO

def detect_anomaly_in_uploaded_csv(content: str, kpi: str, threshold: float):
    try:
        df = pd.read_csv(StringIO(content))
    except Exception as e:
        return {"error": f"Error reading CSV: {e}"}

    if kpi not in df.columns:
        return {"error": f"KPI '{kpi}' not found in file."}

    anomalies = df[df[kpi] > threshold]

    return {
        "kpi": kpi,
        "threshold": threshold,
        "anomaly_count": len(anomalies),
        "anomalies": anomalies.to_dict(orient="records")
    }