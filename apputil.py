import seaborn as sns
import pandas as pd


# update/add code below ...

#Exercise 1: Write a recursive function (fibonacci) that, given n, will give the nth number of the Fibonacci Series.

def fibonacci(n):

    """Recursion function to find the nth number in the Fibonacci series"""

    # Input validation
    if not (isinstance(n, int) and n >= 0):
        raise ValueError("n has to be a positive integer")

    # Base cases
    if n in {0,1}:
        return n

    # Recursive case
    return fibonacci(n-1) + fibonacci(n-2)


# Test cases
print(fibonacci(9))  # 34 
print(fibonacci(12)) # 144


#Exercise 2 : Write a (single) recursive function, to_binary(), that converts an integer into its binary representation

def to_binary(n):

    """Return the binary representation of a positive integer using recursion"""

    # Input Validation
    if not (isinstance(n , int) and n>=0):
         raise ValueError("n has to be a positive integer")

    # Base case
    if n in {0,1}:
        return str(n)

    # Recursive case
    return to_binary(n//2) + str(n%2)

# Test cases
print(to_binary(12))  # '1100'
print(to_binary(0))   # '0'
print(to_binary(1))   # '1'
print(to_binary(2))   # '10'



# Exercise 3: Write a function for each of the following tasks

url = 'https://github.com/melaniewalsh/Intro-Cultural-Analytics/raw/master/book/data/bellevue_almshouse_modified.csv'

df_bellevue = pd.read_csv(url)
# df_bellevue = pd.read_csv('./data/.../mydata.csv')  # you can also reference locally stored data 

# Task 1: List of column names sorted by missing values
def task_1():
    
    """Column names sorted my missing values"""

    # Clean gender column
    df = df_bellevue.copy()
    df['gender'] = df['gender'].astype(str).str.strip().str.lower()

    # Treat 'nan', 'none', '' as missing values
    df['gender'] = df['gender'].replace({'h': pd.NA, 'g': pd.NA, 'm': 'm', 'f': 'f', '?': pd.NA})

    # Calculate missing counts per column
    missing_count = df.isnull().sum()

    # Sort columns by missing counts in ascending order
    sorted_cols = list(missing_count.sort_values().index)

    return sorted_cols

# Task 2: DataFrame with year and total admissions per year

def task_2():

    df = df_bellevue.copy()

    """DataFrame with year and total admissions per year"""
    
    # Parse data into datatime format
    df['date_in'] = pd.to_datetime(df['date_in'], errors = 'coerce')

    # Drop rows with missing or invalid date_in
    df_2 = df.dropna(subset=['date_in'])

    # Extract year from date_in
    df_2['year'] = df_2['date_in'].dt.year

    # Group by year and count admissions
    admission_per_year = df_2.groupby('year').size().reset_index(name = 'total_admissions')

    return admission_per_year

# Task 3: Series with average age at admission per year

def task_3():

    df = df_bellevue.copy()

    """Calculate average age at admission per year"""
    
    # Clean gender column
    df = df_bellevue.copy()
    df['gender'] = df['gender'].astype(str).str.strip().str.lower()

    # Treat 'nan', 'none', '' as missing values
    df['gender'] = df['gender'].replace({'nan': None, 'none':None, '': None})

    # Convert age to numeric
    df['age'] = pd.to_numeric(df['age'] , errors = 'coerce')

    # Drop any rows with missing or invalid gender or age
    df_3 = df.dropna(subset = ['gender' , 'age'])
    
    # Calculate average age per gender
    avg_age = df_3.groupby('gender')['age'].mean()

    return avg_age


# Task 4 : List of 5 common professions in order of prevalence

def task_4():

    df = df_bellevue.copy()

    """ List of 5 common professions in order of prevalence"""

    # Clean profession column with strip white spaces and lower case
    df['profession'] = df['profession'].astype(str).str.strip().str.lower()

    # Replace empty strings with NaN
    df['profession'] = df['profession'].replace({'': None , 'nan': None, 'none': None})

    # Drop rows with missing professions
    df_pf = df.dropna(subset = ['profession'])

    # Count values in profession column
    counts = df_pf['profession'].value_counts()

    top_5_pf = list(counts.head(5).index)

    # If messy data in profession column, print a warning
    print("Messy issues: profession values may have inconsistent casing, spelling, whitespace.")


    return top_5_pf

# Test Cases
print(task_1())          # list of columns sorted by missingness
print(task_2().head())   # first few rows of year vs total admissions
print(task_3())          # average age per gender
print(task_4())          # top 5 professions









    
