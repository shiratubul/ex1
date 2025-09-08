def multiplication_table(rows, cols):
    print(" |" + "|".join(str(c) for c in cols))
    
    for r in rows:
        new_row = [str(r)]
        for c in cols:
            new_row.append(str(r * c))
        print("|".join(new_row))

rows = [1,2, 3]
cols = [1,2, 3, 4]
multiplication_table(rows, cols)
