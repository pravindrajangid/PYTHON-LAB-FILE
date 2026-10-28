
# Function to remove negative values from each row
def filter_negative(matrix):
    return [list(filter(lambda x: x >= 0, row)) for row in matrix]


# Function to square every element of the matrix
def square_matrix(matrix):
    return [list(map(lambda x: x * x, row)) for row in matrix]


# Function to sort each row in ascending order
def sort_rows(matrix):
    return [sorted(row) for row in matrix]


# Function to sort rows according to their sum
def sort_by_sum(matrix):
    return sorted(matrix, key=lambda row: sum(row))


# Function to convert rows into tuples
def convert_to_tuples(matrix):
    return [tuple(row) for row in matrix]


# Main program
matrix = [
    [4, -4, 5, 1],
    [-4, 8, 5, -1],
    [9, 7, -6, 6]
]


print("Original Matrix:")
print(matrix)


# Step 1: Remove negative values
filtered = filter_negative(matrix)
print("\nAfter Filtering Negative Values:")
print(filtered)


# Step 2: Square the remaining values
squared = square_matrix(filtered)
print("\nAfter Squaring Elements:")
print(squared)


# Step 3: Sort each row
sorted_matrix = sort_rows(squared)
print("\nRows Sorted in Ascending Order:")
print(sorted_matrix)


# Step 4: Sort rows according to their sum
final_matrix = sort_by_sum(sorted_matrix)
print("\nRows Sorted According to Their Sum:")
print(final_matrix)


# Step 5: Convert rows into tuples
tuple_matrix = convert_to_tuples(final_matrix)
print("\nFinal Matrix as Tuples:")
print(tuple_matrix)
