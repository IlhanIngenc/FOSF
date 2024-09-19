import sys
import os
from src.models.linear_model import LinearOptimizationModel
from src.utils.solver_utils import format_constraints, check_solution_status

# Add the 'src' folder to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), './src')))


def choose_model(model_type):
    """
    Allows the user to choose the type of optimization model to use.
    :param model_type: A string specifying the type of model ('linear' or others in the future).
    :return: An instance of the selected optimization model.
    """
    if model_type == 'linear':
        return LinearOptimizationModel()
    else:
        raise ValueError(f"Model type '{model_type}' is not supported yet.")


def run_optimization():
    """
    Main function to run the optimization process. This function serves as the central controller
    of the FOSF framework, guiding the user through setting up an optimization model,
    defining its objectives and constraints, and solving it.
    """

    # Allow the user to choose an optimization model
    model_type = input("Enter the optimization model type (e.g., 'linear'): ").lower()

    # Instantiate the selected optimization model
    model = choose_model(model_type)

    # Set up the objective function (example: maximize 2 * x1 + 3 * x2)
    print("Defining the objective function...")
    model.set_objective([-2, -3])  # Example for maximizing 2 * x1 + 3 * x2

    # Define constraints (example: x1 <= 5, x2 <= 5, x1 + x2 <= 8)
    print("Adding constraints...")
    model.add_constraints([1, 0], 5)  # x1 <= 5
    model.add_constraints([0, 1], 5)  # x2 <= 5
    model.add_constraints([1, 1], 8)  # x1 + x2 <= 8

    # Solve the optimization problem
    print("Solving the optimization problem...")
    solution = model.solve()

    # Output the solution
    model.report_results(solution)


if __name__ == "__main__":
    run_optimization()
