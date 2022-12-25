# This is a README file for ds_functions.py file

This code defines three functions in Python: **outliers_iqr**, **outliers_z_score**, and **uninform_finder**.

The **outliers_iqr** function takes in the following arguments:

    data: a pandas DataFrame
    feature: a string representing a column in the DataFrame
    left: a float representing the number of interquartile ranges (IQR) to extend below the first quartile (default is 1.5)
    right: a float representing the number of IQRs to extend above the third quartile (default is 1.5)
    log_scale: a boolean representing whether to apply log scaling to the data before calculating the IQR (default is False)

The function calculates the lower and upper bounds for the given feature using the specified number of IQRs and returns a tuple containing two DataFrames: the first contains the rows in data that fall outside of these bounds (i.e., the outliers), and the second contains the rows that fall within these bounds (i.e., the cleaned data).

The **outliers_z_score** function is similar to **outliers_iqr**, but it uses the z-score method to identify outliers. The arguments are the same as for **outliers_iqr**, except that the default values for left and right are 3.

The **uninform_finder** function takes in a DataFrame and a threshold value (default is 0.95) and returns a list of columns in the DataFrame that are considered low-information, i.e., they have a high percentage of repeated values or a high percentage of unique values. The function iterates over each column in the DataFrame and compares the maximum frequency of any value in the column with the threshold value, as well as the ratio of unique values in the column to the total number of values. If either of these values is above the threshold, the column is considered low-information and is added to the list of low-information columns.