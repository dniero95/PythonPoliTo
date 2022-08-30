
from access import Access
if __name__ == '__main__':
    # read data from file access.txt
    file_name = 'access.txt'
    Access.instantiate_from_txt(file_name)

    users = ['rossi', 'bianchi', 'verdi']
    # print anomalies
    print(f'Anomalie rilevate:\n{Access.format_anomalies(users)}')
    print(f'Numero totale di anomalie: {Access.number_of_anomalies(users)}')
    print(f'Utente con il maggior numero di anomalie: {Access.max_number_of_anomalies(users)}')


#     todo: implement argparse
