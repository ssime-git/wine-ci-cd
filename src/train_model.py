# train_model.py
from sklearn.ensemble import RandomForestRegressor
from config import SEED, METRICS_PATH, MODEL_PATH
import joblib
import logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%m/%d/%Y %I:%M:%S %p'
)

def train_and_evaluate(X_train, X_test, y_train, y_test):
    logging.info("Fitting model")
    regr = RandomForestRegressor(max_depth=2, random_state=SEED)
    regr.fit(X_train, y_train)
    logging.info("Model fitted")
    logging.info("Evaluating model")
    train_score = regr.score(X_train, y_train) * 100
    test_score = regr.score(X_test, y_test) * 100
    logging.info("Model evaluated")
    logging.info("Writing scores to a file")
    with open(METRICS_PATH, 'w') as outfile:
        outfile.write("Training variance explained: %2.1f%%\n" % train_score)
        outfile.write("Test variance explained: %2.1f%%\n" % test_score)
    logging.info("Done saving metrics")
    logging.info("Saving model")
    joblib.dump(regr, MODEL_PATH)
    return regr