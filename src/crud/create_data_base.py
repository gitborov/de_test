from src.connection.postgres import with_connection

@with_connection
def create_db(cursor):

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


create table if not exists users (
	user_id serial primary key, 
	gender varchar(100),
	name_title varchar(100),
	name_first varchar(100),
	age int,
	nat varchar(100),
	created_dttm timestamp default now()::timestamp,
	update_dttm timestamp default now()::timestamp
);
--триггер, вызывающий функцию при попытке обновления данных

DROP TRIGGER IF EXISTS set_timestamp
ON users;
CREATE TRIGGER set_timestamp
BEFORE UPDATE ON users
FOR EACH ROW
EXECUTE PROCEDURE trigger_set_timestamp();


create table if not exists contact_details
	(user_id int primary key references users(user_id),
	phone varchar(100),
	cell varchar(100),
	created_dttm timestamp default now()::timestamp,
	update_dttm timestamp default now()::timestamp);

DROP TRIGGER IF EXISTS set_timestamp
ON contact_details;
CREATE TRIGGER set_timestamp
BEFORE UPDATE ON contact_details
FOR EACH ROW
EXECUTE PROCEDURE trigger_set_timestamp();


create table if not exists media_data
	(user_id int primary key references users(user_id),
	picture varchar(100),
	created_dttm timestamp default now()::timestamp,
	update_dttm timestamp default now()::timestamp);

DROP TRIGGER IF EXISTS set_timestamp
ON media_data;
CREATE TRIGGER set_timestamp
BEFORE UPDATE ON media_data
FOR EACH ROW
EXECUTE PROCEDURE trigger_set_timestamp();


create table if not exists registration_data
	(user_id int primary key references users(user_id),
	email varchar(100),
	username varchar (100),
	"password" varchar(100),
	password_md5 varchar(100),
	password_validation bool,
	created_dttm timestamp default now()::timestamp,
	update_dttm timestamp default now()::timestamp);

DROP TRIGGER IF EXISTS set_timestamp
ON registration_data;
CREATE TRIGGER set_timestamp
BEFORE UPDATE ON registration_data
FOR EACH ROW
EXECUTE PROCEDURE trigger_set_timestamp();


create table if not exists cities
	(city_id serial primary key,
	city varchar(100) UNIQUE,
	state varchar(100),
	country varchar(100),
	timezone_offset  varchar(100),
	timezone_description  varchar(100),
	created_dttm timestamp default now()::timestamp,
	update_dttm timestamp default now()::timestamp);

DROP TRIGGER IF EXISTS set_timestamp
ON cities;
CREATE TRIGGER set_timestamp
BEFORE UPDATE ON cities
FOR EACH ROW
EXECUTE PROCEDURE trigger_set_timestamp();
;

create table if not exists locations 
	(user_id int primary key references users(user_id),
	city_id int references cities(city_id),
	street_name varchar(100),
	street_number int,
	postcode varchar(100),
	latitude float8,
	longitude float8,
	created_dttm timestamp default now()::timestamp,
	update_dttm timestamp default now()::timestamp);

DROP TRIGGER IF EXISTS set_timestamp
ON locations;
CREATE TRIGGER set_timestamp
BEFORE UPDATE ON locations
FOR EACH ROW
EXECUTE PROCEDURE trigger_set_timestamp();

create table if not exists invalid_data (
	user_id serial primary key, 
	gender varchar(100),
	name_title varchar(100),
	name_first varchar(100),
	age int,
	nat varchar(100),
    phone varchar(100),
    cell varchar(100),
    picture varchar(100),
    email varchar(100),
    username varchar (100),
    "password" varchar(100),
    password_md5 varchar(100),
    password_validation bool,
    street_name varchar(100),
    street_number int,
    postcode varchar(100),
    latitude float8,
    longitude float8,
    timezone_offset  varchar(100),
    timezone_description  varchar(100),
    created_dttm timestamp default now()::timestamp);
	'''

    cursor.execute(sql_create_database)
    # return cursor.fetchall()


print(create_db())