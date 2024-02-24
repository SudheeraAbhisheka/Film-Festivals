
CREATE VIEW AwardName AS
SELECT awardname
FROM Awards
WHERE category = 'Best movie' AND festivalname = ANY(SELECT festivalname
                                                    FROM Winners
                                                    WHERE bestmovie = 'Ceasar Must Die');

SELECT awardname
FROM AwardName;     