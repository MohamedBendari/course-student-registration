from django.shortcuts import render
from .forms import StudentForm

def register_student(request):
    success = False
    student = None

    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save()
            success = True
    else:
        form = StudentForm()

    return render(request, 'registration/register.html', {'form': form, 'success': success, 'student': student})
