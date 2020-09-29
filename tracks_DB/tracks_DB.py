# This program extracts some information about some tracks from a .xml file
# and adds them to proper tables in a DB.

import xml.etree.ElementTree as ET
import sqlite3

conn = sqlite3.connect('tracksDB.sqlite')
cur = conn.cursor()

# Creating the tables
cur.executescript('''

DROP TABLE IF EXISTS Artists;
DROP TABLE IF EXISTS Albums;
DROP TABLE IF EXISTS Tracks;

CREATE TABLE Artists (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name  TEXT UNIQUE
);

CREATE TABLE Albums (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title  TEXT UNIQUE
);

CREATE TABLE Tracks (
    id  INTEGER NOT NULL PRIMARY KEY 
        AUTOINCREMENT UNIQUE,
    title  TEXT UNIQUE,
    album_id  INTEGER,
    time_len  INTEGER, rating  INTEGER, play_count  INTEGER
);

''')

fname = 'library.xml'

# Parsing the xml file and accessing the information of tracks.
stuff = ET.parse(fname)
all_val = stuff.findall('dict/dict/dict')

name = None
artist = None
album = None
play_count = None
rating = None
time_len = None

for entry in all_val:
    length = len(entry)
    #print('Length is ', length)
    #print(entry[1].tag)
    #print(entry[1].text)
    for i in range(length):
        key_val = entry[i].tag
        val_val = entry[i].text
        #print('key is ', key_val, '\n')
        #print('val is ', val_val, '\n')
        if key_val == 'key' and val_val == 'Name':
            name = entry[i+1].text
            print('name is ', name, '\n')
        elif key_val == 'key' and val_val == 'Artist':
            artist = entry[i+1].text
            print('artist is ', artist, '\n')
        elif key_val == 'key' and val_val == 'Album':
            album = entry[i+1].text
            print('album is ', album, '\n')
        elif key_val == 'key' and val_val == 'Play Count':
            play_count = entry[i+1].text
            print('ply_count is ', play_count, '\n')
        elif key_val == 'key' and val_val == 'Rating':
            rating = entry[i+1].text
            print('rating is ', rating, '\n')
        elif key_val == 'key' and val_val == 'Total Time':
            time_len = entry[i+1].text
            print('time_len is ', time_len, '\n')
        
        if name is None or artist is None or album is None or play_count is None or rating is None or time_len is None:
            print("****None value detected ****\n")
            continue

        # Entering the extracted data into the database.

        cur.execute('INSERT OR IGNORE INTO Artists(name) VALUES (?)', (artist,))
        cur.execute('SELECT id FROM Artists WHERE name = (?)', (artist,))
        artist_id = cur.fetchone()[0]
        print('artist_id is ', artist_id, '\n')
        cur.execute('INSERT OR IGNORE INTO Albums(title, artist_id) VALUES (?, ?)', (album, artist_id))
        cur.execute('SELECT id FROM Albums WHERE title = (?)', (album,))
        album_id = cur.fetchone()[0]
        print('album_id is ', album_id, '\n')
        cur.execute('''INSERT OR REPLACE
        INTO Tracks(title, album_id, time_len, rating, play_count) VALUES (?, ?, ?, ?, ?)''', (name, album_id, time_len, rating, play_count))

        conn.commit()

print('\nThanks for reviewing')

# Thanks for reviewing
