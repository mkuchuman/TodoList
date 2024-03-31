from django import forms

from .models import Tag, Task


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = "__all__"


class TaskForm(forms.ModelForm):
    tag = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(), widget=forms.CheckboxSelectMultiple
    )

    deadline = forms.DateTimeField(
        required=False,
        widget=forms.DateTimeInput(
            attrs={
                "class": "form-control",
                "placeholder": "Select a datetime",
                "type": "datetime-local",
            }
        ),
    )

    class Meta:
        model = Task
        fields = "__all__"
