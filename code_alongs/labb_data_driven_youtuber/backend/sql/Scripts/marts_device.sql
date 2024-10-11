desc;

CREATE table if not exists marts.views_device_per_date AS (
SELECT
	STRFTIME('%Y-%m-%d',
	datum) AS Datum,
	Enhetstyp,
	sum(Visningar) AS Visningar
FROM
	enhetstyp.diagramdata d
GROUP BY
	(datum,
	Enhetstyp )
ORDER BY 
	Datum ASC );
	

SELECT * FROM marts.views_device_per_date;


CREATE TABLE IF NOT EXISTS marts.device_overview AS (
SELECT
	Enhetstyp,
	Visningar,
	"Visningstid (timmar)" AS Visningstid_timmar,
	"Genomsnittlig visningslängd" AS Visningslängd_genomsnitt
FROM
	enhetstyp.tabelldata );


SELECT * FROM marts.device_overview;