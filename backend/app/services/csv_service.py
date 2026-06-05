import pandas as pd


def analyze_csv(csv_path: str) -> dict:
    try:
        df = pd.read_csv(csv_path)
    except Exception as e:
        return {
            "success": False,
            "error": f"error trying to read the file {e}"
        }

    if df.empty:
        return {
                "success": False,
                "error": "The dataset contains no rows"
        }

    numeric_df = df.select_dtypes(include="number")
    numeric_columns = numeric_df.columns.to_list()

    if not numeric_columns:
        return {
                "success": False,
                "error": "no numeric coloumns found"
        }
    
    return {
            "success": True,
            "rows": len(df.index),
            "columns": len(df.columns),
            "numeric_columns": numeric_columns,
            "summary": get_summary(df, numeric_columns),
            "preview": df.head(7).to_dict(orient="records")
    } 


def get_summary(df: pd.DataFrame, coloumns: list[str])->dict[str, int|float]:
    """
        accepts a csv loaded by pandas as the first argument and 
        numeric coloumns as the second and returns a summary
    """
    summary = {}
    
    for coloumn in coloumns:
        df_not_null = df[coloumn].dropna()
        summary[coloumn] = {
                "count": df_not_null.count(),
                "mean": round(df_not_null.mean(), 2),
                "min": df_not_null.min(),
                "max": df_not_null.max(),
                "median": df_not_null.median(),
                "number of miising data": df[coloumn].isna().sum()
            } 
    return summary