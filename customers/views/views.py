from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from customers.models import Customer
from customers.forms import CustomerModelForm


# Create your views here.


def project_management(request):
    return render(request, 'customers/project-management.html')


def customers(request):
    search = request.GET.get('search')
    filter_date = request.GET.get('filter', '')
    customers = Customer.objects.all()
    if search:
        customers = customers.filter(Q(full_name__icontains=search) | Q(email__icontains=search))
    if filter_date == 'filter_date':
        customers = customers.order_by('-created_at')
    context = {'customers': customers}
    return render(request, 'customers/customers.html', context)


def customer_details(request, customer_slug):
    customer = Customer.objects.get(slug=customer_slug)
    context = {'customer': customer}
    return render(request, 'customers/customer-details.html', context)


def profile(request):
    return render(request, 'customers/profile.html')


def profile_settings(request):
    return render(request, 'customers/settings.html')


def add_customer(request):
    form = CustomerModelForm()
    if request.method == 'POST':
        form = CustomerModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('customers')

    context = {'form': form}

    return render(request, 'customers/add-customer.html', context)


def edit_customer(request, customer_slug):
    customer = get_object_or_404(Customer, slug=customer_slug)
    form = CustomerModelForm(instance=customer)
    if request.method == 'POST':
        form = CustomerModelForm(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customers', )
    return render(request, 'customers/settings.html', {'form': form, 'customer': customer})


def delete_customer(request, customer_slug):
    customer = get_object_or_404(Customer, slug=customer_slug)
    if customer:
        customer.delete()
        return redirect('customers')
