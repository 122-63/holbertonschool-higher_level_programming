-- lists all shows contained in hbtn_0d_tvshows without a genre linked
-- Each record should display: tv_shows.title - tv_show_genres.genre_id
-- Results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
SELECT tv_shows.title, genre_id
FROM tv_show_genres
LEFT JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id
RIGHT OUTER JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id
WHERE genre_id is NULL
ORDER BY tv_shows.title, tv_show_genres.genre_id;
