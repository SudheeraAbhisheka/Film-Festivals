# creating the for festival deatails
CREATE TABLE Festivals(
festivalname VARCHAR(50) PRIMARY KEY,
countryoforigin VARCHAR(50) NOT NULL,
startupyear CHAR(4) NOT NULL
);

# creating the table for the Awards awarded in perticular festival
CREATE TABLE Awards(
festivalname VARCHAR(50) NOT NULL,
category VARCHAR(50) NOT NULL,
awardname VARCHAR(50) NOT NULL,
PRIMARY KEY(festivalname, category),
FOREIGN KEY (festivalname)
REFERENCES Festivals(festivalname)
);

# creating the table to add all the data about winners 
CREATE TABLE Winners(
festivalname VARCHAR(50) NOT NULL,
year CHAR(50) NOT NULL,
bestmovie VARCHAR(50) NOT NULL,
bestdirector VARCHAR(50) NOT NULL,
country_of_the_bestdirector VARCHAR(50) NOT NULL,
bestactress VARCHAR(50) NOT NULL,
birthday_of_bestactress DATE NOT NULL,
PRIMARY KEY(festivalname, year),
FOREIGN KEY (festivalname)
REFERENCES Festivals(festivalname)
);