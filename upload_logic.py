from db_commands import *

def upload_post(id, title, body, path):

    query = """INSERT INTO Posts (id, Title, Body, Likes, path)
                Values (?, ?, ?, 0, ?); """
    
    change_db(query, [id, title, body, path])

    return "Post Added!"