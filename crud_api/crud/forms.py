from django.forms import ModelForm
from .models import Task


# form for user tasks
class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = 'title', 'description'
