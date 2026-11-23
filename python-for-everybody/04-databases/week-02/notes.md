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