import unittest
from src.fosf import run_optimization
from unittest.mock import patch


class TestFOSF(unittest.TestCase):

    @patch('builtins.input', side_effect=['linear'])
    @patch('src.models.linear_model.LinearOptimizationModel.solve', return_value=[3, 5])
    def test_run_optimization(self, mock_solve, mock_input):
        run_optimization()
        mock_solve.assert_called_once()

if __name__ == '__main__':
    unittest.main()
