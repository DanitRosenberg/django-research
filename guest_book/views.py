from django.shortcuts import render, redirect
from .models import Guest
from .forms import GuestForm
from django.contrib.auth.decorators import login_required

def guest_list(request):
    guests = Guest.objects.all()
    return render(request, 'guest_book/guest_list.html', {'guests': guests})

def add_guest(request):
    if request.method == 'POST':
        form = GuestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('guest_list')
    else:
        form = GuestForm()
    return render(request, 'guest_book/add_guest.html', {'form': form})

@login_required
def video_page(request):
    return render(request, 'guest_book/video_page.html')


@login_required
def alternative_page(request):
    return render(request, 'guest_book/alternative_page.html')



from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Question, Answer
from .forms import QuestionnaireForm

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def questionnaire_view(request):
    questions = Question.objects.all()
    if request.method == 'POST':
        form = QuestionnaireForm(request.POST, questions=questions)
        if form.is_valid():
            all_yes = True  # נניח שכל התשובות הן "כן"
            for question in questions:
                field_name = f'question_{question.id}'
                answer_text = form.cleaned_data.get(field_name)

                # שמירת התשובה למסד הנתונים
                Answer.objects.update_or_create(
                    user=request.user,
                    question=question,
                    defaults={'answer_text': answer_text}
                )

                # בדיקה אם התשובה היא לא "כן"
                if answer_text.strip() != 'כן':
                    all_yes = False  # אם יש אפילו תשובה אחת לא "כן", מעדכן ל-False

            # הפניה בהתאם לתשובות
            if all_yes:
                return redirect('yes_redirect_page')  # שם הנתיב לדף הצלחה כשכל התשובות כן
            else:
                return redirect('no_redirect_page')  # שם הנתיב לדף אחר כשיש תשובה שונה

    else:
        form = QuestionnaireForm(questions=questions)

    return render(request, 'guest_book/questionnaire.html', {'form': form})


from django.shortcuts import render

def success_view(request):
    return render(request, 'guest_book/success.html')  # מציג את דף ההצלחה
def failure_view(request):
    return render(request, 'guest_book/failure.html')  # מציג דף אחר


from django.shortcuts import render, redirect
from .forms import CustomRegisterForm

def register_view(request):
    if request.method == 'POST':
        form = CustomRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # או כל דף אחר שתבחר
    else:
        form = CustomRegisterForm()
    
    return render(request, 'guest_book/register.html', {'form': form})


from django.contrib.auth.views import LoginView
from .forms import CustomLoginForm  # טופס התחברות עם תוויות בעברית

class CustomLoginView(LoginView):
    form_class = CustomLoginForm
    template_name = 'guest_book/login.html'  # התבנית שלך

from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

@login_required
def conditional_redirect(request):
    user_id = request.user.id  # מזהה המשתמש
    if user_id % 2 == 0:
        return redirect('video_page')  # אם המספר זוגי
    else:
        return redirect('alternative_page')  # אם המספר אי-זוגי

