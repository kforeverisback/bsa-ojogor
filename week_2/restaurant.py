import os
import csv


"""
All arguments which we probably want to convert it to a cli arg
"""

# Name of the file, we should really put this as an arg
csv_file_name = 'Food_Est_Scores_really_small.csv'
# Score threshold
score_threshold = 90
max_selection = 5
our_zipcode = 78666

def sort_func(key):
    #return abs(int(key[1]) - our_zipcode)
    return int(key[1])

# Reading from the file
with open(csv_file_name) as cf:
    csv_reader = csv.reader(cf, delimiter=',')
    # This method is better, but we'll use the pop() method just for sake of simpliciy
    # header = next(csv_reader)
    # Save the reader output as list
    all_rows = list(csv_reader)

# Popping the Header only
header = all_rows.pop(0)

# In place sorting
all_rows.sort(key=sort_func)
# Achieving the same with three different method
# all_rows.sort(key=lambda elem: int(elem[1]))
# Methods below doesn't sort in-place 
# sorted_rows = sorted(all_rows, key=lambda elem: int(elem[1]))
# sorted_rows = sorted(all_rows, key=sort_func)
print('\t'.join(header))
# i = 10
# for r in all_rows:
#     print('\t'.join(r))
#     if i == 0:
#         break
#     i-=1
selected = []
for row in all_rows:
    if int(row[3]) > score_threshold:
        row[0] = row[0][0:25]
        #selected+=[i[0:15 if len(i) > 15 else len(i)] for i in row]
        selected+=[row]
        if len(selected) >= max_selection:
            break
selected.sort( key=lambda s:int(s[3]), reverse=True)
for row in selected:
    print(f'{row[0]}\t{row[1]}\t{row[3]}')
#print(f'Read CSV file {csv_file_name}, {type(all_rows)}')
