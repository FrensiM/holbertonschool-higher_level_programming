-- genre id
SELECT ts.title, tsg.genre_id
FROM tv_show_genres AS tsg 
INNER JOIN tv_shows AS ts
    ON tsg.show_id = ts.id
ORDER BY ts.title, tsg.genre_id;
