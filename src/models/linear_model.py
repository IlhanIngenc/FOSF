import sys
import os
from scipy.optimize import linprog
from src.utils.solver_utils import format_constraints, check_solution_status
from src.models.base_model import OptimizationModel

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))


class LinearOptimizationModel(OptimizationModel):
    """
    A class representing a linear optimization model, commonly used in
    economic decision-making for optimizing resources and maximizing profits.
    """

    def __init__(self):
        self.objective = None
        self.constraints = {'lhs': [], 'rhs': []}

    def set_objective(self, coefficients):
        """
        Set the coefficients of the objective function.
        In a business context, this typically represents the goal to be maximized
        or minimized, such as profit or cost.

        :param coefficients: List of coefficients for the objective function (e.g., profit).
        """
        self.objective = coefficients

    def add_constraints(self, lhs, rhs):
        """
        Add a constraint to the model.
        Constraints typically represent resource limitations (e.g., labor, materials)
        that must be adhered to when making economic decisions.

        :param lhs: Coefficients representing resource usage for each variable.
        :param rhs: The limit of the resource available (e.g., total hours or budget).
        """
        self.constraints['lhs'].append(lhs)
        self.constraints['rhs'].append(rhs)

    def solve(self):
        """
        Solve the linear optimization problem, which aims to optimize the allocation
        of limited resources to achieve the best economic outcome, such as maximizing
        profit or minimizing cost.

        :return: The optimal solution (values of decision variables).
        """

        print(f"Objective function: {self.objective}")
        print(f"Constraints LHS: {self.constraints['lhs']}")
        print(f"Constraints RHS: {self.constraints['rhs']}")

        A_ub, b_ub = format_constraints(self.constraints['lhs'], self.constraints['rhs'])

        # Solve the optimization problem using the 'highs' method
        result = linprog(c=self.objective, A_ub=A_ub, b_ub=b_ub, method='highs')

        print(f"Optimization status: {result.status}")
        print(f"Optimization message: {result.message}")

        check_solution_status(result)

        if result.success:
            return result.x  # Returns the optimal solution
        else:
            raise ValueError("Linear optimization failed to find a solution.")
