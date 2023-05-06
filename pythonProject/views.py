

def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def make_plan(request):
    return render(request, 'make_plan.html')


def home(request):
    return render(request, 'home.html')

def profile_page(request):
    return render(request, 'profile_page.html')

def sign_in(request):
    return render(request, 'sign_in.html')


def sign_up(request):
    return render(request, 'sign_up.html')


def reset_with_mail(request):
    return render(request, 'reset_with_mail.html')


def new_pass(request):
    return render(request, 'new_pass.html')

def password_success(request):
    return render(request, "home.html")

def password_change_done(request):
    return redirect('/')
