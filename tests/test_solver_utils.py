import unittest
import numpy as np
from src.utils.solver_utils import format_constraints, check_solution_status
from scipy.optimize import OptimizeResult


class TestSolverUtils(unittest.TestCase):

    def test_format_constraints(self):
        lhs = [[1, 0], [0, 1]]
        rhs = [5, 10]
        A_ub, b_ub = format_constraints(lhs, rhs)
        np.testing.assert_array_equal(A_ub, np.array(lhs))
        np.testing.assert_array_equal(b_ub, np.array(rhs))

    def test_check_solution_status_success(self):
        result = OptimizeResult(success=True, x=[1, 2])
        check_solution_status(result)  # Should print success message

    def test_check_solution_status_failure(self):
        result = OptimizeResult(success=False, status=2, message="Infeasible")

        with self.assertRaises(ValueError):
            check_solution_status(result)


if __name__ == '__main__':
    unittest.main()
