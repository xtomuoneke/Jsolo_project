from django.shortcuts import render

def about_us(request):
    return render(request, 'Solo_Project/aboutUs.html')


def admin_dashboard(request):
    return render(request, 'Solo_Project/adminDashboard1.html')