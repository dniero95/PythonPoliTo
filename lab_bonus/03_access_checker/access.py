import datetime as dt
class Access:
    all = []

    def __init__(self, date:dt.datetime, user:str, status:str):
        assert len(user) <= 10, f'Error! wrong username'
        assert status == 'S' or status == 'F', f'Error! wrong status'

        self.date = date
        self.user = user
        self.status = status

        Access.all.append(self)

    @classmethod
    def instantiate_from_txt(cls, path:str):
        with open(path, 'r') as file:
            access = file.readlines()

        for line in access:
            line = line.replace('\n', '')
            line = line.split(' ')
            date = line[0].split('-')
            hour = line[1].split(':')
            Access(
                date=dt.datetime(int(date[0]), int(date[1]), int(date[2]), int(hour[0]), int(hour[1]), int(hour[2])),
                user=line[2],
                status=line[3]
            )

    # check for anomalies on a specific user
    @staticmethod
    def anomalies_checker(user: str):
        anomalies = []
        for access in Access.all:
            if access.user == user and access.status == 'F':
                for i in range(Access.all.index(access) + 1, len(Access.all)):
                    if ((Access.all[i]).date - access.date).total_seconds() <= 60 and Access.all[i].status == 'F':
                        anomalies.append(f'{access.user} {access.date} {Access.all[i].date.time()}')
                        break
        return anomalies

    # return a string that contain each user that has made a strange access

    @staticmethod
    def format_anomalies(users:list):
        anomalies_text = ''
        for user in users:
            for record in Access.anomalies_checker(user):
                anomalies_text += f'{record}\n'
        return anomalies_text
    # return the number of anomalies given a list of user
    @staticmethod
    def number_of_anomalies(users:list):
        total = 0
        for user in users:
            total += len(Access.anomalies_checker(user))

        return total

    # return the user with the max number of anomalies given a list of user.

    @staticmethod
    def max_number_of_anomalies(users:list):
        anomalies = 0
        user = ''
        for user in users:
            if anomalies > Access.number_of_anomalies([user]):
                user = user.name
                anomalies = Access.number_of_anomalies([user])
        return user


    # print all access
    @staticmethod
    def print_all_access():
        for access in Access.all:
            print(access)

    # string version of the obj
    def __str__(self):
        return f'{self.date} {self.user} {self.status}'
    # represent the obj
    def __repr__(self):
        return f'{self.__class__.__name__}({self.date}, {self.user}, {self.status})'