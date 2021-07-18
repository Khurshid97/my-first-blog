from django.shortcuts import render

# Create your views here.
def home(request):
    new = ""
    n = request.GET.get('n')
    if 'Yo' in n:
        new += 'Ё'
    if 'Yu' in n:
        new += 'Ю'
    if 'Ch' in n:
        new += 'Ч'
    if 'Sh' in n:
        new += 'Ш'
    if "O'" in n:
        new += 'Ў'
    if "G'" in n:
        new += 'Ғ'
    for q in n:
        if 'A' == q:
            new += 'А'
        elif 'B' == q:
            new += 'Б'
        elif 'D' == q:
            new += 'Д'
        elif 'E' == q:
            new += 'Э'
        elif 'E' == q:
            new += 'Е'
        elif 'F' == q:
            new += 'Ф'
        elif "G" == q:
            new += 'Г'
        elif 'H' == q:
            new += 'Ҳ'
        elif 'I' == q:
            new += 'И'
        elif 'J' == q:
            new += 'Ж'
        elif 'K' == q:
            new += 'К'
        elif 'L' == q:
            new += 'Л'
        elif 'M' == q:
            new += 'М'
        elif 'N' == q:
            new += 'Н'
        elif 'O' == q:
            new += 'О'
        elif 'P' == q:
            new += 'П'
        elif 'Q' == q:
            new += 'Қ'
        elif 'R' == q:
            new += 'Р'
        elif 'S' == q:
            new += 'С'
        elif 'T' == q:
            new += 'Т'
        elif 'U' == q:
            new += 'У'
        elif 'V' == q:
            new += 'В'
        elif 'X' == q:
            new += 'Х'
        elif 'Z' == q:
            new += 'З'
        elif ' ' == q:
            new += " "
        elif 'a' == q:
            new += 'а'
        elif 'b' == q:
            new += 'б'
        elif 'd' == q:
            new += 'д'
        elif 'e' == q:
            new += 'э'
        elif 'e' == q:
            new += 'е'
        elif 'f' == q:
            new += 'ф'
        elif 'g' == q:
            new += 'г'
        elif 'h' == q:
            new += 'ҳ'
        elif 'i' == q:
            new += 'и'
        elif 'j' == q:
            new += 'ж'
        elif 'k' == q:
            new += 'к'
        elif 'l' == q:
            new += 'л'
        elif 'm' == q:
            new += 'м'
        elif 'n' == q:
            new += 'н'
        if 'o' == q:
            new += 'о'
        elif 'p' == q:
            new += 'п'
        elif 'q' == q:
            new += 'қ'
        elif 'r' == q:
            new += 'р'
        elif 's' == q:
            new += 'с'
        elif 't' == q:
            new += 'т'
        elif 'u' == q:
            new += 'у'
        elif 'v' == q:
            new += 'в'
        elif 'x' == q:
            new += 'х'
        elif 'y' == q:
            new += 'й'
        elif 'z' == q:
            new += 'з'
        elif "o'" == q:
            new += 'ў'
        elif "g'" == q:
            new += 'ғ'
        elif 'sh' == q:
            new += 'ш'
        elif 'ch' == q:
            new += 'ч'
        elif 'ng' == q:
            new += "нг"
        elif 'yu' == q:
            new += 'ю'
        elif 'yo' == q:
            new += 'ё'

    return render(request, 'blog/home.html', {'new':new})


def about(request):
    return render(request, "blog/about.html")

def contacts(request):
    return render(request, "blog/contacts.html")


def homepage(request):
    return render(request, "blog/homepage.html")

def news(request):
    return render(request, "blog/news.html")