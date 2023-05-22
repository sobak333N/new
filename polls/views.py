from django.shortcuts import render
import psycopg2
def index(request):
      video_id1 = 1
      connection = psycopg2.connect(host='localhost', dbname='youtube',
                                    user='postgres', password='3107asdzxc')
      cursor = connection.cursor()
      request = f"select * from youtube where id = {video_id1}"
      cursor.execute(request)
      b = cursor.fetchall()

      a = '<a>'+str(b[0][0])+'</a>'+'<p>'+str(b[0][1])+'</p>'+'<a>'+str(b[0][2])+'</a>'+'<p>'+str(b[0][3])+'</p>'
      c = '<a>'+str(b[1][0])+'</a>'+'<p>'+str(b[1][1])+'</p>'+'<a>'+str(b[1][2])+'</a>'+'<p>'+str(b[1][3])+'</p>'
      return render(request, 'polls/first.html',{'data':a} , {'sdata':c})
