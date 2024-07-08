from src.connection.postgres import with_connection


@with_connection
def read_data(cur, schema_name, flag: bool = True):
    select_query = (f'''
        select u.user_id ,  rd.username, rd."password" , rd.password_validation 
        from {schema_name}.users u 
        join {schema_name}.registration_data rd using(user_id)
        where rd.password_validation = {flag}  ''')
    cur.execute(select_query)
    rows = cur.fetchall()
    return rows

