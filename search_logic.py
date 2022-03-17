from db_commands import *



def user_search(search):

    query = """SELECT * FROM Accounts
            WHERE username LIKE  """
    query += "'" + "%" + search + "%" + "'"
    search_res = query_db(query=query, args=[])
    print(search_res)
    return [dict(x) for x in search_res]


def follow_account(user, following):
    query = """INSERT INTO Follows (idFollower, idFollowing)
                Values (?, ?);
                """
    change_db(query, [user, following])
    return "Worked"