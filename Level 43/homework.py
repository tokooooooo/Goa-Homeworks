def count_items(item_list, item):
    
    return item_list.count(item)

items = ["apple", "banana", "cherry", "apple", "date", "banana", "apple"]
item_to_count = "apple"

count = count_items(items, item_to_count)
print("The item '{item_to_count}' occurs {count} times in the list.")
