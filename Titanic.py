import pandas as pd
import matplotlib as plt

def show_plot(data):
    fig, ax = plt.subplots()

    rects1 = ax.bar(men_means, width, label='Men')
    rects2 = ax.bar(x + width / 2, women_means, width, label='Women')

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('age')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()


data = pd.read_csv("train.csv", sep=',')
show_plot(data)


