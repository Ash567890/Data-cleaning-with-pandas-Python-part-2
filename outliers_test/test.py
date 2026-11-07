import pandas as pd
import numpy as np

# Loading the data in Pandas

data = pd.read_csv(r"D:\Downloads\data_analytics_data\messy_ecommerce_data.csv", sep=",",na_values=['N/A', 'NULL','','NA'], encoding='ISO-8859-1', low_memory=False)

# Making a copy of a dataframe 

df = data.copy()

# Working on OrderID Column 

# Finding leading and trailing spaces

df[df.OrderID.str.strip() != df.OrderID]

# Checking for null values 

df.OrderID.isnull().sum()

# Define the correct pattern:
# ^     = starts with
# ORD-  = literal text "ORD-"
# \d+   = one or more digits
# $     = ends right there
correct_pattern = r"^ORD-\d+$"

# Find rows where OrderID does NOT match the correct pattern

outliers = df[~df["OrderID"].astype(str).str.match(correct_pattern)]

print(f"Total outliers found: {len(outliers)}")
print(outliers[["OrderID"]])

# Define the correct pattern:
# ^     = starts with
# ORD-  = literal text "ORD-"
# \d+   = one or more digits
# $     = ends right there
correct_pattern = r"^ORD-\d+$"

# Find rows where OrderID does NOT match the correct pattern
outliers2 = df[df["OrderID"].astype(str).str.match(correct_pattern)].sample(n=10)

print(f"Total outliers found: {len(outliers2)}")
print(outliers2[["OrderID"]])

# Working on Date Column

# Define the correct strict format pattern: YYYY-MM-DD
# ^         = starts with
# \d{4}     = exactly 4 digits (Year)
# -         = literal hyphen
# \d{2}     = exactly 2 digits (Month)
# -         = literal hyphen
# \d{2}     = exactly 2 digits (Day)
# $         = ends right there
correct_date_pattern = r"^\d{4}-\d{2}-\d{2}$"

# Find rows where OrderDate does NOT match the required format
date_outliers = df[~df["OrderDate"].astype(str).str.match(correct_date_pattern)]

print(f"Total date outliers found: {len(date_outliers)}")
print(date_outliers)

# Checking the sample data for views 

date_outliers['OrderDate'].sample(n=20)

# Working on Name column

df[df.CustomerName.str.strip() == df.CustomerName]

# Working on Email column

df.CustomerEmail.isnull().sum()

df.CustomerEmail.sample(n=15)

# Standard regex pattern covering regular local parts, domains, and standard TLD extensions
email_pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

# Find incorrect/outlier email rows
# (Using ~ to filter for rows that DO NOT match a valid structure)
email_outliers = df[~df["CustomerEmail"].astype(str).str.match(email_pattern)]

email_outliers[['CustomerEmail']]

# Working on Age column

# Checking the age below 0

df[df.CustomerAge<0]['CustomerAge'].abs()

# Checking the age above 100

df[df.CustomerAge>100]

# Change the data type to int 

df['CustomerAge'] = df['CustomerAge'].astype('Int64')

# Working on Country Column

df.Country.unique()

# Working on ProductCategory

df.ProductCategory.unique()

df[df.ProductCategory.str.strip() == '']

# Working on UnitPrice

df['UnitPrice'] = df['UnitPrice'].abs()

#Checking the relation between UnitPrice and Product 

df[(df.UnitPrice<=0) | (df.UnitPrice > 5000)][['UnitPrice','ProductCategory']]

df[df.Quantity<0].Quantity
























