# Write your Day 4 user profile dictionary generator here

def generate_profile():
    # 1. Ask the user for name, age, and city
    # (Hint: use input() three times)
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    city = input("Enter your city: ")
    
    # 2. Create a dictionary with those inputs
    data = {"name": name, "age":age, "city": city}
    
    # 3. Print the full dictionary
    print(data)
    
    # 4. Print just the city
    print(data["city"])
    print(data.get("city"))

if __name__ == "__main__":
    generate_profile()
