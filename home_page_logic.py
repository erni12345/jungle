
from db_commands import *


def get_posts(user_id):
    """
    Fonction qui renvoie les posts qui devraient apparaitre sur la page d'acceuil d'un utilisateur

    Args:
        user_id (int): id de l'utilisateur
    """
    def get_follows(user_id):
        """
        Fonction qui renvoie une liste des personnes que l'utilisateur sui
        """
        query = """SELECT * FROM Follows
                   WHERE idFollower = """ + str(user_id)+" ;"
        following = query_db(query=query)

        return [x["idFollowing"] for x in following]

    
    
    def get_posts_from_accounts(account_ids):

        """
            Fonction qui renvoie les posts, poste par une liste d'utilisateurs.
        """

        query = """SELECT * FROM Posts
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



