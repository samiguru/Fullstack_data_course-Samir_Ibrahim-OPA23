desc;


CREATE TABLE IF NOT EXISTS marts.viewer_content_geografy AS (
SELECT 
	Geografi, 
	Visningar,
	"Genomsnittlig visningslängd"
FROM 
	geografi.tabelldata
ORDER BY 
	"Visningar" DESC);


SELECT * FROM marts.viewer_content_geografy;


CREATE TABLE IF NOT EXISTS marts.views_per_op_system AS (
SELECT 
    Operativsystem,
    SUM(Visningar) AS Totala_visningar
FROM 
    operativsystem.diagramdata
GROUP BY 
    Operativsystem
ORDER BY 
    Totala_visningar DESC);
   
   
SELECT * FROM marts.views_per_op_system;


CREATE TABLE IF NOT EXISTS marts.subscribers AS (
SELECT 
        "Prenumerationskälla",
        SUM(Prenumeranter) AS Totala_prenumeranter,
        SUM("Nya prenumeranter") AS Totala_nya_prenumeranter,
        SUM("Förlorade prenumeranter") AS Totala_förlorade_prenumeranter
    FROM 
        Prenumerationskälla.Tabelldata
    GROUP BY 
        "Prenumerationskälla");
       

SELECT * FROM marts.subscribers;
