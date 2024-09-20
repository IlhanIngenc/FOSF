# FOSF Usage Guide

## How to Use FOSF

1. **Running the Optimization**:
   - To run an optimization, call the `run_optimization()` function in `fosf.py`.
   - The user will be prompted to choose the optimization model type (currently supports 'linear').
   - After choosing the model, the objective function and constraints will be automatically set (in this version).

2. **Extending Objective Functions**:
   - You can modify the `set_objective()` method to define new objective functions for different use cases.

3. **Extending Constraints**:
   - To add new constraints, use the `add_constraints(lhs, rhs)` method, where:
     - `lhs` is a list of coefficients for the decision variables.
     - `rhs` is the right-hand side limit for the constraint.

## Adding More Models

To extend the framework with more optimization models (e.g., nonlinear or mixed-integer programming), implement new classes that inherit from `OptimizationModel` and override the necessary methods:

- `set_objective()`
- `add_constraints()`
- `solve()`

You can build advanced optimization models while reusing the core structure provided by FOSF.

## Next Steps

Install Dependencies: Make sure you have installed all the required dependencies by following the installation guide.
- **Test the Framework:** Run the examples provided to see how the framework solves optimization problems.
- **Extend the Framework:** Implement new optimization models or add more advanced features such as nonlinear programming.


## Troubleshooting

If you encounter any issues while running the framework, please refer to the following steps:

1. Check the installation: Make sure all dependencies are installed and the Python environment is activated.
2. Review the code: Verify that the objective function and constraints are set correctly.
3. Debugging: Use the built-in debugging outputs from the solve() method to analyze the status and message of the solver.

For more advanced troubleshooting, consult the Contributing Guide if you want to submit a bug fix or contribute to the project.


## Conclusion
This guide provides the basic steps for using and extending the Flexible Optimization Solution Framework (FOSF). Feel free to explore the examples and documentation to get the most out of the framework.

## Example Usage

```python
from src.models.linear_model import LinearOptimizationModel

# Define a linear optimization model
model = LinearOptimizationModel()

# Set the objective function
model.set_objective([-2, -3])

# Add constraints
model.add_constraints([1, 0], 5)  # x1 <= 5
model.add_constraints([0, 1], 5)  # x2 <= 5
model.add_constraints([1, 1], 8)  # x1 + x2 <= 8

# Solve the problem
solution = model.solve()

# Print the results
model.report_results(solution)

