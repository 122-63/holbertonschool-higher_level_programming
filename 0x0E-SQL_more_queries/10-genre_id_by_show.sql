-- Write a script that lists all shows contained in hbtn_0d_tvshows
-- Each record should display: tv_shows.title - tv_show_genres.genre_id
-- Results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
SELECT state.title, genre.genre_id FROM tv_shows
INNER JOIN tv_show_genres ON state.id = genre.show_id
ORDER BY state.title, genre.genre_id;
