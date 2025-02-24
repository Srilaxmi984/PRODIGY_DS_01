import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Print the current working directory
print("Current Working Directory:", os.getcwd())

# Set the correct directory (update the path if needed)
correct_path =  r"C:\Users\srila\OneDrive\Desktop\PROJECTS\PRODIGY_DS_01"
os.chdir(correct_path)
print("New Working Directory:", os.getcwd())

# File path
file_path = os.path.join(correct_path, "world_population.csv")

# Check if the file exists
if not os.path.exists(file_path):
    print(f"❌ Error: File not found at {file_path}")
else:
    print("✅ File found! Proceeding with data processing...")

    # Load the dataset
    df = pd.read_csv(file_path, skiprows=4, encoding="ISO-8859-1")

    # Clean the data
    df_cleaned = df.drop(columns=['Country Code', 'Indicator Name', 'Indicator Code'])
    df_cleaned = df_cleaned.rename(columns={'Country Name': 'Country'})
    df_cleaned = df_cleaned[['Country', '2022']]
    df_cleaned = df_cleaned.dropna()

    # 1. Histogram: Distribution of Population Sizes
    plt.figure(figsize=(10, 6))
    sns.histplot(df_cleaned['2022'], bins=30, kde=True, color='blue')
    plt.title('Distribution of Population Sizes Across Countries (2022)')
    plt.xlabel('Population')
    plt.ylabel('Frequency')
    plt.show()

    # 2. Bar Chart: Population of Selected Countries
    selected_countries = ['United States', 'China', 'India', 'Brazil', 'Nigeria', 'Germany']
    df_selected = df_cleaned[df_cleaned['Country'].isin(selected_countries)]

    plt.figure(figsize=(10, 6))
    sns.barplot(x='Country', y='2022', data=df_selected, palette='viridis')
    plt.title('Population of Selected Countries (2022)')
    plt.xlabel('Country')
    plt.ylabel('Population')
    plt.xticks(rotation=45)
    plt.show()