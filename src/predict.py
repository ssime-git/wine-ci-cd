import joblib
import pandas as pd
from config import MODEL_PATH

# Function to load the pre-trained model
def load_model(model_path):
    return joblib.load(model_path)

# Function to run a prediction
def run_prediction(model, input_data):
    return model.predict(input_data)

def main():
    # Load the model
    model = load_model(MODEL_PATH)
    
    # Example input data (replace this with actual data)
    # Ensure the input data format is consistent with the model's training data
    input_data = pd.DataFrame(
        data=[[7.4, 0.7, 0, 1.9, 0.076, 11, 34, 0.9978, 3.51, 0.56, 9.4]], 
        columns=['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar', 
                 'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density', 
                 'pH', 'sulphates', 'alcohol']
    )
    
    # Run the prediction
    prediction = run_prediction(model, input_data)
    
    # Output the prediction
    print(f"The predicted quality is: {prediction}")

if __name__ == '__main__':
    main()