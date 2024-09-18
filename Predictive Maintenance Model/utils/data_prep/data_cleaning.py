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


def feature_selection(df, threshold=1, keep_features=None):
    """
        Selects relevant features from a DataFrame by removing columns that have unique value counts 
        less than or equal to a specified threshold, while keeping specified columns intact.

            Parameters
            ----------
            df : pandas.DataFrame
                The input DataFrame to filter.
            threshold : int, optional
                The minimum number of unique values a column must have to be retained. 
                Columns with fewer unique values than the threshold will be dropped.
                Default is 1.
            keep_features : list of str, optional
                A list of column names that should not be dropped, regardless of their unique value count.
                Default is None, which means no specific columns are preserved.

            Returns
            -------
            pandas.DataFrame
                A DataFrame containing the selected features based on the threshold and the specified keep_features.

    """
    
    # Creates an empty list if keep_features is None
    if keep_features is None:
        keep_features = []

    # Preserve columns in keep_features by creating a filtered DataFrame
    selected_df = df[keep_features].copy()

    unique_values = df.nunique()

    # Filter out features based on the threshold, excluding any already in keep_features
    features_to_keep = unique_values[unique_values > threshold].index.difference(keep_features)

    # Concatenate selected_df with the features that meet the threshold
    selected_df = pd.concat([selected_df, df[features_to_keep]], axis=1)

    return selected_df