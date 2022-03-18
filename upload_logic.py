from db_commands import *

def upload_post(id, title, body, path):
    """
    Fonction qui ajoute a base de donnes un post
    """
    query = """INSERT INTO Posts (id, Title, Body, Likes, path)
                Values (?, ?, ?, 0, ?); """
    
    change_db(query, [id, title, body, path])

    return "Post Added!"