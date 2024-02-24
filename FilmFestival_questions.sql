#1
SELECT bestdirector
FROM Winners 
WHERE country_of_the_bestdirector = 'United States';

#2
SELECT bestactress, TRUNCATE((DATEDIFF(SYSDATE(), birthday_of_bestactress))/365.25, 0) AS age
FROM Winners
ORDER BY age;

#3
SELECT year, bestdirector, country_of_the_bestdirector
FROM Winners
ORDER BY country_of_the_bestdirector;

#4
SELECT festivalname
FROM Festivals
WHERE startupyear < 1950;

#5
SELECT Festivals.festivalname, bestdirector, country_of_the_bestdirector
FROM Winners RIGHT OUTER JOIN Festivals ON
Winners.country_of_the_bestdirector = Festivals.countryoforigin;

#6
SELECT bestmovie, year
FROM Winners JOIN Awards ON
awardname = 'Golden bear' AND Awards.festivalname = Winners.festivalname;

#7
SELECT awardname
FROM Awards
WHERE category = 'Best movie' AND festivalname = ANY(SELECT festivalname
                                                    FROM Winners
                                                    WHERE bestmovie = 'Ceasar Must Die');

#8
SELECT awardname
FROM Awards
WHERE category = 'Best director' AND festivalname = ANY(SELECT festivalname
                                                    FROM Winners
                                                    WHERE bestdirector = 'Roman Polanski');                                                   

#9
SELECT festivalname, MAX(TRUNCATE((DATEDIFF(SYSDATE(), birthday_of_bestactress))/365.25, 0)) AS age
FROM Winners
GROUP BY festivalname;

#10
SELECT country_of_the_bestdirector, COUNT(country_of_the_bestdirector) AS 'No of best directors'
FROM Winners
GROUP BY country_of_the_bestdirector;
