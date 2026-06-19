import subprocess
import sys
import random

def run_test(guess):
    input_str = f"{guess}\n"
    
    # Run the guessing game script
    process = subprocess.run(
        [sys.executable, "day02_guessing_game.py"],
        input=input_str,
        text=True,
        capture_output=True
    )
    
    output = process.stdout
    valid_responses = ["Too high! Try again.", "Too low! Try again.", "Congratulations! You guessed it!"]
    
    for response in valid_responses:
        if response in output:
            return True, response
            
    return False, output.strip()

print("Running 20 Random Test Cases for Day 2 Guessing Game...")
print("-" * 50)
passed_count = 0

for i in range(1, 21):
    # Generate a random guess between 1 and 100
    guess = random.randint(1, 100)
    passed, actual_output = run_test(guess)
    
    if passed:
        print(f"[PASS] Test {i} PASSED: Guess '{guess}' -> Output: '{actual_output}'")
        passed_count += 1
    else:
        print(f"[FAIL] Test {i} FAILED: Guess '{guess}'")
        print(f"   Actual Output:\n{actual_output}\n")

print("-" * 50)
print(f"Results: {passed_count}/20 Tests Passed.")
