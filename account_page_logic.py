from db_commands import *


def get_user_posts(userid):
    
    query = """SELECT * FROM Posts
                WHERE id = ? ;"""
    
    
    posts = query_db(query=query, args=[userid], one=False)

    return [dict(x) for x in posts]


def getAccount(userId):
    query = """SELECT * FROM Accounts
                WHERE id = ?;"""

    account = query_db(query=query, args=[userId], one=True)

    return dict(account)