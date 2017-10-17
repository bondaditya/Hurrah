from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Product, Forcast, Demand , Product2, Product3, Product4
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
		print(request, "Successfully Created")
		return redirect('reports')

	context = {
	'form':form,
	'demand': Demand.objects.get(id=1)

	}	
	return render(request,"form.html",context)

@login_required
def ProductCreateView2(request):
	form = ProductForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.user = request.user 
		instance.save()
		print(request, "Successfully Created")
		return redirect('reports')

	context = {
	'form':form,
	'demand': Demand.objects.get(id=1)

	}	
	return render(request,"form2.html",context)

@login_required
def ProductCreateView3(request):
	form = ProductForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.user = request.user 
		instance.save()
		print(request, "Successfully Created")
		return redirect('reports')

	context = {
	'form':form,
	'demand': Demand.objects.get(id=1)

	}	
	return render(request,"form3.html",context)

@login_required
def ProductCreateView4(request):
	form = ProductForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.user = request.user 
		instance.save()
		print(request, "Successfully Created")
		return redirect('reports')

	context = {
	'form':form,
	'demand': Demand.objects.get(id=1)

	}	
	return render(request,"form4.html",context)

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

def ReportView(request):
	context = {
	'product':Product.objects.filter(id=request.user.id).first(),
	'product2':Product2.objects.filter(id=request.user.id).first(),
	'product3':Product3.objects.filter(id=request.user.id).first(),
	'product4':Product4.objects.filter(id=request.user.id).first(),
	

	}
	return render(request,'reports.html',context)