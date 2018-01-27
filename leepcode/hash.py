def hashing_vectorizer(s, N):
    x = [0 for i in range(N)]
    for f in s.split():
        h = hash(f)
        print(h%N)
        x[h % N] += 1
    return x


print (hashing_vectorizer('we are the great', 6)) # return [0, 1, 3, 0]
#print (hashing_vectorizer('tell me the way to the IBM', 4))  # return [1, 3, 3, 0]

import pandas as pd
import numpy as np

data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
        'year': [2000, 2001, 2002, 2001, 2002],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}

data = pd.DataFrame(data)

def hash_col(df, col, N):
    cols = [col + "_" + str(i) for i in range(N)]
    def xform(x):
        tmp = [0 for i in range(N)];
        tmp[hash(x) % N] = 1;
        return pd.Series(tmp,index=cols)
        df[cols] = df[col].apply(xform)
    return df.drop(col,axis=1)

print (hash_col(data, 'state',4))

