CREATE PROCEDURE AllAwards()
COMMENT 'select all columns from awards.'
SELECT * FROM Awards;

CALL AllAwards();
