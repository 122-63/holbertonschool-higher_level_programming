-- uses the hbtn_0d_tvshows database to lists all genres of the show Dexter
-- The tv_shows table contains only one record where title = Dexter
-- Each record should display: tv_genres.name
SELECT tv_genres.name
FROM tv_show_genres
LEFT JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id
WHERE tv_shows.title = "Dexter"
ORDER BY tv_genres.name ASC;
