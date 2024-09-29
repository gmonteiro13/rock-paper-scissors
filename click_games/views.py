from django.shortcuts import render
from django.views import View
from click_games.forms import LoginForm

# Create your views here.
class LoginView(View):
    def get(self, request):
        contexto = {
            'form': LoginForm()
        }
        return render(request, 'login.html', contexto)
    
    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            return render(request, 'sucesso.html')
        else:
            return render(request, 'login.html', {'form': form})