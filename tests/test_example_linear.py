import unittest
from src.models.linear_model import LinearOptimizationModel


class TestExampleLinear(unittest.TestCase):

    def test_example_solution(self):
        model = LinearOptimizationModel()
        model.set_objective([-2, -3])
        model.add_constraints([1, 0], 5)
        model.add_constraints([0, 1], 5)
        model.add_constraints([1, 1], 8)
        solution = model.solve()
        self.assertAlmostEqual(solution[0], 3, delta=0.1)
        self.assertAlmostEqual(solution[1], 5, delta=0.1)

if __name__ == '__main__':
    unittest.main()
