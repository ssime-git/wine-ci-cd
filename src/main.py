# main.py
from data_prep import load_data
from train_model import train_and_evaluate
from plotting import plot_feature_importance, plot_residuals
import logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%m/%d/%Y %I:%M:%S %p'
)

def main():
    # Data preparation
    X_train, X_test, y_train, y_test = load_data()
    
    # Model training and evaluation
    regr = train_and_evaluate(X_train, X_test, y_train, y_test)
    
    # Plotting
    plot_feature_importance(regr, X_train.columns)
    plot_residuals(X_test, y_test, regr)

if __name__ == '__main__':
    logging.info("Running main")
    main()
    logging.info("Done")