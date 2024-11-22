from django.shortcuts import render,redirect
from author.forms import AuthorForm
# Create your views here.
def add_author(request):
    if request.method == 'POST':
        author_form = AuthorForm(request.POST)
        if author_form.is_valid():
            author_form.save()
            return redirect('add_author')
    else:
        author_form = AuthorForm()
    return render(request, 'author/add_author.html', {'form' : author_form})