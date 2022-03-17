
from db_commands import *


def get_posts(user_id):

    def get_follows(user_id):
        query = """SELECT * FROM Follows
                   WHERE idFollower = """ + str(user_id)+" ;"
        following = query_db(query=query)

        return [x["idFollowing"] for x in following]

    
    
    def get_posts_from_accounts(account_ids):

        query = """SELECT * FROM Posts
                    ORDER BY PostID ASC
                    WHERE id IN """
        
        if len(account_ids) > 1:

            query += str(tuple(account_ids)) + ";"
        elif len(account_ids) == 1:
            query = """SELECT * FROM Posts
                    WHERE id = """ + str(account_ids[0])+" ;"
        else:
            query = ""

        
        posts = query_db(query=query)

        posts =  [dict(x) for x in posts]
        posts.reverse()
        return posts

    
    following = get_follows(user_id)
    posts = get_posts_from_accounts(following)
    return posts



