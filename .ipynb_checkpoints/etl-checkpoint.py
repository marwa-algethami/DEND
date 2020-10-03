import os
import glob
import psycopg2
import pandas as pd
from sql_queries import *


def process_song_file(cur, filepath):
    '''This function will read the song_data json files and insert the records into Song & Artists tables. 
    Parameters: 
    cur: cursor used to execute queries.
    filepath: already assigned in main function, songs files path.
    '''
    df =  pd.read_json(filepath, lines=True)

    song_data = df[['song_id', 'title', 'artist_id', 'year', 'duration']]
    song_data = song_data.values[0]
    song_data = song_data.tolist()
    cur.execute(song_table_insert, song_data)
    
    artist_data = df[['artist_id', 'artist_name', 'artist_location', 'artist_latitude',  'artist_longitude']].values[0]
    artist_data = artist_data.tolist()
    cur.execute(artist_table_insert, artist_data)


def process_log_file(cur, filepath):
    '''This function will read the log_data json files and insert the records into Time & Users and songplays tables.
    Parameters: 
    cur: cursor used to execute queries.
    filepath: already assigned in main function, log files path.
    '''
    
    df = pd.read_json(filepath, lines=True)

    df = df.loc[lambda x: x['page'] == 'NextSong']


    t = pd.to_datetime(df['ts'], unit='ms')
    
    time_data =  [ df['ts'] , t.dt.hour , t.dt.day ,t.dt.weekofyear , t.dt.month ,t.dt.year , t.dt.dayofweek]
    column_labels =  [ 'timestamp','hour', 'day', 'weekofyear', 'month', 'year',  'weekday' ]
    time_df = pd.DataFrame({column_labels[i]: time_data[i] for i in range(len(column_labels))} )

    for i, row in time_df.iterrows():
        cur.execute(time_table_insert, list(row))

    user_df = df[['userId','firstName' , 'lastName' ,'gender','level']]

    for i, row in user_df.iterrows():
        cur.execute(user_table_insert, row)

    for index, row in df.iterrows():
        
        cur.execute(song_select, (row.song, row.artist, row.length))
        results = cur.fetchone()
        
        if results:
            songid, artistid = results
        else:
            songid, artistid = None, None

        # insert songplay record
        songplay_data =  ( row.ts, row.userId, row.level, songid, artistid, row.sessionId, row.location, row.userAgent)
        cur.execute(songplay_table_insert, songplay_data)


def process_data(cur, conn, filepath, func):
    '''This function will generate the file names in a directory,  os.walk() returns a list of three items, name of the root directory,
     a list of the names of the subdirectories, and a list of the filenames in the current directory.
    Parameters: 
    cur: used to execute queries.
    filepath: for json files directories.
    func: used in iteration process. 
    '''
    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root,'*.json'))
        for f in files :
            all_files.append(os.path.abspath(f))

    # get total number of files found
    num_files = len(all_files)
    print('{} files found in {}'.format(num_files, filepath))

    # iterate over files and process
    for i, datafile in enumerate(all_files, 1):
        func(cur, datafile)
        conn.commit()
        print('{}/{} files processed.'.format(i, num_files))


def main():
    '''This function is used in connecting to the database and calling two different functions with thier parameters. '''
        
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
    cur = conn.cursor()

    process_data(cur, conn, filepath='data/song_data', func=process_song_file)
    process_data(cur, conn, filepath='data/log_data', func=process_log_file)
    


    conn.close()


if __name__ == "__main__":
    main()