xfile = open('test_file.txt', 'r')
for line in xfile:
    if line == "wubba lubba dub dub":
        line = "quarta linea"
    else:
        line = "wubba lubba dub dub"
    
    print(line)