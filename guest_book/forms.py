from django import forms
from .models import Guest
from .models import Question



class GuestForm(forms.ModelForm):
    class Meta:
        model = Guest
        fields = ['name']



from django import forms
from .models import Question

class QuestionnaireForm(forms.Form):
    def __init__(self, *args, **kwargs):
        questions = kwargs.pop('questions')
        super(QuestionnaireForm, self).__init__(*args, **kwargs)
        for question in questions:
            field_name = f'question_{question.id}'
            if question.question_type == 'text':
                self.fields[field_name] = forms.CharField(
                    label=question.text,
                    widget=forms.Textarea(attrs={'rows': 3, 'cols': 40}),  # הגדרת גודל מותאם
		    required=True
                )
            elif question.question_type == 'multiple_choice':
                choices = [(option.strip(), option.strip()) for option in question.options.split(',')]
                self.fields[field_name] = forms.ChoiceField(
                    label=question.text,
                    widget=forms.RadioSelect,
                    choices=choices,
                    required=True
                )


from django.contrib.auth.forms import AuthenticationForm

class CustomLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(CustomLoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = 'משתמש'
        self.fields['password'].label = 'סיסמה'



from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CustomRegisterForm(UserCreationForm):
    username = forms.CharField(label='משתמש', max_length=150)
    password1 = forms.CharField(label='סיסמה', widget=forms.PasswordInput)
    password2 = forms.CharField(label='אישור סיסמה', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

