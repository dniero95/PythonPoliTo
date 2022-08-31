import argparse as args
from access import Access
if __name__ == '__main__':
    # handle the argument from CLI
    # for reference check https://www.youtube.com/watch?v=J51vxXAWigI
    parser = args.ArgumentParser(description='script that analize anomalies in the access of a list of user taken from a access.txt file')
    parser.add_argument('users', type=str, nargs='+', help='Enter users as: name1 name2 name3')
    parsed_args = parser.parse_args()
    print(parsed_args.users)
    users = parsed_args.users
    # users = ['verdi', 'rossi', 'bianchi', 'gialli']
    # read data from file access.txt
    file_name = 'access.txt'
    Access.instantiate_from_txt(file_name)

    # print anomalies
    print(f'Anomalie rilevate:\n{Access.format_anomalies(users)}')
    print(f'Numero totale di anomalie: {Access.number_of_anomalies(users)}')
    print(f'Utente con il maggior numero di anomalie: {Access.user_max_number_of_anomalies(users)}')



