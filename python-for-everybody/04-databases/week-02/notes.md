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

                                            **Thursday 26/11/2026**
# Databases and Visualization

This chapter integrating data retrieval, storage, and visualization in a multi-step data analysis process using Python and databases.
**Multi-Step Data Gathering and Processing**
Separate the data gathering process from data cleaning and analysis to handle large datasets and interruptions efficiently.
Use a restartable gathering process that stores raw data in a local or cloud database, allowing resumption without duplication.
**Data Cleaning and Analysis**
After gathering, clean and parse the raw data stored in the database to prepare it for analysis.
The cleaning phase is faster and can be rerun independently of the gathering phase, enabling efficient data processing.

# Visualization Example: Geocoding and Mapping
Use geocoding to convert addresses into geographic coordinates and visualize them on a map using Open Street Map.
The process involves running Python scripts to gather geodata, store it in a SQLite database, parse it into JavaScript, and display pins on an interactive map in a browser.
This approach teaches foundational concepts of data mining and visualization by building the processes from scratch, providing practical experience with Python, databases, APIs, and web-based visualization tools.

In a nutshell

Retrieving data means getting data from where it's stored so you can work with it. Common sources are files (CSV, Excel), databases (using SQL), and web APIs.

Visualization means turning that data into a chart so patterns are easy to see, such as a bar chart for comparing categories or a line chart for change over time.

The basic flow: retrieve → look at it → visualize

In a nutshell: data mining is finding useful patterns in large amounts of data, and the "technologies" are the tools and techniques used to do it.

Main techniques

Classification: put items into known groups (e.g. spam vs not spam).
Clustering: group similar items when you don't know the groups beforehand (e.g. customer segments).
Regression: predict a number (e.g. next month's sales).
Association rules: find things that happen together (e.g. people who buy bread often buy butter).
Anomaly detection: spot unusual items (e.g. fraud).

Tools and technologies

Languages and libraries: Python (pandas, scikit-learn), R, SQL.
Visual tools: Weka, KNIME, RapidMiner, Orange. You build the process by dragging blocks, with little or no code.
Big data tools: Hadoop, Spark, for data too large for one computer.
Storage: databases and data warehouses, where the data is kept before mining.
BI tools: Power BI, Tableau, for exploring and showing results. (Business Intelligence tools)
Gather raw data → clean it → choose a technique → build a model → check the results → present them
the raw data and restartable steps are the first part of that process.