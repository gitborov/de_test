
import psycopg2
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
try:
    # Подключение к существующей базе данных
    connection = psycopg2.connect(dbname='postgres',
                                    user="admin",
                                  # пароль, который указали при установке PostgreSQL
                                  password="password",
                                  host="127.0.0.1",
                                  port="5433")
    connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    # Курсор для выполнения операций с базой данных
    cursor = connection.cursor()
    sql_create_database = '''
SET search_path TO DE_test_schema;
    
 --функция установливающая текущее время в нужной колонке 
CREATE OR REPLACE FUNCTION trigger_set_timestamp()
RETURNS TRIGGER AS $$
BEGIN
  NEW.update_dttm = NOW()::timestamp;
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;


create table users (
	user_id serial primary key, 
	gender varchar(30),
	name_title varchar(30),
	name_first varchar(30),
	age int,
	nat varchar(10),
	created_dttm timestamp default now()::timestamp,
	update_dttm timestamp default now()::timestamp
);
--триггер, вызывающий функцию при попытке обновления данных
CREATE TRIGGER set_timestamp
BEFORE UPDATE ON users
FOR EACH ROW
EXECUTE PROCEDURE trigger_set_timestamp();


create table contact_details
	(user_id int primary key references users(user_id),
	phone varchar(30),
	cell varchar(30),
	created_dttm timestamp default now()::timestamp,
	update_dttm timestamp default now()::timestamp);

CREATE TRIGGER set_timestamp
BEFORE UPDATE ON contact_details
FOR EACH ROW
EXECUTE PROCEDURE trigger_set_timestamp();


create table media_data
	(user_id int primary key references users(user_id),
	picture varchar(60),
	created_dttm timestamp default now()::timestamp,
	update_dttm timestamp default now()::timestamp);

CREATE TRIGGER set_timestamp
BEFORE UPDATE ON media_data
FOR EACH ROW
EXECUTE PROCEDURE trigger_set_timestamp();


create table registration_data
	(user_id int primary key references users(user_id),
	email varchar(30),
	username varchar (30),
	"password" varchar(30),
	password_md5 varchar(50),
	password_validation bool,
	created_dttm timestamp default now()::timestamp,
	update_dttm timestamp default now()::timestamp);

CREATE TRIGGER set_timestamp
BEFORE UPDATE ON registration_data
FOR EACH ROW
EXECUTE PROCEDURE trigger_set_timestamp();


create table cities
	(city_id serial primary key,
	city varchar(30),
	state varchar(30),
	country varchar(30),
	timezone_offset  varchar(30),
	timezone_description  varchar(30),
	created_dttm timestamp default now()::timestamp,
	update_dttm timestamp default now()::timestamp);

CREATE TRIGGER set_timestamp
BEFORE UPDATE ON cities
FOR EACH ROW
EXECUTE PROCEDURE trigger_set_timestamp();
;

create table locations 
	(user_id int primary key references users(user_id),
	city_id int references cities(city_id),
	street_name varchar(30),
	street_number int,
	postcode varchar(30),
	latitude float8,
	longitude float8,
	created_dttm timestamp default now()::timestamp,
	update_dttm timestamp default now()::timestamp);

CREATE TRIGGER set_timestamp
BEFORE UPDATE ON locations
FOR EACH ROW
EXECUTE PROCEDURE trigger_set_timestamp();

create table test_table
	(id int primary key references users(user_id),
	some_shit varchar(30),
	some_shit2 varchar(30)
	);
	'''
    cursor.execute(sql_create_database)
    print("Таблицы PostgreSQL успешно построены")
    # sql_create_scheme = '''CREATE SCHEMA IF NOT EXISTS DE_test_schema'''
    # cursor.execute(sql_create_scheme)
except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("Соединение с PostgreSQL закрыто")