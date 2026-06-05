import pandas as pd


def analyze_csv(df: pd.DataFrame) -> dict:

    if df.empty:
        return {
                "success": False,
                "error": "The dataset is empty"
        }

    numeric_df = df.select_dtypes(include="number")
    numeric_columns = numeric_df.columns.to_list()

    
    return {
            "success": True,
            "rows": len(df.index),
            "columns": len(df.columns),
            "numeric_columns": numeric_columns,
            "summary": get_summary(df, numeric_columns),
            "preview": df.head(7).to_dict(orient="records")
    } 


def get_summary(df: pd.DataFrame, columns: list[str])->dict[str, dict[str, int|float]]:
    """
        accepts a csv loaded by pandas as the first argument and 
        numeric columns as the second and returns a summary
    """
    summary = {}
    
    for column in columns:
        df_not_null = df[column].dropna()
        summary[column] = {
                "count": df_not_null.count(),
                "mean": round(df_not_null.mean(), 2),
                "min": df_not_null.min(),
                "max": df_not_null.max(),
                "median": df_not_null.median(),
                "number of miising data": df[column].isna().sum()
            } 
    return summary


# try:
#     df = pd.read_csv(csv_path)
# except Exception as e:
#     {
#         "success": False,
#         "error": f"error trying to read the file {e}"
#     }
