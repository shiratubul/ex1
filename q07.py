import csv
from collections import Counter
from bidi.algorithm import get_display

file_path = r"C:\Users\USER\Downloads\street.csv"

# קריאה של שמות הרחובות
street_names = []
with open(file_path, encoding="windows-1255") as f:
    reader = csv.DictReader(f)
    for row in reader:
        name = row["street_name"].strip()
        if name:
            street_names.append(name)

# ספירה
counter = Counter(street_names)

# 10 הנפוצים ביותר
print(get_display("עשרת שמות הרחובות הנפוצים ביותר בישראל:\n"))
for name, count in counter.most_common(10):
    print(get_display(f"{name}: {count}"))
