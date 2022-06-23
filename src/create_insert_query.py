query = "INSERT INTO estates (info)\nVALUES"

file = open('estates.json', 'r')
Lines = file.readlines()
file.close()
num_lines = len(Lines)

for i in range(num_lines):
    if i == 0 or i == num_lines-1:
        continue
    elif i == num_lines-2:
        query += '(\'' + Lines[i].rstrip('\n').rstrip(',') + '\');'
    else:
        query += '(\'' + Lines[i].rstrip('\n').rstrip(',') + '\'),\n'

file = open('../sql_queries/insert_query.sql', 'w')
file.write(query)
file.close()