from django.shortcuts import render
def index(request):
      a = "<table border = 1><tr><td>xuiasdasdas</td><td>xuiasdasdas</td><td>xuiasdasdas</td></tr></table>"
      return render(request, 'polls/first.html',{'data':a})
