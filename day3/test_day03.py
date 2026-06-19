import subprocess
import sys

def run_tests():
    print("Running Tests for Day 3 Inventory Manager...")
    print("-" * 50)
    
    process = subprocess.run(
        [sys.executable, "day03_inventory.py"],
        text=True,
        capture_output=True
    )
    
    output = process.stdout.lower()
    passed_tests = 0
    total_tests = 4
    
    # Test 1: Check if there is an initial inventory print
    if "[" in output and "]" in output:
        print("[PASS] Test 1: Found list printed in output.")
        passed_tests += 1
    else:
        print("[FAIL] Test 1: Could not find a list printed in output.")
        
    # Test 2 & 3 are hard to check exactly without knowing the user's item names,
    # so we will check for general list structural changes by seeing multiple lists printed.
    lists_printed = output.count("[")
    if lists_printed >= 2:
        print("[PASS] Test 2: Found updated list printed in output.")
        passed_tests += 1
    else:
        print("[FAIL] Test 2: Could not find an updated list printed in output.")
        
    # Test 3: Check for length print
    if "3" in output or "three" in output:
        # Assuming the final list has 3 items (3 initial + 1 append - 1 remove = 3)
        print("[PASS] Test 3: Found the correct length (3) printed in output.")
        passed_tests += 1
    else:
        print("[FAIL] Test 3: Could not find the correct length (3) printed.")
        
    # Test 4: Verify no errors
    if process.returncode == 0:
        print("[PASS] Test 4: Script executed without errors.")
        passed_tests += 1
    else:
        print(f"[FAIL] Test 4: Script threw an error:\n{process.stderr}")

    print("-" * 50)
    print(f"Results: {passed_tests}/{total_tests} Tests Passed.")

if __name__ == "__main__":
    run_tests()
