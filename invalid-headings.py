fname = raw_input('Enter file name: ')
if len(fname) == 0:
    fname = 'invalid headings report.txt'
    
with open(fname) as file, open("Invalid-Headings-Fixed.txt", "w") as file2:
    data=file.read().replace("\n ", " ")    

    for line in data:
        line = line.rstrip()
        if "k970" not in line:
            file2.write(line.strip() + "\n")    
        else:
            continue
