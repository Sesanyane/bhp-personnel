from django import forms

from edc_base.sites import SiteModelFormMixin

from ..models import Employee


class EmployeeForm(SiteModelFormMixin, forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        self.fields['identifier'].required = False

    identifier = forms.CharField(
        label='Employee Identifier',
        widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    class Meta:
        model = Employee
        fields = '__all__'
