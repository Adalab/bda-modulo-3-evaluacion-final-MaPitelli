### Importamos las librerías que necesitamos
# Tratamiento de datos
# -----------------------------------------------------------------------
import pandas as pd
import numpy as np
from itertools import combinations

# Evaluar linealidad de las relaciones entre las variables y la distribución de las variables
# ------------------------------------------------------------------------------
import scipy.stats as stats
from scipy.stats import kstest, shapiro, mannwhitneyu


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


def categorize(education_level, group_a, group_b):
    """
    Categorizes education levels into two groups based on provided lists.
    
    Parameters:
    - education_level: The education level to categorize.
    - group_a: List of education levels considered as lower.
    - group_b: List of education levels considered as higher.
    
    Returns:
    - 'group_a' for lower education levels
    - 'group_b' for higher education levels
    - 'Unknown' for values not in provided lists
    """
    if education_level in group_a:
        return 'group_a'
    elif education_level in group_b:
        return 'group_b'
    else:
        return 'Unknown'  # To handle values that do not match the defined groups


def determine_problem_type(dataframe, metric):
    """
    Determines whether the problem is about proportions or means.
    
    Parameters:
    - metric (str): The name of the metric to be analyzed.

    Returns:
    - str: "proportions" if the metric is binary, "means" if the metric is continuous.
    """
    # Check if the metric is binary
    unique_values = dataframe[metric].dropna().unique()
    if set(unique_values).issubset({0, 1}):
        return "proportions"
    else:
        return "means"


def normality_test(dataframe, metric, method='shapiro', alpha=0.05):
    """
    Performs a test to check the normality of data using Shapiro-Wilk or Kolmogorov-Smirnov.

    Parameters:
    - metric (str): The name of the metric to be analyzed.
    - method (str): The method to use for the normality test ('shapiro' or 'ks').
    - alpha (float): The significance level for the normality test (default is 0.05).

    Returns:
    - tuple: The test statistic and the p-value.
    """
    data = dataframe[metric].dropna()

    if method == 'shapiro':
        stat, p_value = shapiro(data)
    elif method == 'ks':
        stat, p_value = kstest(data, 'norm')
    else:
        raise ValueError("Unsupported method. Use 'shapiro' or 'ks'.")

    if p_value > alpha:
        print(f"The data for the metric '{metric}' follows a normal distribution (p-value = {p_value:.4f}).")
    else:
        print(f"The data for the metric '{metric}' does not follow a normal distribution (p-value = {p_value:.4f}).")

    return stat, p_value


def mann_whitney_test(dataframe, metric_columns, control_group, test_group, group_column='test_group', alpha=0.05):
    """
    Performs the Mann-Whitney U test to compare the medians of metrics between two groups in a given DataFrame.

    Parameters:
    - metric_columns (list): A list of column names representing the metrics to compare between groups.
    - control_group (str): The name of the control group in the column specified by group_column.
    - test_group (str): The name of the test group in the column specified by group_column.
    - group_column (str): The name of the column that contains the group information (default is 'test_group').
    - alpha (float): The significance level for the test (default is 0.05).

    Returns:
    - None: Prints to the console whether the medians are different or the same for each metric.
    """
    # Filter the DataFrame to keep only the control and test data
    control = dataframe[dataframe[group_column] == control_group]
    test = dataframe[dataframe[group_column] == test_group]

    # Iterate over the metric columns to see if there are differences between the groups for each metric
    for metric in metric_columns:
        metric_control = control[metric].dropna()
        metric_test = test[metric].dropna()

        # Apply the statistic
        u_statistic, p_value = mannwhitneyu(metric_control, metric_test)

        # Print the result of the test
        if p_value < alpha:
            print(f"For the metric '{metric}', the medians are different (p-value = {p_value:.4f}).")
        else:
            print(f"For the metric '{metric}', the medians are the same (p-value = {p_value:.4f}).")


