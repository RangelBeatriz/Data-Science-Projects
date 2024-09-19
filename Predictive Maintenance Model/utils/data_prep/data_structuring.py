import pandas as pd
import numpy as np


def add_max_cycles_column(df, label, cycles):
    """
        Adds a column representing the maximum number of time cycles for each unit.

            Parameters
            ----------
                df : pandas.DataFrame
                    The input DataFrame containing all features.
                label : str
                    The column name representing the unit labels (e.g., machine, device, or entity).
                cycles : str
                    The column name representing the registered time cycles.

            Returns
            -------
                pandas.DataFrame
                    The DataFrame with an additional column 'max_time_cycles', which contains the maximum number of time cycles for each unit.
    """
    # Find the maximum number of cycles for each unit
    max_cycles = df[[label, cycles]].groupby(label, as_index=False).max()

    # Rename the cycles column to max_time_cycles
    max_cycles = max_cycles.rename(columns={cycles: 'max_time_cycles'})

    # Merge the original DataFrame with the max cycles per unit
    df_merged = df.merge(max_cycles, on=label, how='left')

    return df_merged


def calculate_rul_column(df, max_cycles, current_cycles):
    """
        Calculates the Remaining Useful Life (RUL) of an asset based on the maximum and current cycle counts.

            Parameters
            ----------
                df : pandas.DataFrame
                    The input DataFrame containing asset data.
                max_cycles : str
                    The column name that stores the maximum number of cycles an asset can undergo.
                current_cycles : str
                    The column name that stores the current cycle count of the asset.

            Returns
            -------
                pandas.DataFrame
                    The input DataFrame with an additional column 'rul', representing the Remaining Useful Life of each asset.
    """
    df['rul'] = df[max_cycles] - df[current_cycles]

    return df