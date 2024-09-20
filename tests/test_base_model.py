import unittest
from abc import ABCMeta, abstractmethod
from src.models.base_model import OptimizationModel


class TestBaseModel(unittest.TestCase):
    def test_cannot_instantiate_abstract_class(self):
        with self.assertRaises(TypeError):
            OptimizationModel()

    # Test, if derived classes implement required methods
    def test_required_methods(self):
        class MockModel(OptimizationModel):
            def set_objective(self):
                pass

            def add_constraints(self):
                pass

            def solve(self):
                return [0, 0]

        model = MockModel()
        self.assertTrue(hasattr(model, 'set_objective'))
        self.assertTrue(hasattr(model, 'add_constraints'))
        self.assertTrue(hasattr(model, 'solve'))


if __name__ == '__main__':
    unittest.main()
