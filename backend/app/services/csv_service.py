import pandas as pd


def analyze_csv(csv_path: str) -> dict:
    df = pd.read_csv(csv_path)

    if all(name != "Score" for name in df.to_dict().keys()):
        return {
                "success": False,
                "error": "Column 'Score' not found"
        }
    return {
        "success": True,
        "data": {
            "student_count": len(df),
            "highest_score": df["Score"].max(),
            "average_score": round(df["Score"].mean(), 2)
        }
    }
