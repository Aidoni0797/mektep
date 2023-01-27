from django.shortcuts import redirect, render, get_object_or_404
from .models import *

from .forms import *
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordChangeView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views import View
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required

from .forms import RegisterForm, LoginForm, UpdateUserForm, UpdateProfileForm
from .forms import UploadFileForm
from django.views.decorators.csrf import ensure_csrf_cookie
 

def editcompany(request,pk):
    company=Company.objects.get(id=pk)
    if request.method=='POST':
        form=CompForm(request.POST,request.FILES,instance=company)
        if form.is_valid():
            form.save()
            return redirect('main_page')
    else:
        form=CompForm(instance=company)
    return render(request,'handbook/comp_edit.html',{'form':form})


def upload_display_video(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            #print(file.name)
            handle_uploaded_file(file)
            return render(request, "handbook/upload-display-video.html", {'filename': file.name})
    else:
        form = UploadFileForm()
    return render(request, 'handbook/upload-display-video.html', {'form': form})

def handle_uploaded_file(f):
    with open(f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def addnewcomp(request):
    if request.method=='POST':
        form=CompForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('main_page')
    else:
        form=CompForm()
    return render(request,'handbook/newcompform.html',{'form':form})

def addnewtest(request):
    if request.method=='POST':
        form=CompForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('main_page')
    else:
        form=CompForm()
    return render(request,'handbook/newtestform.html',{'form':form})

def createnewquestion(request):
    if request.method=='POST':
        question_title=request.POST.get('newquestionn')
        answer1 = AnswerModel(text=request.POST.get('newanswer1'))
        answer1.save()
        answer2 = AnswerModel(text=request.POST.get('newanswer2'))
        answer2.save()
        answer3 = AnswerModel(text=request.POST.get('newanswer3'))
        answer3.save()
        answer4 = AnswerModel(text=request.POST.get('newanswer4'))
        answer4.save()
        rightanswer = request.POST.get('answer')

        if rightanswer=='1':
            question=QuestionModel(text=question_title,correct_answer=answer1,author=request.user)
            question.save()
            question.other_answers.add(answer2)
            question.other_answers.add(answer3)
            question.other_answers.add(answer4)
            question.save()
        elif rightanswer=='2':
            question = QuestionModel(text=question_title, correct_answer=answer2,author=request.user)
            question.save()
            question.other_answers.add(answer1)
            question.other_answers.add(answer3)
            question.other_answers.add(answer4)
            question.save()
        elif rightanswer=='3':
            question = QuestionModel(text=question_title, correct_answer=answer3,author=request.user)
            question.save()
            question.other_answers.add(answer1)
            question.other_answers.add(answer2)
            question.other_answers.add(answer4)
            question.save()
        elif rightanswer=='4':
            question = QuestionModel(text=question_title, correct_answer=answer4,author=request.user)
            question.save()
            question.other_answers.add(answer1)
            question.other_answers.add(answer3)
            question.other_answers.add(answer2)
            question.save()
        return redirect(createnewtest)
    else:
        return render(request,'handbook/createnewquestion.html')

def createnewtest(request):
    if request.method=='POST':
        title=request.POST.get('title')
        questions=request.POST.get('select_test')
        print(questions)
        return redirect(createnewtest)
    else:
        if QuestionModel.objects.filter(author=request.user).exists:
            query=QuestionModel.objects.filter(author=request.user)
            return render(request,'handbook/createnewtest.html',{'questions':query})
        else:
            return render(request, 'handbook/createnewtest.html', {'questions': []})
def paint(request):
    return render(request,'painting/index.html')

def register(request):

    data = {}

    if request.method == 'POST':
 
        form = RegistrForm(request.POST)

        if form.is_valid():

            form.save()

            data['form'] = form

            data['res'] = "Барлығы өтті"
 
            return render(request, 'handbook/main_page.html', data)
    else: 

        form = RegistrForm()

        data['form'] = form

        return render(request, 'handbook/register.html', data)

def main_page(request):
    return render(request,'handbook/main_page.html',{})

def children(request):
    usser = User.objects.all()
    return render(request,'handbook/children.html',{'usser':usser})

def ishop(request):
    ishops=Company.objects.filter(comapny_category='Internet Shop')
    return render(request,'handbook/ishop.html',{'ishops':ishops})

def smarket(request):
    smarkets=Company.objects.filter(comapny_category='SuperMarket')
    return render(request,'handbook/smarket.html',{'smarkets':smarkets})

def shopping(request):
    shops=Company.objects.filter(comapny_category='Shopping center')
    return render(request,'handbook/shopping.html',{'shops':shops})

def fshop(request):
    fshops=Company.objects.filter(comapny_category='Furniture Shop')
    return render(request,'handbook/fshop.html',{'fshops':fshops})

def icompany(request):
    icomps=Company.objects.filter(comapny_category='IT Company')
    return render(request,'handbook/icomp.html',{'icomps':icomps})

def edu(request):
    edus=Company.objects.filter(comapny_category='Educational Center')
    return render(request,'handbook/edu.html',{'edus':edus})

def company_detail(request,pk):
    try:
        Fcompany=get_object_or_404(Company,pk=pk)
        rate=Rate.objects.filter(id=pk)
        return render(request,'handbook/details.html',{'company':Fcompany,'rating':rate})
    except ObjectDoesNotExist:
        return render(request,'handbook/main_page.html',{})
    
# Create your views here.

def home(request):
    return render(request, 'users/home.html')


class RegisterView(View):
    form_class = RegisterForm
    initial = {'key': 'value'}
    template_name = 'users/register.html'

    def dispatch(self, request, *args, **kwargs):
        # will redirect to the home page if a user tries to access the register page while logged in
        if request.user.is_authenticated:
            return redirect(to='/')

        # else process dispatch as it otherwise normally would
        return super(RegisterView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            messages.success(request, f'{username} қолданушысына аккаунт сәтті құрылды!')

            return redirect(to='login')

        return render(request, self.template_name, {'form': form})


# Class based view that extends from the built in login view to add a remember me functionality
class CustomLoginView(LoginView):
    form_class = LoginForm

    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember_me')

        if not remember_me:
            # set session expiry to 0 seconds. So it will automatically close the session after the browser is closed.
            self.request.session.set_expiry(0)

            # Set session as modified to force data updates/cookie to be saved.
            self.request.session.modified = True

        # else browser session will be as long as the session cookie time "SESSION_COOKIE_AGE" defined in settings.py
        return super(CustomLoginView, self).form_valid(form)


class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'users/password_reset.html'
    email_template_name = 'users/password_reset_email.html'
    subject_template_name = 'users/password_reset_subject'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "Өтініш, дұрыс ақпарат еңгізіңіз..."
    success_url = reverse_lazy('users-home')


class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'users/change_password.html'
    success_message = "Successfully Changed Your Password"
    success_url = reverse_lazy('users-home')


@login_required
def profile(request):
    if request.method == 'POST':
        return render(request, 'users/profile.html')
        # user_form = UpdateUserForm(request.POST, instance=request.user)
        # profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.users.profile)

        # if user_form.is_valid() and profile_form.is_valid():
        #     user_form.save()
        #     profile_form.save()
        #     messages.success(request, 'Your profile is updated successfully')
        #     return redirect(to='users-profile')
    else:
       user_form = UpdateUserForm(instance=request.user)
       #profile_form = UpdateProfileForm(instance=request.user.profile)
        
    # return render(request, 'users/profile.html')#, {'user_form': user_form, 'profile_form': profile_form})
