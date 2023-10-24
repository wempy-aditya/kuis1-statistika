import matplotlib.pyplot as plt
import pandas as pd

data = {
    'GENDER': ['Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female'],
    'AGE': [35, 42, 50, 28, 65, 38, 44, 53, 30, 47, 60, 33, 39, 58, 45, 48, 56, 29, 52, 41],
    'BMI': [28.5, 24.9, 31.2, 22.7, 27.8, 29.1, 26.3, 27.6, 30.0, 23.5, 26.9, 28.1, 29.8, 25.3, 28.7, 24.6, 31.4, 23.8, 27.2, 29.0],
    'CHOLESTEROL': [200, 180, 220, 160, 190, 210, 180, 210, 220, 170, 190, 200, 230, 190, 180, 170, 220, 160, 190, 210],
    'HEART RATE': [75, 80, 72, 68, 78, 70, 72, 76, 74, 68, 75, 72, 76, 78, 72, 74, 72, 68, 80, 70],
    'SMOKING STATUS': ['Never', 'Current', 'Pass', 'Never', 'Current', 'Never', 'Never', 'Current', 'Pass', 'Never', 'Current', 'Never', 'Current', 'Never', 'Never', 'Current', 'Pass', 'Never', 'Current', 'Never'],
    'GENETIC DISEASE': ['No', 'Yes', 'No', 'No', 'Yes', 'No', 'Yes', 'No', 'Yes', 'No', 'Yes', 'No', 'No', 'Yes', 'No', 'No', 'Yes', 'No', 'Yes', 'No']
}

# Create a DataFrame
df = pd.DataFrame(data)

# Create side by side box plots for AGE, BMI, CHOLESTEROL, and HEART RATE
plt.figure(figsize=(12, 6))

# Age
plt.subplot(2, 2, 1)
plt.title('Age')
plt.boxplot([df[df['GENDER'] == 'Male']['AGE'], df[df['GENDER'] == 'Female']['AGE']], labels=['Male', 'Female'])

# BMI
plt.subplot(2, 2, 2)
plt.title('BMI')
plt.boxplot([df[df['GENDER'] == 'Male']['BMI'], df[df['GENDER'] == 'Female']['BMI']], labels=['Male', 'Female'])

# Cholesterol
plt.subplot(2, 2, 3)
plt.title('Cholesterol')
plt.boxplot([df[df['GENDER'] == 'Male']['CHOLESTEROL'], df[df['GENDER'] == 'Female']['CHOLESTEROL']], labels=['Male', 'Female'])

# Heart Rate
plt.subplot(2, 2, 4)
plt.title('Heart Rate')
plt.boxplot([df[df['GENDER'] == 'Male']['HEART RATE'], df[df['GENDER'] == 'Female']['HEART RATE']], labels=['Male', 'Female'])

plt.tight_layout()
plt.show()
