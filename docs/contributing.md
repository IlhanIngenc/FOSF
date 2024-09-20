# Contributing to FOSF

## How to Contribute

We welcome contributions to the Flexible Optimization Solution Framework (FOSF). Here’s how you can get started:

1. **Fork the Repository**: 
   - Fork the repository on GitHub to your own account.

2. **Clone the Repo**: 
   - Clone the forked repository to your local machine:
   ```bash
   git clone https://github.com/ilhaningenc/fosf.git
   cd fosf

3. **Create a Feature Branch:**
   - Create a new branch for the feature or fix you are working on:
   ```bash
    git checkout -b feature/new-feature

4. **Make Changes:**
   - Add your feature or fix and commit the changes.
   - Follow PEP-8 guidelines for Python code.
   - Write tests for any new functionality.
   - Submit a Pull Request (PR):
   - Once your changes are ready, submit a pull request to the main repository.

## Coding Standards
   1. Ensure all code follows PEP-8 standards.
   2. Write clear and concise comments.
   3. Test your code thoroughly before submitting a pull request.

## Adding New Optimization Models
- To add new optimization models, create a new class that inherits from OptimizationModel and implement the following methods:
   1. set_objective()
   2. add_constraints()
   3. solve()

### We look forward to your contributions and feedback!