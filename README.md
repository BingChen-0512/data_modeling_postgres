# Data Modeling with Postgres for Sparkify
Sparkify is a startup, which has a new music streaming app. They've been collecting data about songs and user activity.

### Motivation
Sparkify wants to know what songs users are listening to by analyzing the data collected. To query the data, which resides in a directory of JSON logs on user activity and another directory with JSON metadata on the songs, they need a well-designed database as well as an ETL pipline.

### Design of database schema and ETL pipeline
The database schema was designed to be a star schema with a fact table (songplays) and four dimension tables (users, songs, artists, time).

#### Fact Table
1. **songplays**-records in log data asscociated with songs plays
- _songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent_
![alt text](https://github.com/BingChen-0512/data_modeling_postgres/blob/master/songplays.png?raw=true)
#### Dimension Tables
2. **users**-users in the app
- _user_id, first_name, last_name, gender, level_
![alt text](https://github.com/BingChen-0512/data_modeling_postgres/blob/master/users.png?raw=true)
3. **songs**-songs in music database
- _song_id, title, artist_id, year, duration_
![alt text](https://github.com/BingChen-0512/data_modeling_postgres/blob/master/songs.png?raw=true)
4. **artists**-artists in music database
- _artist_id, name, location, latitude, longitude_
![alt text](https://github.com/BingChen-0512/data_modeling_postgres/blob/master/artists.png?raw=true)
5. **time**-timestamps of records in **songplays** broken down into specific units
- _start_time, hour, day, week, month, year, weekday_
![alt text](https://github.com/BingChen-0512/data_modeling_postgres/blob/master/time.png?raw=true)

#### ETL pipeline
The ETL pipeline is based on two functions. <br \>
The _process_song_file_ function is to read files in the "data/song_data" file and load the data about songs into **songs** table and **artists** table. 
The _process_log_file_ function is to extract log data associated with song plays and load them into **users** table, **time** table and **songplays** table. As the **songplays** table is designed as fact table, the primary keys of **songs** table and **artists** table are added to it by joining these two dimesion tables on artists_id. Finally, a _process_data_ function is used to walk through the two directories and call the above two functions respectively.

### How to run the Python scripts
- Run create_tables.py first to create the database and tables, and then run etl.py to load data into the database.
- The Jupyter Notebook files, etl.ipynb and test.ipynb, are for testing and seeing results.

### Examples and Analysis Results
- The example is a subset of the whole dataset. The log data only includes user activity in November 2018, while the song data only covers 71 records.
- In the **songplays** table, only 1 song has both songid and artistid. By joining **songplays** table with **songs** table, we know the song's name is **Setantamatins**.  
