import subprocess
import sys
import random

def run_tests():
    print("Running 20 Random Test Cases for Day 4...")
    print("-" * 50)
    
    names = ["Alice", "Bob", "Charlie", "Diana", "Eve", "Frank", "Grace", "Heidi", "Ivan", "Judy"]
    cities = ["New York", "London", "Tokyo", "Paris", "Berlin", "Sydney", "Toronto", "Dubai", "Mumbai", "Cairo"]
    
    passed_count = 0
    
    for i in range(1, 21):
        name = random.choice(names)
        age = str(random.randint(18, 99))
        city = random.choice(cities)
        
        input_str = f"{name}\n{age}\n{city}\n"
        
        process = subprocess.run(
            [sys.executable, "day04_profile.py"],
            input=input_str,
            text=True,
            capture_output=True
        )
        
        output = process.stdout
        
        # We expect the dictionary to contain the generated values, and the city to be printed
        if name in output and age in output and city in output:
            print(f"[PASS] Test {i} PASSED: Input ({name}, {age}, {city})")
            passed_count += 1
        else:
            print(f"[FAIL] Test {i} FAILED: Input ({name}, {age}, {city})")
            print(f"   Actual Output:\n{output.strip()}\n")

    print("-" * 50)
    print(f"Results: {passed_count}/20 Tests Passed.")

if __name__ == "__main__":
    run_tests()
