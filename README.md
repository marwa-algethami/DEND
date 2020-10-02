**Project: Data Modeling with Postgres**

**About Project**

This project aims to Analyze a startup called Sparkify they've been collecting on songs and user activity on their new music streaming app.
My role was creating data modeling with Postgres and build an ETL pipeline using Python.
First, I choose the Star Schema model because of its simplicity and efficiency for defining fact and dimension tables. I was then building the ETL pipeline to transfer data from JSON directories into these tables in Postgres using Python and SQL.

**Project Template**

This project contains these files:
1.*test.ipynb* displays the first few rows of each table to let you check your database.
2.*create_tables.py* drops and creates tables. 
3.*etl.ipynb* reads and processes a single file from song_data and log_data and loads the data into your tables. 
4.*etl.py* reads and processes files from song_data and log_data and loads them into your tables. 
5.*sql_queries.py* contains all your SQL queries and is imported into the last three files above.

**Schema for the Song Play Analysis**
Using the song and log datasets, I created a star schema optimized for queries on song play analysis. This includes the following tables.
Fact Table
1.songplays - records in log data associated with song plays. with following attributes
songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent
Dimension Tables
users - users in the app. with the following attributes
user_id, first_name, last_name, gender, level
songs - songs in the music database. With the following attributes
song_id, title, artist_id, year, duration
artists - artists in the music database. With the following attributes
artist_id, name, location, latitude, longitude
time - timestamps of records in songplays broken down into specific units. with the following attributes
start_time, hour, day, week, month, year, weekday

**ETL Pipeline**
The following process is to create an ETL pipeline 
•read all JSON Files from the directories
•Create and insert Songs and Artists table from song dataset
•Create and insert  Users and Time table from log dataset

**Run Pipeline**
The following instructions are to run the pipeline :
1.Run run_create. ipynb to create tables.
2.Run etl. ipynb at the end, I did etl.py implementation
3.Run test.ipynb to make sure all the records were added successfully

