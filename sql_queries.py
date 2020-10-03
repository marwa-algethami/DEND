# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays ; "
user_table_drop = "DROP TABLE IF EXISTS users ;"
song_table_drop = "DROP TABLE IF EXISTS songs ; "
artist_table_drop = "DROP TABLE IF EXISTS artists ;"
time_table_drop = "DROP TABLE IF EXISTS time; "

#temp_table_drop = (""" DROP TABLE IF EXISTS temp;""")

# CREATE TABLES
#specify data type and constraints 
songplay_table_create = (""" CREATE TABLE IF NOT EXISTS songplays (
                                                                    songplay_id serial  NOT NULL  , 
                                                                    start_time bigint REFERENCES time,
                                                                    user_id varchar  REFERENCES users ,
                                                                    level varchar , 
                                                                    song_id varchar REFERENCES songs, 
                                                                    artist_id varchar  REFERENCES artists ,
                                                                    session_id varchar NOT NULL ,
                                                                    location varchar , 
                                                                    user_agent varchar ,
                                                                    PRIMARY KEY (songplay_id )
                                                                 
                                                                    
                                                                    
                                                                    );""")

user_table_create = (""" CREATE TABLE IF NOT EXISTS users (user_id varchar  NOT NULL  , first_name varchar, last_name varchar, gender varchar, level varchar , CONSTRAINT user_pkey PRIMARY KEY (user_id) 
);""")

song_table_create = (""" CREATE TABLE IF NOT EXISTS songs (song_id varchar NOT NULL , title varchar, artist_id varchar, year int , duration float , CONSTRAINT song_pkey PRIMARY KEY (song_id) 
);""")

artist_table_create = (""" CREATE TABLE IF NOT EXISTS artists (artist_id varchar NOT NULL , name varchar, location varchar, latitude float, longitude float , CONSTRAINT artist_pkey PRIMARY KEY (artist_id) 
);""")

time_table_create = (""" CREATE TABLE IF NOT EXISTS time(start_time bigint  , hour int,day int, week int,month int , year int ,weekday int 
,CONSTRAINT time_pkey PRIMARY KEY (start_time) 

);""")

#temp_table_create = (""" CREATE TABLE temp ( data json)""")


# INSERT RECORDS

songplay_table_insert = (""" INSERT INTO songplays (start_time , user_id , level  , song_id , artist_id  , session_id  , location  , user_agent )
VALUES ( %s, %s ,%s ,%s ,%s ,%s ,%s ,%s)  
""")
#i use upsert feature to update users table with new inserted level 
user_table_insert = (""" INSERT INTO users (user_id , first_name , last_name , gender , level ) VALUES (%s, %s, %s ,%s ,%s)
ON CONFLICT ON CONSTRAINT user_pkey
DO 
   UPDATE SET level = EXCLUDED.level""")

song_table_insert = (""" INSERT INTO songs (song_id , title , artist_id , year  , duration ) VALUES (%s, %s, %s ,%s ,%s)
ON CONFLICT ON CONSTRAINT song_pkey 
DO NOTHING

 """)

artist_table_insert = (""" INSERT INTO artists (artist_id , name , location , latitude , longitude  ) VALUES (%s, %s, %s ,%s ,%s)
ON CONFLICT ON CONSTRAINT artist_pkey 
DO NOTHING
""")


time_table_insert = (""" INSERT INTO time (start_time , hour , day , week , month  , year  , weekday ) VALUES (%s, %s, %s ,%s ,%s ,%s ,%s)
ON CONFLICT ON CONSTRAINT time_pkey 
DO NOTHING""")

json_copy = ("""COPY temp FROM '%s';""")

# FIND SONGS
#Implement the song_select to find the song ID and artist ID based on the title, artist name, and duration of a song.
#Escape query values by using the placholder %s method
song_select = ("""  select s.song_id , a.artist_id from songs as s join artists as a  on s.artist_id = a.artist_id 
where s.title = %s and a.name = %s and s.duration = %s  """)

# QUERY LISTS

create_table_queries = [user_table_create, song_table_create, artist_table_create, time_table_create , songplay_table_create ]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop ]