SELECT * FROM youtube;

SELECT DISTINCT category FROM youtube;

SELECT
	count(category) AS number_in_science
FROM
	youtube
WHERE
	category = 'Science & Technology';


SELECT
	"youtuber name", category
FROM
	youtube
WHERE
	category = 'Science & Technology';
	

SELECT
	* EXCLUDE ("youtuber name", "avg views")
FROM
	youtube
WHERE
	category = 'Science & Technology'
	OR category = 'Education';


SELECT DISTINCT "audience country" FROM youtube;


SELECT * FROM youtube WHERE "audience country" = 'Japan';

	
SELECT
	"audience country",
	COUNT(*) AS number_youtubers
FROM
	youtube
GROUP BY
	"audience country"
ORDER BY 
	number_youtubers DESC LIMIT 10;
	
SELECT
	category,
	COUNT(*) AS number
FROM
	youtube
GROUP BY
	category
ORDER BY
	number DESC;
	

SELECT "avg comments" FROM youtube;


SELECT
	"youtuber name",
	CASE 
		WHEN "avg comments" = 'N/A' THEN 0
		WHEN "avg comments" LIKE '%K' THEN CAST(replace("avg comments", 'K', '') AS float) *1000
		ELSE CAST("avg comments" AS integer)
	END AS avg_comments,
FROM
	youtube
ORDER BY avg_comments DESC;


SELECT * FROM youtube;