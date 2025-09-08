def print_multiplication_table(rows, cols):
  max_val = max([max(rows) * max(cols)] + rows + cols)
  width = len(str(max_val))
  header = ["".rjust(width)] + [str(c).rjust(width) for c in cols]
  
  print(" | ".join(header))
  print("-" * (len(" | ".join(header))))
  
  for r in rows:
    row_values = [str(r * c).rjust(width) for c in cols]
    print(str(r).rjust(width) + " | " + " | ".join(row_values))

rows = [2,3]
cols = [-11,1,2]
print_multiplication_table(rows, cols)