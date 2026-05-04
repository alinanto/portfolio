from django.shortcuts import render
import ipaddress
import os
from django.conf import settings
from .models import Contact, Visit, Contact
import re

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR', '')

    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0].strip()
    else:
        ip = request.META.get('REMOTE_ADDR', '').strip()

    # Validate IP safely
    try:
        ipaddress.ip_address(ip)
        return ip
    except ValueError:
        return None

def get_notes_tree():
    notes_dir = os.path.join(settings.BASE_DIR, 'static', 'notes')
    tree = {}
    if os.path.exists(notes_dir):
        for category in sorted(os.listdir(notes_dir)):
            cat_path = os.path.join(notes_dir, category)
            if os.path.isdir(cat_path):
                pdfs = sorted([f for f in os.listdir(cat_path) if f.endswith('.pdf')])
                if pdfs:
                    tree[category] = pdfs
    return tree

def render_fn(request):
    # Ensure session exists
    if not request.session.session_key:
        request.session.create()

    session_key = request.session.session_key

    # Store only first visit per session
    if not request.session.get('counted'):
        Visit.objects.get_or_create(session_key=session_key)
    request.session['counted'] = True

    # HANDLE FORM SUBMIT
    success = False
    error = False

    if request.method == "POST":
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        message = request.POST.get('message', '').strip()

        #Basic validation
        if name and email and message:
            if re.match(r"[^@]+@[^@]+\.[^@]+", email):

                # Save to DB
                Contact.objects.create(
                    name=name,
                    email=email,
                    message=message
                )

                # Send Email (optional, can be commented out if not configured)
                
                success = True
                print("New Contact Message:")
                print(name, email, message)
            else:
                error = True


    # For now just printing (later we store/send email)

    visit_count = Visit.objects.count()
    notes_tree = get_notes_tree()

    return render(request, 'index.html', {
        'notes_tree': notes_tree,
        'visit_count': visit_count,
        'success': success,
        'error': error
    })