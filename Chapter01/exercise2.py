import pandas as pd
import matplotlib.pyplot as plt

if __name__ == "__main__":
    url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
    df = pd.read_csv(url, names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class'])

    # print(df.info())
    # print(df.describe())
    # print(df.head(10))
    # print(df.loc[df['sepal_length'] > 5.0,].head(10))

    '''
    # 점차트
    marker_shapes = ['.', '^', '*']
    ax = plt.axes()
    
    for i, species in enumerate(df['class'].unique()):
        species_data = df[df['class'] == species]
        species_data.plot.scatter(x = 'sepal_length', y = 'sepal_width', marker = marker_shapes[i], s = 100, title = "Sepal Width vs Length by Species", label = species, figsize = (10, 7), ax = ax)

    plt.show()
    plt.clf()
    '''

    '''
    # 히스토그램
    df['petal_length'].plot.hist(title = 'Histogram of Petal Length')
    plt.show()
    '''

    # 캔들차트
    df.plot.box(title = 'Boxplot of Sepal Length & Width, and Petal Length & Width')
    plt.show()