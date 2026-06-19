import subprocess
import sys

def run_test(num1, num2, operation, expected_output):
    input_str = f"{num1}\n{num2}\n{operation}\n"
    
    # Run the calculator script
    process = subprocess.run(
        [sys.executable, "day01_calculator.py"],
        input=input_str,
        text=True,
        capture_output=True
    )
    
    output = process.stdout
    # We check if the expected output is anywhere in the script's stdout
    if expected_output in output:
        return True, output.strip()
    else:
        return False, output.strip()

test_cases = [
    (10, 5, "+", "Output:  15.0"),
    (10, 5, "-", "Output:  5.0"),
    (10, 5, "*", "Output:  50.0"),
    (10, 5, "/", "Output:  2.0"),
    (10, 0, "/", "Error: Cannot divide by zero!"),
    (0, 5, "/", "Output:  0.0"),
    (-5, -5, "+", "Output:  -10.0"),
    (2.5, 2.5, "*", "Output:  6.25"),
    (10, 5, "unknown", "Invalid operation"),
    (100, 33, "-", "Output:  67.0")
]

print("Running 10 Test Cases for Day 1 Calculator...")
print("-" * 50)
passed_count = 0

for i, (num1, num2, op, expected) in enumerate(test_cases, 1):
    passed, actual_output = run_test(num1, num2, op, expected)
    if passed:
        print(f"[PASS] Test {i} PASSED: {num1} {op} {num2} -> expected '{expected}'")
        passed_count += 1
    else:
        print(f"[FAIL] Test {i} FAILED: {num1} {op} {num2}")
        print(f"   Expected to contain: {expected}")
        print(f"   Actual Output:\n{actual_output}\n")

print("-" * 50)
print(f"Results: {passed_count}/{len(test_cases)} Tests Passed.")
