from django.shortcuts import render

# Create your views here.

def home(request) :
	string = '大艺数-app'
	appList = ['App', '小程序', 'H5', '新媒体']
	appMap = {'site': '大艺数', 'numbers': '25'}
	List = map(str, range(100))
	return render(request, 'app/home.html', {'str':string, 'appList':appList, 'appMap':appMap, 'List': List})

