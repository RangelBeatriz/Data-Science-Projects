import pandas as pd
import numpy as np



def columns_with_null(df):
    """
        Identifies columns in the DataFrame that contain null values.

            Parameters
            ----------
            df : pandas.DataFrame
                The input DataFrame to check for null values.

            Returns
            -------
            list
                A list of column names that contain null values.
    """
    # Get the sum of null values for each column
    null_counts = df.isnull().sum()

    # Return list of columns where null count is greater than 0
    return null_counts[null_counts > 0].index.tolist()