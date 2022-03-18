from db_commands import *



def user_search(search):
    """
    Fonction qui recherche la base de donnes pour un compte
    ayant un nom proche de ce que demande l'utilisateur
    """
    query = """SELECT * FROM Accounts
            WHERE username LIKE  """
    query += "'" + "%" + search + "%" + "'"
    search_res = query_db(query=query, args=[])
    print(search_res)
    return [dict(x) for x in search_res]


def follow_account(user, following):
    """
    Fonction qui ajoute a la base de donnees le "follow" qu'a fait l'utilisateur
    """
    query = """INSERT INTO Follows (idFollower, idFollowing)
                Values (?, ?);
                """
    change_db(query, [user, following])
    return "Worked"