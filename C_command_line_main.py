import argparse
import os
import pandas as pd
import logging
from C_RLUS import set_rho

def load_theta(data_path):
    try:
        data = pd.read_csv(data_path)
        theta = data['delay'].tolist()
        return theta
    except Exception as e:
        logging.error(f"Error loading data from {data_path}: {e}")
        exit(1)

def setup_logging(log_file):
    """Sets up the logging configuration."""
    logging.basicConfig(filename=log_file, level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run the RLUS algorithm.")
    parser.add_argument("--data_path", type=str, required=True, help="Path to the CSV data file.")
    parser.add_argument("--q", type=float, default=0.5, help="Quantile to estimate.")
    parser.add_argument("--delta_target", type=float, default=0.05, help="Target confidence level.")
    parser.add_argument("--epsilon_min", type=float, required=True, help="Minimum epsilon value.")
    parser.add_argument("--epsilon_max", type=float, required=True, help="Maximum epsilon value.")
    parser.add_argument("--b", type=int, default=1000, help="Number of bootstrap resamples.")
    parser.add_argument("--result_path", type=str, required=True, help="Path to save the results.")
    parser.add_argument("--result_file", type=str, required=True, help="File to save the results.")
    parser.add_argument("--log_file", type=str, default="application.log", help="File to log the operations.")

    args = parser.parse_args()

    # Setup logging
    setup_logging(args.log_file)

    theta = load_theta(args.data_path)
    epsilon_range = (args.epsilon_min, args.epsilon_max)

    # Compute the largest accepted rho value
    largest_accepted_rho = set_rho(args.q, args.delta_target, epsilon_range, theta, args.b)

    # Prepare the results to be saved
    result = {
        "epsilon_range": f"({epsilon_range[0]}, {epsilon_range[1]})",
        "largest_accepted_rho": largest_accepted_rho
    }
    df = pd.DataFrame([result])
    full_path = os.path.join(args.result_path, args.result_file)

    # Attempt to save the results and handle possible exceptions
    try:
        if os.path.isfile(full_path):
            df.to_csv(full_path, mode='a', header=False, index=False)
        else:
            df.to_csv(full_path, mode='w', header=True, index=False)
        logging.info(f"Results have been successfully saved to {full_path}")
        print(f"Results have been successfully saved to {full_path}")
    except Exception as e:
        logging.error(f"Failed to save results to {full_path}: {e}")
        exit(1)
