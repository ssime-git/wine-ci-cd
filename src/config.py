# config.py
SEED = 42
DATA_PATH = "data/wine_quality.csv"
TEST_SIZE = 0.2
MODEL_PATH = "models/random_forest_regressor.joblib"
METRICS_PATH = "report/metrics.txt"
FEATURE_IMPORTANCE_PLOT_PATH = "report/feature_importance.png"
RESIDUALS_PLOT_PATH = "report/residuals.png"
MAX_DEPTH = 2
TARGET_COLUMN = "quality"