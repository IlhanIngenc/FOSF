import numpy as np
from scipy.optimize import linprog


def format_constraints(lhs_list, rhs_list):
    """
    Convert lists of constraints into a format compatible with optimization solvers.
    This function takes the left-hand side (LHS) coefficients and the right-hand side (RHS)
    bounds and returns them as NumPy arrays, ready to be used in solvers like linprog.

    :param lhs_list: List of LHS constraint coefficients (A_ub matrix for linprog).
    :param rhs_list: List of RHS values (b_ub vector for linprog).
    :return: Tuple of NumPy arrays (A_ub, b_ub) for solver compatibility.
    """
    A_ub = np.array(lhs_list)
    b_ub = np.array(rhs_list)
    return A_ub, b_ub


def check_solution_status(result):
    """
    Check the result status from the optimization solver.
    This function prints detailed information about the optimization result,
    including whether the solution was successful or not, and raises an error if failed.

    :param result: The result object returned by the optimization solver.
    """
    if result.success:
        print("Optimization succeeded.")
        print(f"Optimal solution found: {result.x}")
    else:
        print(f"Optimization failed. Status: {result.status}")
        print(f"Message: {result.message}")
        raise ValueError("Optimization failed to find a feasible solution.")
