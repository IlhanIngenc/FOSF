import unittest
from src.models.linear_model import LinearOptimizationModel


class TestLinearModel(unittest.TestCase):

    def setUp(self):
        self.model = LinearOptimizationModel()

    def test_set_objective(self):
        self.model.set_objective([1, 2])
        self.assertEqual(self.model.objective, [1, 2])

    def test_add_constraints(self):
        self.model.add_constraints([1, 0], 5)
        self.assertEqual(self.model.constraints['lhs'], [[1, 0]])
        self.assertEqual(self.model.constraints['rhs'], [5])

    def test_solve_valid(self):
        self.model.set_objective([-2, -3])
        self.model.add_constraints([1, 0], 5)
        self.model.add_constraints([0, 1], 5)
        self.model.add_constraints([1, 1], 8)
        solution = self.model.solve()
        self.assertAlmostEqual(solution[0], 3, delta=0.1)
        self.assertAlmostEqual(solution[1], 5, delta=0.1)


if __name__ == '__main__':
    unittest.main()
