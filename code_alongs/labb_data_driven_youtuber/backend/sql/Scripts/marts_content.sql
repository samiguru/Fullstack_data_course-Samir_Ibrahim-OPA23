desc;


SELECT 
	* 
FROM 
	information_schema.schemata 
WHERE 
	catalog_name = 'youtube_data';

CREATE schema if not exists marts;

CREATE TABLE IF NOT EXISTS marts.content_view_time AS 
(
SELECT
	Videotitel,
	"Publiceringstid för video" AS Publiceringstid,
	Visningar,
	"Visningstid (timmar)" AS Visningstid_timmar,
	Exponeringar,
	Prenumeranter,
	"Klickfrekvens för exponeringar (%)" AS "Klickfrekvens_exponering_%"
FROM
	Innehåll.Tabelldata
ORDER BY
	"Visningstid (timmar)" DESC OFFSET 1);


SELECT * FROM marts.content_view_time;

CREATE TABLE IF NOT EXISTS marts.views_per_date AS (
SELECT
	STRFTIME('%Y-%m-%d',
	Datum) AS Datum,
	Visningar
FROM
	Innehåll.Totalt);


SELECT * FROM marts.views_per_date;


CREATE TABLE IF NOT EXISTS marts.views_per_gender AS (
SELECT 
    "Tittarnas kön" AS "Kön",
    "Visningar (%)" AS "Visningar_%",
    "Genomsnittlig visningslängd",
    "Genomsnittlig procent som har visats (%)" AS "Genomsnittlig_%_visat",
    "Visningstid (timmar) (%)" AS "Visningstid_timmar_%"
FROM 
    Tittare.Tabelldata_alder);

   
SELECT * FROM marts.views_per_gender;


CREATE TABLE IF NOT EXISTS marts.views_per_age AS (
SELECT 
    "Tittarnas ålder" AS "Ålder",
    "Visningar (%)" AS "Visningar_%",
    "Genomsnittlig visningslängd",
    "Genomsnittlig procent som har visats (%)" AS "Genomsnittlig_%_visat",
    "Visningstid (timmar) (%)" AS "Visningstid_timmar_%"
FROM 
    Tittare.Tabelldata_kon 
ORDER BY
    "Ålder");


SELECT * FROM marts.views_per_age;


CREATE TABLE IF NOT EXISTS marts.views_top_10 AS (
SELECT
	 "Videotitel" AS Titel,
	 "Visningar" AS Antal_visningar
FROM
	Innehåll.Tabelldata);



CREATE TABLE IF NOT EXISTS marts.views_top_10 AS (
WITH video_table AS (SELECT * FROM Innehåll.Tabelldata),
     video_diagram AS (SELECT * FROM Innehåll.Diagramdata)
SELECT 
    DISTINCT(vtab."Videotitel"),
    vtab."Publiceringstid för video",
    vtab.visningar AS totala_visningar,
    vtab."Visningstid (timmar)",
    vtab.Prenumeranter,
FROM
    video_table AS vtab
LEFT JOIN video_diagram AS vdia
ON vtab."Publiceringstid för video" = vdia."Publiceringstid för video"
WHERE 
    STRPTIME(vtab."Publiceringstid för video", '%b %d, %Y') >= STRPTIME('2024-01-01', '%Y-%m-%d')
ORDER BY totala_visningar DESC, STRPTIME(vtab."Publiceringstid för video", '%b %d, %Y') DESC LIMIT 10);


SELECT * FROM marts.views_top_10;

CREATE TABLE IF NOT EXISTS marts.views_latest_10 AS (
WITH video_table AS (SELECT * FROM Innehåll.Tabelldata),
     video_diagram AS (SELECT * FROM Innehåll.Diagramdata)
SELECT 
    DISTINCT(vtab."Videotitel"),
    vtab."Publiceringstid för video",
    vtab.visningar AS totala_visningar,
    vtab."Visningstid (timmar)",
    vtab.Prenumeranter,
FROM
    video_table AS vtab
LEFT JOIN video_diagram AS vdia
ON vtab."Publiceringstid för video" = vdia."Publiceringstid för video"
WHERE 
    STRPTIME(vtab."Publiceringstid för video", '%b %d, %Y') >= STRPTIME('2024-01-01', '%Y-%m-%d')
ORDER BY (STRPTIME(vtab."Publiceringstid för video", '%b %d, %Y'), totala_visningar) DESC LIMIT 10);


SELECT * FROM marts.views_latest_10;

SELECT * FROM information_schema.tables WHERE table_schema = 'marts';


