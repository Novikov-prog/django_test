from django.shortcuts import render


def home(request):
    return render(request, 'home.html')

def reverse(request):
    user_text = request.GET['usertext'] # requete du texte inseré + l'affichage
    reversed_text = user_text[::-1] # la formule réinversante du texte
    return render(request, 'reverse.html', {'usertext':user_text, 'reversedtext':reversed_text})