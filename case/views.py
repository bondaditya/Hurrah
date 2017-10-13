from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Product, Forcast, Demand 
from .forms import ProductForm, ForcastForm 
from django.shortcuts import render_to_response
from django.template.context import RequestContext




@login_required
def ProductCreateView(request):
	form = ProductForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.user = request.user 
		instance.save()
		messages.success(request, "Successfully Created")

	context = {
	'form':form,
	'demand': Demand.objects.get(id=1)

	}	
	return render(request,"form.html",context)

@login_required
def ForcastCreateView(request):
	form = ForcastForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.user = request.user 
		instance.save()

	context = {
	'form':form,
	'demand': Demand.objects.get(id=1)
	}
	return render(request,"forcast.html",context)


def IntroductionView(request):
	return render(request,'intro.html')