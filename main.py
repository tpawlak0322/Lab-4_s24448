from scripts import load_data as loader
from scripts import prepare_data as prep
from scripts import model_training as training
import joblib

data = loader.load()

X_train, X_test, y_train, y_test = prep.prepare_data(data)

model = training.train(X_train=X_train,X_test=X_test,y_train=y_train,y_test=y_test)
optimised_model = training.optimised_training(X_train=X_train,X_test=X_test,y_train=y_train,y_test=y_test)
optimised_model_rf = training.optimised_training_random_forest(X_train=X_train,X_test=X_test,y_train=y_train,y_test=y_test)

joblib.dump(optimised_model_rf, 'optimised_model.pkl')
