# Create a tuple containing marks of 5 subjects
marks = (85, 92, 78, 88, 90)

# Display the marks
print("Marks in 5 subjects:", marks)

# Calculate total, highest, lowest, and average marks using tuple functions
total_marks = sum(marks)
highest_mark = max(marks)
lowest_mark = min(marks)
average_marks = total_marks / len(marks)

# Display results
print("\n--- Results ---")
print("Total Marks:", total_marks)
print("Highest Marks:", highest_mark)
print("Lowest Marks:", lowest_mark)
print("Average Marks:", round(average_marks, 2))

# Convert tuple to list to modify marks
marks_list = list(marks)
print("\nTuple converted to List:", marks_list)

# Modify one of the subject marks (say, change 3rd subject mark)
marks_list[2] = 82
print("Updated List:", marks_list)

# Convert the list back to tuple
marks = tuple(marks_list)
print("Modified Tuple:", marks)
