# data_prep.py
import pandas as pd
from sklearn.model_selection import train_test_split
from config import DATA_PATH, TEST_SIZE, SEED, TARGET_COLUMN
import logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%m/%d/%Y %I:%M:%S %p'
)

def load_data(data_path=DATA_PATH):
    logging.info(f"Loading data from {data_path}")
    df = pd.read_csv(data_path)
    y = df.pop(TARGET_COLUMN)
    logging.info("Data loaded")

    logging.info("splitting data")
    X_train, X_test, y_train, y_test = train_test_split(df, y, test_size=TEST_SIZE, random_state=SEED)
    logging.info("Data split")
    return X_train, X_test, y_train, y_test