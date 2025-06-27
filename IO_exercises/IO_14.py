# Exercise 14: Tabular Output from Lists

names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]
print(f"{"names":<13}{"scores"}")
print("-"*20)
for i,j in zip(names,scores):
    print(f"{i:<15}{j}")
