from sklearn.linear_model import LinearRegression
## Training data- build model
X = [[6, 2], [8, 1], [10, 0], [14, 2], [18, 0]]
y = [[7], [9], [13], [17.5], [18]]
model = LinearRegression()
model.fit(X, y)
## Test model
X_test = [[8, 2], [9, 0], [11, 2], [16, 2], [12, 0]]
y_test = [[11], [8.5], [15], [18], [11]]
## Test model
predictions = model.predict(X_test)
for i, prediction in enumerate(predictions):
    print ('Predicted: %s, Target: %s' % (prediction, y_test[i]))
    print ('R-squared: %.2f' % model.score(X_test, y_test))

# Predicted: [ 10.0625], Target: [11]
# Predicted: [ 10.28125], Target: [8.5]
# Predicted: [ 13.09375], Target: [15]
# Predicted: [ 18.14583333], Target: [18]
# Predicted: [ 13.3125], Target: [11]
# R-squared: 0.77