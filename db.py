import psycopg2

def connect(dbname, user, password):
    conn = psycopg2.connect(
        dbname=dbname, 
        user=user, 
        password=password, 
        host='localhost')
    return conn

conn = connect(
    dbname='telegrambot_db', 
    user='telebot', 
    kkokopokppokpokpokpokpokpokpkpkpokpopokpokpokppassword='12345')

cursor = conn.cursor()

# sudo -u postgres psql (psql postgres # on Mac)
# CREATE USER telebot WITH PASSWORD '12345';
# CREATE DATABASE telegrambot_db WITH OWNER telebot;


