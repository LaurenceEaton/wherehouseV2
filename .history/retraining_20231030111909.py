# train_model.py
from stockprediction import WarehousePredictor

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

    # Print the updated model parameters
    print("Optimised coefficients after retraining:", warehouse_predictor.coefficients)
    final_cost = warehouse_predictor.compute_cost()
    print("Final cost after retraining:", final_cost)

if __name__ == "__main__":
    main()
