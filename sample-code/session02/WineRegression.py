### WineRegreesion
### Date: July 5 2020
import pandas as pd
df = pd.read_csv('data\winequality-red.csv', sep=';')
df.describe()
### Ve do thi ve du lieu nhap
import matplotlib.pylab as plt
plt.scatter(df['alcohol'], df['quality'])
plt.xlabel('Alcohol')
plt.ylabel('Quality')
plt.title('Alcohol Against Quality')
plt.show()
### Tinh hoi qui
from sklearn.linear_model import LinearRegression
import pandas as pd
import matplotlib.pylab as plt
from sklearn.model_selection import train_test_split
df = pd.read_csv('data/winequality-red.csv', sep=';')
X = df[list(df.columns)[:-1]]
y = df['quality']
X_train, X_test, y_train, y_test = train_test_split(X, y)
regressor = LinearRegression()
regressor.fit(X_train, y_train)
y_predictions = regressor.predict(X_test)
print ('R-squared:', regressor.score(X_test, y_test))
#### Output 0.345622479617