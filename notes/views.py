from django.shortcuts import render, redirect, get_object_or_404
from .models import Note

def home(request):
    query = request.GET.get("q", "")
    if query:
        notes = Note.objects.filter(title__icontains=query)
    else:
        notes = Note.objects.all()
    return render(request, "home.html", {"notes": notes, "query": query})

def add_note(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        if title and description:
            Note.objects.create(title=title, description=description)
            return redirect("home")
    return render(request, "add_note.html")

def view_note(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    return render(request, "view_note.html", {"note": note})

def delete_note(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    note.delete()
    return redirect("home")
