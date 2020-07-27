## Linear regression
### page 23
# Training data
X = [[6], [8], [10], [14], [18]]
y = [[7], [9], [13], [17.5], [18]]
XTest=[[12],[14]]
###Create and fit the model
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X, y)
print("Xtest")
print(XTest)
print ('pizza predict should cost: ')
a=model.predict(XTest)
print(a)
####A 12" pizza should cost: $13.68