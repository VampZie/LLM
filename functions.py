import pandas as pd

def get_upregulated_genes(species: str, stage: str, top_n: int = 5):
    df = pd.read_csv("data/expression_data.csv")
    filtered = df[(df["species"] == species) & (df["stage"] == stage)]
    up = filtered[filtered["log2_fold_change"] > 0]
    result = up.sort_values("log2_fold_change", ascending=False).head(top_n)
    return result.to_dict(orient="records")

def get_downregulated_genes(species: str, stage: str, top_n: int = 5):
    df = pd.read_csv("data/expression_data.csv")
    filtered = df[(df["species"] == species) & (df["stage"] == stage)]
    down = filtered[filtered["log2_fold_change"] < 0]
    result = down.sort_values("log2_fold_change").head(top_n)
    return result.to_dict(orient="records")
