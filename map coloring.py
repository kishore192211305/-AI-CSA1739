from itertools import product
from copy import deepcopy

def is_consistent(country, color, assignment, neighbors):
    for neighbor in neighbors[country]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

def backtrack(assignment, countries, colors, neighbors):
    if len(assignment) == len(countries):
        return assignment  # All countries are assigned a color

    unassigned_country = next(country for country in countries if country not in assignment)

    for color in colors:
        if is_consistent(unassigned_country, color, assignment, neighbors):
            new_assignment = deepcopy(assignment)
            new_assignment[unassigned_country] = color
            result = backtrack(new_assignment, countries, colors, neighbors)
            if result is not None:
                return result
    return None

def main():
    countries = input("Enter the countries (space-separated): ").split()
    neighbors = {}
    print("Enter the neighbors for each country:")
    for country in countries:
        neighbors[country] = input(f"Neighbors of {country} (space-separated): ").split()
    colors = input("Enter the colors (space-separated): ").split()
    assignment = {}

    solution = backtrack(assignment, countries, colors, neighbors)
    if solution:
        print("Map Coloring Solution:")
        for country, color in solution.items():
            print(f"{country}: {color}")
    else:
        print("No solution found.")

main()
