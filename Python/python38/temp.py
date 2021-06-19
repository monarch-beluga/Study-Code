# from sklearn.linear_model import Ridge
# import numpy as np
# import pandas as pd
#
# csv = "E:/Data/temp/modis_points.csv"
# df = pd.read_csv(csv, index_col=0)
# df1 = df.iloc[:, 2:]
# x = df1.columns.astype('int').values


# n_samples, n_features = 10, 5
# rng = np.random.RandomState(0)
# y = rng.randn(n_samples)
# X = rng.randn(n_samples, n_features)
# clf = Ridge(alpha=1.0)
# clf.fit(X, y)

import requests

url = 'https://s3.ananas.chaoxing.com/doc/00/63/5b/2b4b9585cd1062027224be134c8623f2/thumb/{0}.png'
path = r'E:/'

for i in range(1, 2):
    src_url = url.format(i)
    img = requests.get(url=src_url).content
    with open(path + '{0}.png'.format(i), 'wb') as fp:
        fp.write(img)
    print(i)
