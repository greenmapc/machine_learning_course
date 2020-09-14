import pandas as pd
import matplotlib.pyplot as plt

MALE_CONST = 'male'
FEMALE_CONST = 'female'


def preparing_data(data, gender):
    survived_number = data[data.Sex.isin([gender]) & data.Survived.isin([1])]
    not_survived_number = data[data.Sex.isin([gender]) & data.Survived.isin([0])]
    survived_info = [survived_number.shape[0], not_survived_number.shape[0]]
    return survived_info


def show_plot(men_info, woomen_info):
    width = 0.4
    labels = ['Survived', 'Did not survived']
    fig, ax = plt.subplots()

    ax.bar(labels, men_info, width, label='Men')
    ax.bar(labels, woomen_info, width, bottom=men_info, label='Women')
    ax.set_title('Statistic')
    ax.legend()
    plt.savefig('stat.png')


data = pd.read_csv("titanic_data.csv", sep=',')
male_survived_info = preparing_data(data, MALE_CONST)
female_survived_info = preparing_data(data, FEMALE_CONST)
show_plot(male_survived_info, female_survived_info)
