# Write your Day 3 inventory manager script here

def manage_inventory():
    # 1. Create a variable called inventory that holds a list of 3 starting items
    inventory = ["apple", "banana", "orange"]
    
    # 2. Print the initial inventory
    print(inventory)
    
    # 3. Use .append() to add a new item
    inventory.append("grape")
    
    # 4. Use .remove() to remove one of the original items
    inventory.remove("banana")
    
    # 5. Print the updated inventory
    print(inventory)
    
    # 6. Print the total number of items using len()
    print("Total items: ", len(inventory))

if __name__ == "__main__":
    manage_inventory()
