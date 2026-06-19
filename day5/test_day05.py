import subprocess
import sys
import random

def run_tests():
    print("Running 20 Random Test Cases for Day 5...")
    print("-" * 50)
    
    passed_count = 0
    valid_inputs = ["1", "2", "invalid_str", "99"]
    
    for i in range(1, 21):
        # Generate a random sequence of choices, ending with an exit choice
        sequence_length = random.randint(0, 5)
        choices = [random.choice(valid_inputs) for _ in range(sequence_length)]
        
        # Pick an exit command randomly
        exit_cmd = random.choice(["3", "exit"])
        choices.append(exit_cmd)
        
        input_str = "\n".join(choices) + "\n"
        
        process = subprocess.run(
            [sys.executable, "day05_menu.py"],
            input=input_str,
            text=True,
            capture_output=True
        )
        
        output = process.stdout
        
        # Verify correctness
        test_passed = True
        for choice in choices:
            if choice == "1" and "Hello there!" not in output:
                test_passed = False
            elif choice == "2" and "It is time to learn Python!" not in output:
                test_passed = False
            elif choice in ["3", "exit"] and "Goodbye!" not in output:
                test_passed = False
            elif choice not in ["1", "2", "3", "exit"] and "Invalid choice" not in output:
                test_passed = False
                
        if test_passed:
            print(f"[PASS] Test {i} PASSED: Sequence {choices}")
            passed_count += 1
        else:
            print(f"[FAIL] Test {i} FAILED: Sequence {choices}")
            print(f"   Actual Output:\n{output.strip()}\n")

    print("-" * 50)
    print(f"Results: {passed_count}/20 Tests Passed.")

if __name__ == "__main__":
    run_tests()
