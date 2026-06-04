import pandas as pd


def analyze_csv(csv_path: str) -> dict:
    
    df = pd.read_csv(csv_path)
    return {
        "student_count": len(df),
        "highest_score": df["Score"].max(),
        "average_score": round(df["Score"].mean(), 2)
    }
