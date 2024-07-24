from django.shortcuts import render
from django.http import JsonResponse
from .forms import UserForm, AppForm, GroupForm
from .models import User, App, Group

def index(request):
	user_form = UserForm()
	app_form = AppForm()
	group_form = GroupForm()
	return render(request, 'api/index.html', {'user_form': user_form, 'app_form': app_form, 'group_form': group_form})
def get_response(request):
	if request.method == 'POST':
		user_name = request.POST.get('user_name')
		app_name = request.POST.get('app_name')
		group_name = request.POST.get('group_name')
		response_data = {
			'user_name': user_name,
			'app_name': app_name,
			'group_name': group_name
		}
		return JsonResponse(response_data)
	return JsonResponse({'error': 'Invalid request'}, status=400)

def autocomplete(request):
	term = request.GET.get('term')
	user_names = list(User.objects.filter(name__icontains=term).values_list('name', flat=True))
	app_names = list(App.objects.filter(name__icontains=term).values_list('name', flat=True))
	group_names = list(Group.objects.filter(name__icontains=term).values_list('name', flat=True))
	return JsonResponse(user_names + app_names + group_names, safe=False)

# Create your views here.
