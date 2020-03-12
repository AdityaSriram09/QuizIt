from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
	return render(request,'accounts/home.html')

def register(request):
	if request.method=='Post':
		form= UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/account')
	else:
		form = UserCreationForm()

		args={'form':form}
		return render(request,'accounts/reg_form.html',args)