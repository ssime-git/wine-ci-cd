# plotting.py
import seaborn as sns
import matplotlib.pyplot as plt
from config import FEATURE_IMPORTANCE_PLOT_PATH, RESIDUALS_PLOT_PATH
import numpy as np
import pandas as pd
import logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%m/%d/%Y %I:%M:%S %p'
)

def plot_feature_importance(regr, feature_names):
    importances = regr.feature_importances_
    feature_df = pd.DataFrame(list(zip(feature_names, importances)), columns=["feature", "importance"])
    feature_df = feature_df.sort_values(by='importance', ascending=False)
    
    sns.set(style="whitegrid")
    ax = sns.barplot(x="importance", y="feature", data=feature_df)
    ax.set_xlabel('Importance') 
    ax.set_ylabel('Feature')
    ax.set_title('Random forest feature importance')

    plt.tight_layout()
    plt.savefig(FEATURE_IMPORTANCE_PLOT_PATH, dpi=120) 
    plt.close()
    logging.info("Feature importance plotted")

def plot_residuals(X_test, y_test, regr):
    y_pred = regr.predict(X_test) + np.random.normal(0, 0.25, len(y_test))
    y_jitter = y_test + np.random.normal(0, 0.25, len(y_test))
    res_df = pd.DataFrame(list(zip(y_jitter, y_pred)), columns=["true", "pred"])
    
    ax = sns.scatterplot(x="true", y="pred", data=res_df)
    ax.set_aspect('equal')
    ax.set_xlabel('True wine quality') 
    ax.set_ylabel('Predicted wine quality')
    ax.set_title('Residuals')

    ax.plot([1, 10], [1, 10], 'black', linewidth=1)
    plt.ylim((2.5, 8.5))
    plt.xlim((2.5, 8.5))

    plt.tight_layout()
    plt.savefig(RESIDUALS_PLOT_PATH, dpi=120)
    plt.close()
    logging.info("Residuals plotted")