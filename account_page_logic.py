from db_commands import *


def get_user_posts(userid):

    query = """SELECT * FROM Posts
                WHERE id = ? ;"""
    
    
    posts = query_db(query=query, args=[userid], one=False)

    return [dict(x) for x in posts]


def getAccount(userId):

    """
    Fonction qui renvoie les infos d'un compte assoscie a id

    """
    
    query = """SELECT * FROM Accounts
                WHERE id = ?;"""

    account = query_db(query=query, args=[userId], one=True)

    return dict(account)