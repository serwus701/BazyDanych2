from sqlalchemy import create_engine

from sql_requests.shared_sql_requests import sql_change_user_password, sql_change_admin_password, sql_request_login
from tools import is_user_or_admin

url = 'mysql://login_manager:loginpassword123@127.0.0.1/plants'
engine = create_engine(url)

NEITHER = 0
USER = 1
ADMIN = 2


def change_password(user_logged, new_password, old_password):
    connection = engine.connect()

    login_approval = sql_request_login(connection, user_logged, old_password)

    if login_approval == USER:
        try:
            sql_change_user_password(connection, new_password, user_logged)
            connection.close()
            return True
        except:
            connection.close()
            return False

    if login_approval == ADMIN:
        try:
            sql_change_admin_password(connection, new_password, user_logged)
            connection.close()
            return True
        except:
            connection.close()
            return False

    if login_approval == NEITHER:
        connection.close()
        return False





def report_an_issue():
    print("123")
