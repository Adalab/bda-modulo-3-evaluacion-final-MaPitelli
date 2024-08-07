import pandas as pd
import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns
from itertools import combinations
from scipy.stats import kstest, spearmanr, pearsonr


def identify_linearity(dataframe, column_combinations_list):
        """
        Identifies if the relationships between pairs of variables in a DataFrame are linear or not.

        Parameters:
        -----------
        dataframe : pandas.DataFrame
            The DataFrame containing the variables to be analyzed.

        column_combinations_list : list of tuples
            A list of tuples where each tuple contains two column names from the DataFrame to be analyzed.

        Returns:
        --------
        linear_relationships : list of tuples
            A list of tuples containing the names of the columns that have a linear relationship.

        non_linear_relationships : list of tuples
            A list of tuples containing the names of the columns that do not have a linear relationship.
        """
        linear_relationships = []
        non_linear_relationships = []

        for pair in column_combinations_list: 
            # Perform the normality test
            _, p_value1 = kstest(dataframe[pair[0]], "norm")
            _, p_value2 = kstest(dataframe[pair[1]], "norm")

            if p_value1 > 0.05 and p_value2 > 0.05:
                linear_relationships.append(pair)
            else:
                non_linear_relationships.append(pair)

        return linear_relationships, non_linear_relationships


def identify_correlations(dataframe):
    """
    Identifies correlations among numeric columns in the dataframe using Pearson or Spearman methods.

    Parameters:
    -----------
    dataframe : pandas.DataFrame
        The DataFrame containing the variables to analyze.

    Returns:
    --------
    results : dict
        A dictionary containing the correlation DataFrames. The keys are 'pearson' and 'spearman'.
        If all relationships are either linear or non-linear, only one key will be present.
    """
    # Select numeric columns
    numerics = dataframe.select_dtypes(include=np.number).columns
    
    # Generate all possible combinations of numeric columns
    num_combinations = list(combinations(numerics, 2))
    
    # Identify if the relationships are linear or non-linear
    linear, non_linear = identify_linearity(dataframe, num_combinations)
    
    # Initialize the results dictionary
    results = {}

    if linear:
        # Apply Pearson correlation for linear relationships
        linear_columns = set([item for sublist in linear for item in sublist])
        df_pearson = dataframe[list(linear_columns)].corr(method="pearson")
        results['pearson'] = df_pearson

    if non_linear:
        # Apply Spearman correlation for non-linear relationships
        non_linear_columns = set([item for sublist in non_linear for item in sublist])
        df_spearman = dataframe[list(non_linear_columns)].corr(method="spearman")
        results['spearman'] = df_spearman
    
    return results


def classify_correlations(correlation_df):
    """
    Classify the correlations in the given DataFrame into weak, moderate, and strong correlations.
    
    Parameters:
    -----------
    correlation_df : pandas.DataFrame
        DataFrame containing the correlation values between pairs of variables.
    
    Returns:
    --------
    None
    """
    weak_correlations = []
    moderate_correlations = []
    strong_correlations = []

    # To avoid duplicates, use a set to register processed pairs
    processed_pairs = set()

    for row in correlation_df.index:
        for col in correlation_df.columns:
            if row != col and (col, row) not in processed_pairs:
                corr_value = correlation_df.at[row, col]
                processed_pairs.add((row, col))
                processed_pairs.add((col, row))

                if 0.1 <= abs(corr_value) < 0.3:
                    weak_correlations.append((row, col, corr_value))
                elif 0.3 <= abs(corr_value) < 0.7:
                    moderate_correlations.append((row, col, corr_value))
                elif abs(corr_value) >= 0.7:
                    strong_correlations.append((row, col, corr_value))

    # Print the results
    print("Weak Correlations:")
    for item in weak_correlations:
        print(f"Between {item[0]} and {item[1]}: {item[2]:.2f}")

    print("\nModerate Correlations:")
    for item in moderate_correlations:
        print(f"Between {item[0]} and {item[1]}: {item[2]:.2f}")

    print("\nStrong Correlations:")
    for item in strong_correlations:
        print(f"Between {item[0]} and {item[1]}: {item[2]:.2f}")

    # Return None, as we're only printing the results
    return None
    # return weak_correlations, moderate_correlations, strong_correlations