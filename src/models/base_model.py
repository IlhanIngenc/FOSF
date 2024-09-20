# src/models/base_model.py

from abc import ABC, abstractmethod


class OptimizationModel(ABC):
    """
    Abstract base class for different optimization models in FOSF.
    Each specific optimization model should inherit from this class and
    implement the required methods.
    """

    @abstractmethod
    def set_objective(self, coefficients):
        """
        Set the objective function for the optimization model.
        For linear optimization, this would be the coefficients of the objective function.
        For nonlinear optimization, this could be a function.
        """
        pass

    @abstractmethod
    def add_constraints(self, lhs, rhs):
        """
        Add constraints to the optimization model.
        Constraints are typically represented by a left-hand side (lhs)
        matrix and a right-hand side (rhs) vector for linear optimization.
        """
        pass

    @abstractmethod
    def solve(self):
        """
        Solve the optimization problem.
        Each model will have a different solving mechanism.
        """
        pass

    def report_results(self, solution):
        """
        A common method to report the results of the optimization.
        This can be overridden by specific models if necessary.
        """
        print(f"Optimal solution: {solution}")
