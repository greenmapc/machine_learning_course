import numpy as np
import pandas as pd

disease = pd.read_csv('disease.csv', delimiter=";")
symptom = pd.read_csv('symptom.csv', delimiter=";")

rand_symp = [np.random.randint(0, 2) for i in range(23)]

p_disease = []
for i in range(len(disease) - 1):
    p_disease.append(disease['количество пациентов'][i] / disease['количество пациентов'][len(disease) - 1])

# игнорируем знаменатель из формулы, так как он одинаков для всех
p_disease_symptoms = [1] * (len(disease) - 1)
for i in range(len(disease) - 1):
    p_disease_symptoms[i] *= p_disease[i]
    for j in range(len(symptom)-1):
        if rand_symp[j] == 1:
            p_disease_symptoms[i] *= float(symptom.iloc[j + 1][i + 1])

# найдем наиболее вероятное заболевание при сгенерированных симптомах
max = 0
disease_index = 0
for i in range (0, len(p_disease_symptoms)):
    if p_disease_symptoms[i] > max:
        max = p_disease_symptoms[i]
        disease_index = i

print(disease.iloc[disease_index][0])
