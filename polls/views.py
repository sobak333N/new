from django.shortcuts import render
# import psycopg2
def index(request):
      # i = 0
      # video_id1 = 1
      #
      # connection = psycopg2.connect(host='localhost', dbname='youtube',
      #                               user='postgres', password='3107asdzxc')
      # cursor = connection.cursor()
      # request = f"select * from youtube where id = {video_id1}"
      # cursor.execute(request)
      # b = cursor.fetchall()
      # a = '''
      #             <img src="{% static 'polls/pictures/line.png' %}">
      #             <div id="pic", align="left">
      #           <img src="{% static 'polls/pictures/h''' + str(b[i][0])+ '''.jpg' %}">
      #       </div>
      #       <div id="text" >
      #           <a> rang ''' +str(b[i][0])+ ''' </a><p> '''+str(b[i][1])+ ''' </p><a> '''+str(b[i][2])+ ''' </a><p>'''+str(b[i][3])+'''</p></div>'''
      #
      # while i < 90 :
      #       a = a + '''
      #             <img src="{% static 'polls/pictures/line.png' %}">
      #       <div id="pic", align="left">
      #           <img src="{% static 'polls/pictures/h''' + str(b[i][0])+ '''.jpg' %}">
      #       </div>
      #       <div id="text" >
      #           <a> rang ''' +str(b[i][0])+ ''' </a><p> '''+str(b[i][1])+ ''' </p><a> '''+str(b[i][2])+ ''' </a><p>'''+str(b[i][3])+'''</p>
      #       </div>
      #       '''
      #       i +=1
      a  = '''
                  <img src="/static/polls/pictures/line.png">
            <div id="pic", align="left">
                <img src="/static/polls/pictures/h''' + str(2) + '''.jpeg">
            </div>
            <div id="text" >
                <a> rang ''' +str(1)+ ''' </a><p> '''+str(2)+ ''' </p><a> '''+str(3)+ ''' </a><p>'''+str(4)+'''</p>
            </div>
            '''
      b = ''
      for i in range(10):
            b += a
      return render(request, 'polls/first.html',{'data':b})
