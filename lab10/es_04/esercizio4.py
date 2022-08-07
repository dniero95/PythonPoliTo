

try:
    fname = open("info.txt", "r")
    #print(fname.read())

    

    service_type = []
    total_price = 0
    for line in fname:
        
        fields = line.split(";")
        if not fields[1] in service_type:
            service_type.append(fields[1])
        # print(fields)
        # total_price += float(fields[2])

    fname.close()



    for service in service_type:
        fname = open("info.txt", "r")
        
        for line in fname:
            fields = line.split(";")
        
            if service in fields:
                total_price += float(fields[2])
        
        fname.close()
        
        print(service, "Prezzo servizio: ", total_price)
        total_price = 0
except:
    print("file non presente")

    


#print(service_type)