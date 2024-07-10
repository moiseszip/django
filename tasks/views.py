from django import forms
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")
    # priority = forms.IntegerField(label="Priority", min_value=1, max_value=10)

# Create your views here.
def index(request):
    # check if there is a list f tasks in that session, if not create one
    if "tasks" not in request.session:
        request.session["tasks"] = []

    return render(request, "tasks/index.html", {
        "tasks": request.session["tasks"]
    })

def add(request):

    if request.method == 'POST':
        # set the data from the form in form var
        form = NewTaskForm(request.POST)
        if form.is_valid():
            # clean the 'task' data and put in task var, then in tasks list
            task = form.cleaned_data["task"]
            request.session["tasks"] += [task]
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            # return form with the user inputs
            return render(request, "tasks/add.html", {
                "form": form
            })

    return render(request, "tasks/add.html", {
        # return add page with new form
        "form": NewTaskForm()
    })
