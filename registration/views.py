from django.shortcuts import render,redirect
from app.models import Registration, Event
from django.http import HttpResponse
def HOME(request):
    return render(request,'home.html')
def register(request):
    if request.method == 'POST':
        # Extract individual records from the form
        name = request.POST.get('name')
        college = request.POST.get('college')
        technical_events = request.POST.getlist('technical_events')  # Use getlist for multiple selections
        non_technical_events = request.POST.getlist('non_technical_events')  # Optional field, use getlist

        phone = request.POST.get('phone')
        email = request.POST.get('email')

        # Create a new Registration instance
        registration = Registration(
            name=name,
            college=college,
            phone=phone,
            email=email
        )
        registration.save()  # Save the registration first

        # Add selected technical events
        for event_name in technical_events:
            event_instance, created = Event.objects.get_or_create(name=event_name, event_type='technical')
            registration.technical_events.add(event_instance)

        # Add selected non-technical events if any
        for event_name in non_technical_events:
            event_instance, created = Event.objects.get_or_create(name=event_name, event_type='non_technical')
            registration.non_technical_events.add(event_instance)

        # After saving, you can redirect to a success page or show a success message
        return HttpResponse('Registration successful!')  # Or redirect to another page

    return render(request, 'home.html')
