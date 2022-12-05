from db import conn, cursor
from datetime import datetime

def create_table_location():
    query = """
    CREATE TABLE IF NOT EXISTS locations (
        id SERIAL PRIMARY KEY,
        chat_id INT,
        latitude FLOAT,
        longitude FLOAT,
        create_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
    );"""
    cursor.execute(query=query)
    conn.commit()
    print('create table location successfuly!')

def insert_location(chat_id: int,
                    latitude: float, 
                    longitude: float):
    query = f"""
    INSERT INTO locations(
        chat_id, latitude, longitude
    )VALUES (
        {chat_id}, {latitude}, {longitude}
        );"""
    cursor.execute(query=query)
    conn.commit()
    print('Insert location successfuly!')

def update_location(chat_id: int,
                    latitude: float,
                    longitude: float): 
    query = f"""
        UPDATE locations 
        SET latitude = {latitude}, longitude = {longitude}, create_at = CURRENT_TIMESTAMP
        WHERE chat_id = {chat_id};"""
    cursor.execute(query=query)
    conn.commit()

def is_location_exists(chat_id: int):
    query = f"""
        SELECT * 
        FROM locations
        WHERE chat_id = {chat_id};"""

    cursor.execute(query=query)
    response = cursor.fetchone()
    if response:
        return True
    return False

