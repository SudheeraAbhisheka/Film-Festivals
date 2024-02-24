import mysql.connector;

# opening the connection to mysql server
mydb = mysql.connector.connect(host='localhost', database='FilmFestivals_20535197', user = input("user: "), password = input("password: "))

# defining a new cursor
mycursor = mydb.cursor()

print("""
Years between 2010 to 2014
1.	All the best directors from the United States.
2.	Sort out the actresses’ ages when they are getting the award.
3.	Group the Best movies according to the country.
4.	What are the festivals that start up before 1950?
5.	Who are the best directors from as same as festival origin country?
6.	What are the movies that have won the Golden Bear?
7.	What are the awards that “Caesar must die” has won?
8.	What is the award director “Roman Polanski” has won?
9.	Maximum age of actress’s awarded in each festival.
10.	No of best directors from each country.
0.  Exit""")


result = ["Empty"]
number = "111"

while(number != "0"):
    number = input("Enter the number: ")
    if(number == "1"):
        mycursor.execute("SELECT bestdirector FROM Winners  WHERE country_of_the_bestdirector = 'United States'") 
    elif(number == "2"):
        mycursor.execute("SELECT bestactress, TRUNCATE((DATEDIFF(SYSDATE(), birthday_of_bestactress))/365.25, 0) AS age FROM Winners ORDER BY age")
    elif(number == "3"):
        mycursor.execute("SELECT year, bestdirector, country_of_the_bestdirector FROM Winners ORDER BY country_of_the_bestdirector")
    elif(number == "4"):
        mycursor.execute("SELECT festivalname FROM Festivals WHERE startupyear < 1950")
    elif(number == "5"):
        mycursor.execute("SELECT Festivals.festivalname, bestdirector, country_of_the_bestdirector FROM Winners RIGHT OUTER JOIN Festivals ON Winners.country_of_the_bestdirector = Festivals.countryoforigin")
    elif(number == "6"):
        mycursor.execute("SELECT bestmovie, year FROM Winners JOIN Awards ON awardname = 'Golden bear' AND Awards.festivalname = Winners.festivalname")
    elif(number == "7"):
        mycursor.execute("SELECT awardname FROM Awards WHERE category = 'Best movie' AND festivalname = ANY(SELECT festivalname FROM Winners WHERE bestmovie = 'Ceasar Must Die')")
    elif(number == "8"):
        mycursor.execute("SELECT awardname FROM Awards WHERE category = 'Best director' AND festivalname = ANY(SELECT festivalname FROM Winners WHERE bestdirector = 'Roman Polanski')                                               ")
    elif(number == "9"):
        mycursor.execute("SELECT festivalname, MAX(TRUNCATE((DATEDIFF(SYSDATE(), birthday_of_bestactress))/365.25, 0)) AS age FROM Winners GROUP BY festivalname")
    elif(number == "10"):
        mycursor.execute("SELECT country_of_the_bestdirector, COUNT(country_of_the_bestdirector) AS 'No of best directors' FROM Winners GROUP BY country_of_the_bestdirector")
    elif(number == "11"):
        mycursor.execute("INSERT INTO Festivals VALUES ('Oscar Film Festival', 'France', '1929')")
    elif(number == "12"):
        mycursor.execute("SELECT * FROM Festivals")
    elif(number == "13"):
        mycursor.execute("UPDATE Festivals SET startupyear = '1939' WHERE festivalname = 'Oscar Film Festival'")
    else:
        print("Please select one of above query")

    result = mycursor.fetchall()
    for i in result:
        print(i) # printing the final result

# closing the connctor and the cursor
mycursor.execute("SELECT * FROM Festivals") 

#UPDATE Festivals SET startupyear = '1939' WHERE festivalname = 'Oscar Film Festival'


mycursor.close()
mysql.close()





