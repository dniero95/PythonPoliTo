from tabulate import tabulate

if __name__ == '__main__':
    rows = [['Good morning','Buon giorno','Guten Morgen'],
                 ['It is a pleasure to meet you','È un piacere incontrarti','Es ist mir eine Freude Sie zu treffen'],
                 ['Please call me tomorrow','Per favore, chiamami domani','Bitte rufen Sie mich morgen an'],
                 ['Good morning','Buon giorno','Guten Morgen'],
                 ['Have a nice day!','Buona giornata!','Einen schönen Tag noch!']]

    print('Elenco Saluti')
    header = ['Inglese' ,'Italiano', 'Tedesco']
    print(tabulate(rows, headers=header))