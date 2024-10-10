desc;

WITH 
	date_table AS (SELECT * FROM datum.tabelldata OFFSET 1),
	date_total AS (SELECT * FROM datum.totalt OFFSET 1)
SELECT 
	STRFTIME('%Y-%m-%d', tot.datum), 
	tot.visningar,
	tab.visningar,
	tab."visningstid (timmar)"
FROM date_total as tot
LEFT JOIN date_table as tab 
ON tot.datum = tab.datum;

SELECT Enhetstyp, count(*) total_rows, sum(Visningar) as total_visningar 
from 
Enhetstyp.Diagramdata group by Enhetstyp;

select * from Enhetstyp.Diagramdata d;

SELECT * EXCLUDE (Innehåll) FROM  Innehåll.Tabelldata ORDER BY "Visningstid (timmar)" DESC OFFSET 1 LIMIT 5;

SELECT * FROM  Innehåll.Diagramdata;

SELECT STRFTIME('%Y-%m-%d', Datum), Visningar FROM Innehåll.Totalt;