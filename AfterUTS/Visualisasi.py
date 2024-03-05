# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt

# # Membaca data dari file CSV
# file_path = './coin_Bitcoin.csv'
# df = pd.read_csv(file_path)

# x = np.random.normal(df['Open'].mean(), df['Open'].std(), 100)
# plt.gca().set(title='Normal Distribution of Opening Prices', ylabel='Frequency')
# plt.hist(x, 100)
# plt.show()

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Membaca data dari file CSV
file_path = './coin_Bitcoin.csv'
df = pd.read_csv(file_path)

plt.plot(df.index,df['Close'])
plt.gca().set(title='Bitcoin Closing Prices', xlabel='Year', ylabel='Closing Prices USD ($)')
plt.show()