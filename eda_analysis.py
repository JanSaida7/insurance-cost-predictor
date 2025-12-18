import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv('insurance.csv')

# Basic inspection
print("Data Head:")
print(df.head())
print("\nData Info:")
print(df.info())
print("\nData Description:")
print(df.describe())

# Handle categorical variables for EDA
# Convert 'smoker' and 'sex' to numerical for correlation analysis
df_eda = df.copy()
df_eda['smoker'] = df_eda['smoker'].apply(lambda x: 1 if x == 'yes' else 0)
df_eda['sex'] = df_eda['sex'].apply(lambda x: 1 if x == 'male' else 0)

# One-Hot Encoding for 'region'
df_eda = pd.get_dummies(df_eda, columns=['region'], drop_first=True)

# Visualizations
plt.figure(figsize=(10, 6))
sns.scatterplot(x='bmi', y='charges', hue='smoker', data=df)
plt.title('BMI vs Charges')
plt.savefig('bmi_vs_charges.png')
print("Saved bmi_vs_charges.png")

plt.figure(figsize=(10, 6))
sns.boxplot(x='smoker', y='charges', data=df)
plt.title('Smoker vs Charges')
plt.savefig('smoker_vs_charges.png')
print("Saved smoker_vs_charges.png")

# Correlation Heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(df_eda.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.savefig('correlation_heatmap.png')
print("Saved correlation_heatmap.png")
