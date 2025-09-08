# פונקציה שמחזירה את כל הקבוצות החלקיות של רשימה
def subsets(lst):
    result = [[]]  # מתחילים עם הקבוצה הריקה
    for elem in lst:
        new_subsets = []
        for subset in result:
            new_subset = subset.copy()
            new_subset.append(elem)
            new_subsets.append(new_subset)
        result.extend(new_subsets)
    return result

# קריאת הקובץ והדפסת כל קבוצות המילים
filename = r"C:\Users\USER\Downloads\words.txt"

with open(filename, 'r', encoding='utf-8') as f:
    words = [line.strip() for line in f if line.strip()]  # רשימה של מילים

for subset in subsets(words):
    print(subset)
