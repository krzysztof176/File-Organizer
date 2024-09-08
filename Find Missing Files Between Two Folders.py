import os

def find_difference(array1, array2):
    # Convert lists to sets to find the difference
    set1 = set(array1)
    set2 = set(array2)
    
    # Find the difference: elements in array1 but not in array2
    difference = list(set1 - set2)
    
    return difference

def get_all_filenames(folder_path):
    filenames = []
    # Walk through the directory tree
    for root, directories, files in os.walk(folder_path):
        for filename in files:
            filenames.append(filename)
    return filenames

# Example usage
goldPath = r"{}".format(input("Where are the gold files located?\n"))
organizedPath = r"{}".format(input("Where are the organized files located?\n"))

goldList = get_all_filenames(goldPath)
organizedList = get_all_filenames(organizedPath)

difference = find_difference(goldList, organizedList)

for filename in difference:
    print(filename)