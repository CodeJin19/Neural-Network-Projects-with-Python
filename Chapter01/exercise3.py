import numpy as np
import pandas as pd

if __name__ == "__main__":
    url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
    df = pd.read_csv(url, names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class'])

    # 로우 열 개를 무작위로 선정
    random_index = np.random.choice(df.index, replace = False, size = 10)

    # 무작위로 고른 로우의 sepal_length 값을 None으로 수정
    df.loc[random_index, 'sepal_length'] = None

    print(df.isnull().any())