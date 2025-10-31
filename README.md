# Lab 5: Static Code Analysis

## Objective Summary

This lab focused on enhancing Python code quality, security, and style by utilizing industry-standard static analysis tools (Pylint, Flake8, and Bandit) to detect and rectify common programming issues in the `inventory_system.py` file. The analysis and fixes were performed to improve the code's robustness, security, and maintainability.

---

## Known Issue Table

The following table documents the issues identified in the original `inventory_system.py` by the static analysis tools and the approach taken to fix them in the final `cleaned_inventory_system.py`.

| Issue | Type | Line(s) | Description | Fix Approach |
| :--- | :--- | :--- | :--- | :--- |
| **Mutable default argument** | Bug | 8 | `logs = []` shared across calls, causing unexpected data persistence. | Changed default to `None` and initialized inside the function. |
| **Bare except:** | Code Smell | 22 | Catches all exceptions, hides real errors. | Replaced with specific exceptions (`KeyError`, `TypeError`) and added logging. |
| **Insecure eval() usage** | Security | 74 | Executes arbitrary code, creates major security vulnerability. | Removed `eval()` completely from the program. |
| **File not closed properly** | Bug | 33, 39 | Files were opened without using a context manager (`with open`). | Replaced with `with open(...)` to ensure automatic file closure. |
| **Line too long (E501)** | Style | 21 | Line exceeds 79 characters as per PEP8 standards. | Broke line into multiple shorter lines for readability. |
| **Missing module docstring** | Style | 1 | No top-level description of file purpose. | Added "Inventory Management System - Static Analysis Clean Version" as docstring. |
| **Use of global** | Code Smell | 55 | Global variable access discouraged by Pylint. | Justified and documented since it's needed for shared inventory data. |

---

## Reflection (Sample Answers - **VERIFY AND ADJUST**)

### 1. Which issues were the easiest to fix, and which were the hardest? Why?

* **Easiest:** The style issues reported by Flake8, particularly the **Line too long (E501)** and **Missing module docstring**, were the easiest. They were mechanical fixes requiring no change to the program's logic.
* **Hardest:** The hardest issue was the **Mutable default argument** at line 8. It required knowledge of Python's function execution model to understand *why* `logs=[]` was a bug, and then correctly refactoring the function signature and internal initialization.

### 2. Did the static analysis tools report any false positives? If so, describe one example.

* Yes, a potential false positive/justified usage was the **Use of global** reported by Pylint (line 55). While Pylint rightly flags global variable use as a code smell, for this small, self-contained `inventory_system.py` program, using a global dictionary was the simplest and clearest way to manage the single state of the inventory data across all functions. No complex class structure was required.

### 3. How would you integrate static analysis tools into your actual software development workflow?

I would integrate static analysis at two key stages:

* **Local Development (Pre-Commit):** Use a tool like `pre-commit` to run **Flake8** and low-severity **Pylint** checks before a commit is created. This ensures style compliance and catches obvious errors immediately, keeping the repository clean.
* **Continuous Integration (CI):** Configure the CI pipeline (e.g., in GitHub Actions) to run high-severity **Pylint** and all **Bandit** checks on every pull request. The build should **fail** if any high-severity bugs or security vulnerabilities (like the **Insecure eval() usage**) are introduced.

### 4. What tangible improvements did you observe in the code quality, readability, or potential robustness after applying the fixes?

The improvements were significant:

* **Robustness:** Fixing the **Mutable default argument** eliminated a hidden data-persistence bug, and changing the **Bare except:** to specific exceptions (like `KeyError`) ensures that unexpected errors are not suppressed, making the program more reliable.
* **Security:** Removing the **Insecure eval() usage** completely patched a critical vulnerability, making the program significantly safer.
* **Readability:** Adhering to PEP 8 standards by fixing the **Line too long (E501)** and adding a **Missing module docstring** made the entire file easier to understand and navigate.

---

Remember to commit and push all 6 required files, including this `readme.md`, to your GitHub repository before submitting.

Do you have any questions about the submission process or the required file structure?
