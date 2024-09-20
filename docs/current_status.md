# Flexible Optimization Solution Framework (FOSF)

## Current Version Overview

The **Flexible Optimization Solution Framework (FOSF)** is a tool for solving linear optimization problems using the `scipy.optimize.linprog` function. It provides a flexible structure where different optimization models can be implemented and used in various scenarios.

### Current Features

1. **Linear Optimization Model**:
   - This model allows for solving linear programming problems.
   - Uses the **'highs'** method from SciPy for solving optimization problems.
   - Supports setting objective functions and adding constraints to the model.

2. **Helper Functions**:
   - `format_constraints`: Formats the constraints to be used by the optimizer.
   - `check_solution_status`: Checks the status of the optimization result and prints detailed messages.

### Code Example

Here's an example of how to run a linear optimization:

```python
from src.models.linear_model import LinearOptimizationModel

# Create a linear optimization model
model = LinearOptimizationModel()

# Define the objective function for maximizing 2 * x1 + 3 * x2
model.set_objective([-2, -3])

# Add constraints (e.g., x1 <= 5, x2 <= 5, x1 + x2 <= 8)
model.add_constraints([1, 0], 5)  # x1 <= 5
model.add_constraints([0, 1], 5)  # x2 <= 5
model.add_constraints([1, 1], 8)  # x1 + x2 <= 8

# Solve the optimization problem
solution = model.solve()

# Report the results
model.report_results(solution)
