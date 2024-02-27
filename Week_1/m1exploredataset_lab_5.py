# -*- coding: utf-8 -*-
"""M1ExploreDataSet-lab_5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14m-m7_DYpDVp9yV7qvfU18OyDaolcFOU

# **Survey Dataset Exploration Lab**

Estimated time needed: **30** minutes

## Objectives

After completing this lab you will be able to:

-   Load the dataset that will used thru the capstone project.
-   Explore the dataset.
-   Get familier with the data types.

## Load the dataset

Import the required libraries.
"""

import pandas as pd

"""The dataset is available on the IBM Cloud at the below url.

"""

dataset_url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/LargeData/m1_survey_data.csv"

"""Load the data available at dataset_url into a dataframe.

"""

df = pd.read_csv(dataset_url)

"""## Explore the data set

It is a good idea to print the top 5 rows of the dataset to get a feel of how the dataset will look.

Display the top 5 rows and columns from your dataset.
"""

print(df.head())

"""## Find out the number of rows and columns

Start by exploring the numbers of rows and columns of data in the dataset.

Print the number of rows in the dataset.
"""

num_rows = df.shape[0]
print("Number of rows:", num_rows)

"""Print the number of columns in the dataset.

"""

num_columns = df.shape[1]
print("Number of columns:", num_columns)

"""## Identify the data types of each column

Explore the dataset and identify the data types of each column.

Print the datatype of all columns.
"""

print(df.dtypes)

"""Print the mean age of the survey participants.

"""

mean_age = df['Age'].mean()
print("Mean age of survey participants:", mean_age)

"""The dataset is the result of a world wide survey. Print how many unique countries are there in the Country column.

"""

unique_countries = df['Country'].nunique()
print("Number of unique countries in the dataset:", unique_countries)