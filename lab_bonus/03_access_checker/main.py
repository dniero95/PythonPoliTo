import argparse as args
from access import Access
if __name__ == '__main__':
    # handle the argument from CLI
    parser = args.ArgumentParser(description='list of users name')
    parser.add_argument('users', metavar='users', type=str, nargs='+', help='Enter users as: name1 name2 name3')
    args = parser.parse_args()
    users = args._get_args()
    print(users)
    print(type(args))



    # read data from file access.txt
    # file_name = 'access.txt'
    # Access.instantiate_from_txt(file_name)
    #
    # # print anomalies
    # print(f'Anomalie rilevate:\n{Access.format_anomalies(users)}')
    # print(f'Numero totale di anomalie: {Access.number_of_anomalies(users)}')
    # print(f'Utente con il maggior numero di anomalie: {Access.max_number_of_anomalies(users)}')


#     todo: implement argparse
