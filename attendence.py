from collections import Counter

def most_attended_subject(attendance):
    # Count the frequency of each subject initial
    subject_count = Counter(attendance)
    
    # Find the subject with the maximum attendance
    most_attended = max(subject_count, key=subject_count.get)
    
    return most_attended

# Example input
attendance = [
    'M', 'C', 'P', 'M', 'E', 'M', 'D', 'M', 'P', 'C', 
    'M', 'M', 'M', 'E', 'P', 'M', 'C', 'M', 'P', 'D',
    'M', 'C', 'M', 'E', 'P', 'D', 'M', 'P', 'M', 'C',
    'M', 'E', 'P', 'D', 'M', 'M', 'M', 'M', 'M', 'C',
    'P', 'M', 'E', 'M', 'D', 'M', 'C', 'M', 'P', 'M',
    'M', 'M', 'E', 'P', 'M', 'D', 'M', 'P', 'C', 'M',
    'E', 'M', 'D', 'M', 'P', 'M', 'M', 'C', 'M', 'P',
    'M', 'E', 'D', 'M', 'P', 'C', 'M', 'M', 'M', 'M',
    'M', 'E', 'P', 'M', 'C', 'M', 'M', 'P', 'D', 'M',
    'E', 'M', 'P', 'C', 'M', 'M', 'M', 'M', 'M', 'M'
]

# Find and print the most attended subject
print(most_attended_subject(attendance))
//////////////////////////////////////////////////////////////////////////////////
# input code
from collections import Counter

def most_attended_subject(attendance):
    # Count the frequency of each subject initial
    subject_count = Counter(attendance)
    
    # Find the subject with the maximum attendance
    most_attended = max(subject_count, key=subject_count.get)
    
    return most_attended

# Input: Ask the user to enter attendance as a space-separated string
attendance = input("Enter the attendance for 100 days (space-separated initials M, C, P, D, E): ").split()

# Ensure the input is valid
if len(attendance) != 100 or any(subj not in {'M', 'C', 'P', 'D', 'E'} for subj in attendance):
    print("Invalid input. Please enter exactly 100 valid subject initials (M, C, P, D, E).")
else:
    # Find and print the most attended subject
    print("The subject attended the most is:", most_attended_subject(attendance))
    
///////////////////////////////////////////////////////////////

from collections import Counter

def most_attended_subject(attendance):
    # Count the frequency of each subject initial
    subject_count = Counter(attendance)
    
    # Find the subject with the maximum attendance
    most_attended = max(subject_count, key=subject_count.get)
    
    return most_attended

# Input: Prompt the user to enter attendance for 100 days one by one
attendance = []
print("Enter the subject initial for each of the 100 days (M, C, P, D, E):")

for i in range(1, 101):
    while True:
        subject = input(f"Day {i}: ").strip().upper()
        if subject in {'M', 'C', 'P', 'D', 'E'}:
            attendance.append(subject)
            break
        else:
            print("Invalid input. Please enter one of M, C, P, D, E.")

# Find and print the most attended subject
print("The subject attended the most is:", most_attended_subject(attendance))

    

