# 04-databases - Week 2
                                        **Monday 23/11/2026**
# Using databases with Python
**Chapter Fifteen: Many-to-Many Relationships in SQL**

Many-to-One and One-to-Many Relationships

One-to-many relationships involve one record in a table being related to many records in another table, such as an album having many tracks.
These relationships are modeled using foreign keys on the "many" side, allowing multiple records to reference a single record.
Many-to-Many Relationships and Junction Tables

Many-to-many relationships occur when multiple records in one table relate to multiple records in another, such as books having multiple authors and authors writing multiple books.
These cannot be modeled with a single foreign key, so a junction (or connector) table is created to link the two tables with two foreign keys.
The junction table can also store additional data about the relationship, like roles (e.g., instructor or student).

In a nutshell:many-to-many means each row on both sides can link to many rows on the other side. It is solved with a third table in the middle.
# code example:
CREATE TABLE PlaylistTrack (
    playlist_id INTEGER,
    track_id INTEGER,
    PRIMARY KEY (playlist_id, track_id)
)

**What to remember**:
Many-to-many = two one-to-many relationships joined by a middle table.
The junction table holds two foreign keys, and usually nothing else.
Both foreign keys sit in the junction table, because that is now the "many" side of both relationships.


# JOIN
In a nutshell: a table holds one kind of thing. JOIN glues rows from two tables together using the foreign key, so you can read the data side by side again.

Why JOIN exists

Your Album table stores artist_id = 11, not the name "AC/DC". That avoids repeating text, but a bare 11 is unreadable. JOIN looks up the 11 in the Artist table and brings the name back.

One JOIN, step by step
sql
SELECT Album.title, Artist.name
FROM Album JOIN Artist
ON Album.artist_id = Artist.id
SELECT Album.title, Artist.name: which columns I want to see.
FROM Album JOIN Artist: which two tables to glue.
ON Album.artist_id = Artist.id: the matching rule. Glue a row of Album to the row of Artist where the foreign key equals the primary key. This is the line that makes it work.
Table.column notation (like Album.title): both Album and Track have a column called title, and several tables have id. The table name tells SQL which one you mean.

Result: ('Who Made Who', 'AC/DC'), because Album's artist_id 11 matched Artist's id 11.

Chaining several JOINs

That is exactly your grader's query. Each JOIN follows one foreign key:

sql
SELECT Track.title, Artist.name, Album.title, Genre.name
FROM Track JOIN Genre JOIN Album JOIN Artist
ON Track.genre_id = Genre.id
AND Track.album_id = Album.id
AND Album.artist_id = Artist.id
Track.genre_id = Genre.id: Track → Genre
Track.album_id = Album.id: Track → Album
Album.artist_id = Artist.id: Album → Artist (the path to the artist goes through Album)

So one result row is a track, with its artist, album and genre names all in one line.