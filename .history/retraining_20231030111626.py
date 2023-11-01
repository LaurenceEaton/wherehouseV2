# train_model.py
from warehouse_predictor import WarehousePredictor

def main():
    # Create an instance of the WarehousePredictor class
    warehouse_predictor = WarehousePredictor()

    # Read and preprocess the updated data
    warehouse_predictor.read_data()
    warehouse_predictor.prepare_inputs_outputs()

    # Specify hyperparameters for retraining
    learning_rate = 0.01  # You can adjust this if needed
    iterations = 1000  # You can adjust this as well

    # Retrain the model
    warehouse_predictor.gradient_descent(learning_rate, iterations)

    # Save the updated model parameters
    warehouse_predictor.save_model("model_parameters.json")

if __name__ == "__main__":
    main()
