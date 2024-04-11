from django import forms
from .models import Task
from datetime import datetime

class TaskCreateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_to_date', 'status', 'priority']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'due_to_date': forms.SelectDateWidget(years=range(datetime.now().year, datetime.now().year + 5)),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'priority': forms.Select(attrs={'class': 'form-select'}),
        }
    def __init__(self, *args, **kwargs):
        super(TaskCreateForm, self).__init__(*args, **kwargs)
        self.fields['due_to_date'].initial = datetime.now().date()  #


class TaskFilterForm(forms.Form):
    STATUS_CHOICES = [
        ("", "All"),
        ("DONE",'Done'),
        ("TO_DO", "To do"),
        ("IN_PROGRESS", "In progress")
    ]

    status = forms.ChoiceField(choices=STATUS_CHOICES, label="Status", required=False, widget=forms.Select(attrs={"class":"form-select"}))