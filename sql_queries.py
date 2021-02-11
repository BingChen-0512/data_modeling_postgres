# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES
songplay_table_create = ("""
    CREATE TABLE songplays (
    songplay_id SERIAL PRIMARY KEY,
    start_time timestamp not NULL references time,
    user_id int NOT NULL references users,
    level varchar NOT NULL,
    song_id VARCHAR references songs,
    artist_id VARCHAR references artists,
    session_id int NOT NULL,
    location varchar NOT NULL,
    user_agent VARCHAR NOT NULL
    )
""")

user_table_create = ("""
    CREATE TABLE users(
    user_id int PRIMARY KEY,
    first_name varchar NOT NULL,
    last_name varchar NOT NULL,
    gender varchar NOT NULL,
    level varchar NOT NULL
    )
""")

song_table_create = ("""
    CREATE TABLE songs(
    song_id VARCHAR PRIMARY KEY,
    title varchar NOT NULL,
    artist_id VARCHAR NOT NULL,
    year int NOT NULL,
    duration numeric NOT NULL
    )
""")

artist_table_create = ("""
    CREATE TABLE artists(
    artist_id VARCHAR PRIMARY KEY,
    name varchar NOT NULL,
    location varchar NOT NULL,
    latitude numeric,
    longitude numeric
    )
""")

time_table_create = ("""
    CREATE TABLE time(
    start_time timestamp PRIMARY KEY,
    hour int NOT NULL,
    day int NOT NULL,
    week int NOT NULL,
    month int NOT NULL,
    year int NOT NULL,
    weekday varchar NOT NULL
    )
""")


# INSERT RECORDS

songplay_table_insert = ("""
    INSERT INTO songplays(start_time, user_id, level, song_id, artist_id, session_id, location,user_agent)
    VALUES (to_timestamp(%s/1000), %s, %s, %s, %s, %s, %s, %s)
""")

user_table_insert = ("""
    INSERT INTO users(user_id, first_name, last_name, gender,level)
    VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT (user_id)
    DO UPDATE
    SET level=excluded.level
""")

song_table_insert = ("""
    INSERT INTO songs(song_id, title, artist_id, year, duration)
    VALUES (%s, %s, %s, %s, %s)
    on CONFLICT (song_id)
    do nothing
""")

artist_table_insert = ("""
    INSERT INTO artists(artist_id, name, location, latitude, longitude)
    VALUES (%s, %s, %s, %s, %s)
    on CONFLICT (artist_id)
    do nothing
""")


time_table_insert = ("""
    INSERT INTO time(start_time, hour, day, week, month, year, weekday)
    VALUES (to_timestamp(%s/1000), %s, %s, %s, %s, %s, %s)
    on CONFLICT (start_time)
    do nothing
""")

# FIND SONGS

song_select = ("""
    SELECT s.song_id, s.artist_id
    FROM songs s
    JOIN artists a
    ON s.artist_id=a.artist_id
    WHERE s.title=%s AND a.name=%s AND s.duration=%s
""")

# QUERY LISTS

create_table_queries = [user_table_create, song_table_create, artist_table_create, time_table_create, songplay_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
