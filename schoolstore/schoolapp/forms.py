from django import forms
from .models import Student, Material,Department, Course
from bootstrap4.widgets import RadioSelectButtonGroup

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

    materials_provide = forms.ModelMultipleChoiceField(
        queryset=Material.objects.all(),
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'custom-checkbox'}),
        required=False
    )
    department = forms.ModelChoiceField(queryset=Department.objects.all(), empty_label="Select Department")
    course = forms.ModelChoiceField(queryset=Course.objects.none(), empty_label="Select Course")


