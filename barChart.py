import matplotlib.pyplot as plt
import numpy as np

data = {
    'GENDER': ['Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female'],
    'AGE': [35, 42, 50, 28, 65, 38, 44, 53, 30, 47, 60, 33, 39, 58, 45, 48, 56, 29, 52, 41],
    'BMI': [28.5, 24.9, 31.2, 22.7, 27.8, 29.1, 26.3, 27.6, 30.0, 23.5, 26.9, 28.1, 29.8, 25.3, 28.7, 24.6, 31.4, 23.8, 27.2, 29.0],
    'BLOOD PRESSURE': ['120/80', '130/85', '140/90', '115/75', '135/85', '125/80', '125/78', '130/82', '140/88', '118/76', '135/85', '120/78', '142/90', '128/82', '125/80', '130/85', '140/88', '115/75', '135/85', '125/80'],
    'CHOLESTEROL': [200, 180, 220, 160, 190, 210, 180, 210, 220, 170, 190, 200, 230, 190, 180, 170, 220, 160, 190, 210],
    'HEART RATE': [75, 80, 72, 68, 78, 70, 72, 76, 74, 68, 75, 72, 76, 78, 72, 74, 72, 68, 80, 70],
    'SMOKING STATUS': ['Never', 'Current', 'Pass', 'Never', 'Current', 'Never', 'Never', 'Current', 'Pass', 'Never', 'Current', 'Never', 'Current', 'Never', 'Never', 'Current', 'Pass', 'Never', 'Current', 'Never'],
    'GENETIC DISEASE': ['No', 'Yes', 'No', 'No', 'Yes', 'No', 'Yes', 'No', 'Yes', 'No', 'Yes', 'No', 'No', 'Yes', 'No', 'No', 'Yes', 'No', 'Yes', 'No']
}

# Extract GENDER and GENETIC DISEASE data for the bar chart
gender = data['GENDER']
genetic_disease = data['GENETIC DISEASE']

# Count the occurrences of 'Yes' and 'No' for genetic disease in each gender
male_genetic_disease_count = genetic_disease[:10].count('Yes')
female_genetic_disease_count = genetic_disease[10:].count('Yes')

# Create bar chart
x = np.arange(2)  # Two bars
bar_width = 0.35

plt.bar(x, [male_genetic_disease_count, female_genetic_disease_count], bar_width, label='Yes')
plt.bar(x + bar_width, [10 - male_genetic_disease_count, 10 - female_genetic_disease_count], bar_width, label='No')

plt.xlabel('Gender')
plt.ylabel('Count')
plt.title('Genetic Disease by Gender')
plt.xticks(x + bar_width / 2, ['Male', 'Female'])
plt.legend()

plt.show()
