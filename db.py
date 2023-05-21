import psycopg2


connection = psycopg2.connect(host='localhost', dbname='youtube',
                               user='postgres', password='3107asdzxc')
cursor=connection.cursor()
data = first.pars()
n=0
while n<100:
    rang=data[n][0]
    name=data[n][1]
    channel=data[n][2]
    views = data[n][3]
    insert_query= f"""INSERT INTO public.youtube(
	                    id, name, channel, views)
	                    VALUES ({rang}, '{name}', '{channel}', '{views}');"""
    cursor.execute(insert_query)
    connection.commit()
    n+=1

def get():
    connection = psycopg2.connect(host='localhost', dbname='youtube',
                                  user='postgres', password='3107asdzxc')
    cursor=connection.cursor()
    cursor.execute(SELECT * from )