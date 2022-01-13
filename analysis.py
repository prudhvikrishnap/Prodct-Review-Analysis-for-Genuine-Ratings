import pymysql

from matplotlib import pyplot as plt

connection = pymysql.connect(
host='localhost',
user='root',
password='',
db='project',
)
company_ratings = {}
try:
with connection.cursor() as cursor:
        sql = "SELECT * from ratings"
try:
            cursor.execute(sql)
            result = cursor.fetchall()

for row in result:
if row[0] not in company_ratings:
                    company_ratings[row[0]] = (row[1] + row[2] + row[3] + row[4])/4
else:

                    avg = (row[1] + row[2] + row[3] + row[4])/4
if avg != 0:
                      company_ratings[row[0]] = (company_ratings[row[0]] + avg)/2


except:
print("Oops! Something wrong")
    plt.style.use("fivethirtyeight")
    company = company_ratings.keys()
    rating = company_ratings.values()
    plt.bar(company, rating, color="#444444", label="rating")
    plt.title("SURVEY ANALYSIS")
    plt.xlabel("Brands")
    plt.ylabel("Points")
    plt.legend()
    plt.show()

    connection.commit()
finally:
    connection.close()
