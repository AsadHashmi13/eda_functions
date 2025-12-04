import pandas as pd

def detailed_value_counts(df,col):

    counts = df[col].value_counts()
    proportions = df[col].value_counts(normalize=True).mul(100)
    results_df = pd.DataFrame({'Count': counts, 'Proportion': proportions})
    results_df.reset_index(inplace=True)
    return results_df