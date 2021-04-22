from datetime import datetime, timedelta
from pyroaring import BitMap
import uuid


class User:
    def __init__(self, user_name, logins):
        self.user_name = user_name
        self.logins = logins

    def login(self, date):
        self.logins.add(date)


class Session:
    def __init__(self, users):
        self.users = users
    
    def login_user(self, user_name):
        date_now = int(datetime.utcnow().strftime("%Y%m%d"))
        try:
            self.users[user].login(date_now)
        except:
            self.users[uuid.uuid1()] = User(user_name, BitMap([date_now]))
        print(self.users)
    
    def weekly_inactivity(self):
        counter = 0
        week_ago =  datetime.now() - timedelta(days=7)
        
        for user in self.users:
            last_login = datetime.strptime(str(self.users[user].logins[-1]), "%Y%m%d")
            if last_login < week_ago:
                counter += 1
        
        return counter