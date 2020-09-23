import pandas as pd
from matplotlib import pyplot
from EVcharger_datagenerator import TimeValueGenerator

def main():

    # Class instance
    time_generator = TimeValueGenerator(50, 5, 30, 'ev_data.csv')

    # Calls the generate method
    time_generator.generate_time_values()

    df = pd.read_csv("ev_data.csv")
    df.groupby('date_time').cumsum()['power'].plot(x='date_time', y='power')
    pyplot.show()


if __name__ == '__main__':
    main()