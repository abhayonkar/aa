import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# Load the dataset
url = 'https://raw.githubusercontent.com/selva86/datasets/master/Advertising.csv'
data = pd.read_csv(url)

# Display the first few rows of the dataset
print(data.head())

# Define features and target
X = data[['TV', 'radio', 'newspaper']]
y = data['sales']

from sklearn.model_selection import train_test_split

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Simple Linear Regression
X_train_simple = X_train[['TV']]
X_test_simple = X_test[['TV']]

model_simple = LinearRegression()
model_simple.fit(X_train_simple, y_train)

y_pred_simple = model_simple.predict(X_test_simple)
print("Simple Linear Regression - R2 Score:", r2_score(y_test, y_pred_simple))
print("Simple Linear Regression - MSE:", mean_squared_error(y_test, y_pred_simple))

# Multi-Linear Regression
model_multi = LinearRegression()
model_multi.fit(X_train, y_train)

y_pred_multi = model_multi.predict(X_test)
print("Multi-Linear Regression - R2 Score:", r2_score(y_test, y_pred_multi))
print("Multi-Linear Regression - MSE:", mean_squared_error(y_test, y_pred_multi))


from sklearn.preprocessing import PolynomialFeatures

# Polynomial Regression
poly = PolynomialFeatures(degree=2)
X_train_poly = poly.fit_transform(X_train)
X_test_poly = poly.transform(X_test)

model_poly = LinearRegression()
model_poly.fit(X_train_poly, y_train)

y_pred_poly = model_poly.predict(X_test_poly)
print("Polynomial Regression - R2 Score:", r2_score(y_test, y_pred_poly))
print("Polynomial Regression - MSE:", mean_squared_error(y_test, y_pred_poly))


results = {
    "Simple Linear Regression": {
        "R2 Score": r2_score(y_test, y_pred_simple),
        "MSE": mean_squared_error(y_test, y_pred_simple)
    },
    "Multi-Linear Regression": {
        "R2 Score": r2_score(y_test, y_pred_multi),
        "MSE": mean_squared_error(y_test, y_pred_multi)
    },
    "Polynomial Regression": {
        "R2 Score": r2_score(y_test, y_pred_poly),
        "MSE": mean_squared_error(y_test, y_pred_poly)
    }
}

print(pd.DataFrame(results).T)
