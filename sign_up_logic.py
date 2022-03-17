from db_commands import *




# Gestion de la base de données (copier-coller de la doc de FLASK)


def check_if_account_exists(email, password):
    query = """SELECT id FROM Login
                WHERE Email = ? AND Password = ?;"""

    accounts = query_db(query=query, args=[email, password])

    return accounts


def creat_account(id, name, last_name, age, username, bio):

    modify_login = """INSERT INTO Accounts (id, Name, Prenom, Biography, Age, Interests, username)
                        Values (?, ?, ?, ?, ?, ?, ?); """

    change_db(modify_login, [id, last_name, name, bio, age, "", username])

    return "Worked"