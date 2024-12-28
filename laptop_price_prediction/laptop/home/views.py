from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib import messages
from django.core.exceptions import ValidationError
import numpy as np
import joblib
from django.contrib.auth import authenticate, login as auth_login

# Load your model
model = joblib.load('static/laptop_price_prediction')

def prediction(request):
    output = None 

    if request.method == 'POST':
        try:
            # Fetching form values safely and converting them to the required data types
            company = int(request.POST.get('company', 0))  # Company selection as integer
            device_type = int(request.POST.get('type', 0))  # Type of device
            screen_resolution = int(request.POST.get('screen_resolution', 0))  # Screen resolution
            cpu = int(request.POST.get('cpu', 0))  # CPU selection
            memory = int(request.POST.get('memory', 0))  # Memory selection
            gpu = int(request.POST.get('gpu', 0))  # GPU selection
            os = int(request.POST.get('os', 0))  # Operating system selection

            # Additional features that are missing in the form but are required by the model
            ram = int(request.POST.get('ram', 8))  # Default RAM, e.g., 8GB
            storage = int(request.POST.get('storage', 512))  # Default Storage, e.g., 512GB
            battery = float(request.POST.get('battery', 50.0))  # Default battery life or size
            weight = float(request.POST.get('weight', 1.5))  # Default weight in kg
            screen_size = float(request.POST.get('screen_size', 15.6))  # Default screen size in inches

            # Combine all inputs into a single array for model prediction
            input_data = np.array([[company, device_type, screen_resolution, cpu, memory, gpu, os,
                                    ram, storage, battery, weight, screen_size]])

            # Predicting using the model
            pred = model.predict(input_data)
            output = f"Prediction: {pred[0]}"

        except ValueError as e:
            output = f"Error: {str(e)}"

    return render(request, 'prediction.html', {'output': output})

# Create your views here.

def index(request):
    return render(request,'index.html')


def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)  # Use Django's login function
            return redirect('home')  # Redirect to home page or any desired page
        else:
            # Handle invalid login
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    else:
        return render(request, 'login.html')
    

def signup(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email_or_phone')  # Adjusted field name to match the form
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # Check if passwords match
        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return render(request, 'signup.html')

        # Check if username is already taken
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username is already taken.")
            return render(request, 'signup.html')

        # Check if username is alphanumeric and not purely numeric
        if not username.isalnum() or username.isnumeric():
            messages.error(request, "Username must contain both letters and numbers, and it can't be purely numeric.")
            return render(request, 'signup.html')

        # Create the user and set additional fields
        try:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.first_name = first_name  # Set first name
            user.last_name = last_name  # Set last name
            user.save()

            messages.success(request, "Account created successfully.")
            return redirect('login')  # Redirect to login page after successful signup
        except ValidationError as e:
            messages.error(request, str(e))
            return render(request, 'signup.html')

    return render(request, 'signup.html')




def profile(request):
    if request.user.is_authenticated:
        return render(request, 'profile.html', {'user': request.user})
    else:
        return redirect('login')  # Redirect to login if not authenticated
