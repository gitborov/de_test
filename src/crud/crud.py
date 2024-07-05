from src.connection.postgres import with_connection

@with_connection
def create_table(cur, table_name, columns):
    create_table_query = '''
        CREATE TABLE IF NOT EXISTS {} (
            id SERIAL PRIMARY KEY,
            {}
        )
    '''.format(table_name, ', '.join(columns))
    cur.execute(create_table_query)

@with_connection
def insert_data(cur, table_name, columns, values):
    insert_query = '''
        INSERT INTO {} ({})
        VALUES (%s, %s, ...)
    '''.format(table_name, ', '.join(columns))
    cur.execute(insert_query, values)

@with_connection
def read_data(cur, schema_name, table_name):
    select_query = 'SELECT * FROM {}'.format(table_name)
    cur.execute(select_query)
    rows = cur.fetchall()
    return rows

@with_connection
def update_data(cur, table_name, columns, values, condition):
    update_query = '''
        UPDATE {}
        SET {} = %s, {}
        WHERE condition
    '''.format(table_name, columns[0], columns[1])
    cur.execute(update_query, values)

@with_connection
def delete_data(cur, table_name, condition):
    delete_query = '''
        DELETE FROM {}
        WHERE condition
    '''.format(table_name)
    cur.execute(delete_query)