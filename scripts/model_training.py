from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestRegressor
import matplotlib.pyplot as plt

def train(X_train,y_train,X_test,y_test):
    model = LinearRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    mse = mean_squared_error(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print(f'MSE: {mse}')
    print(f'MAE: {mae}')
    print(f'R2: {r2}')
    return model


def optimised_training(X_train,y_train,X_test,y_test):
    param_grid = {
        'n_estimators': [50],
        'max_depth': [3],
        'learning_rate': [0.01]
    }

    grid_search = GridSearchCV(GradientBoostingRegressor(), param_grid, cv=5, scoring='neg_mean_squared_error')
    grid_search.fit(X_train, y_train)

    print("Best Parameters:", grid_search.best_params_)
    model = grid_search.best_estimator_

    y_pred_best = model.predict(X_test)
    mse_best = mean_squared_error(y_test, y_pred_best)
    mae_best = mean_absolute_error(y_test, y_pred_best)
    r2_best = r2_score(y_test, y_pred_best)

    print(f'Best MSE: {mse_best}')
    print(f'Best MAE: {mae_best}')
    print(f'Best R2: {r2_best}')
    return model    

def optimised_training_random_forest(X_train, y_train, X_test, y_test):
    param_grid = {
        'n_estimators': [200],
        'max_depth': [10],
        'min_samples_split': [10]
    }

    
    grid_search = GridSearchCV(RandomForestRegressor(random_state=42), param_grid, cv=5, scoring='neg_mean_squared_error')
    grid_search.fit(X_train, y_train)

    print("Best Parameters:", grid_search.best_params_)
    model = grid_search.best_estimator_

    y_pred_best = model.predict(X_test)
    mse_best = mean_squared_error(y_test, y_pred_best)
    mae_best = mean_absolute_error(y_test, y_pred_best)
    r2_best = r2_score(y_test, y_pred_best)

    print(f'Best MSE: {mse_best}')
    print(f'Best MAE: {mae_best}')
    print(f'Best R²: {r2_best}')
    return model


