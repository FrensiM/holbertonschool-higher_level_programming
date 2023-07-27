-- genre id
SELECT ts.title, tsg.genre_id
FROM tv_shows AS ts 
LEFT JOIN tv_show_genres AS tsg
    ON tsg.show_id = ts.id
ORDER BY ts.title, tsg.genre_id;
