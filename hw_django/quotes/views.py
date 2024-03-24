from django.shortcuts import render, redirect
from django.views.decorators.cache import never_cache
from django.core.paginator import Paginator
from .forms import AuthorForm, QuoteForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test

from .models import Author
from .utils import get_mongo

def main(request, page=1):
    db = get_mongo()
    quotes = db.quotes.find()
    per_page = 10
    paginator = Paginator(list(quotes), per_page)
    quotes_page = paginator.page(page)
    return render(request, 'quotes/index.html', context={'quotes': quotes_page})


@login_required
def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            new_author = Author(
                fullname=form.cleaned_data['fullname'],
                born_date=form.cleaned_data['born_date'],
                born_location=form.cleaned_data['born_location'],
                description=form.cleaned_data['description'],
            )
        try:
            new_author.save()
        except Exception as e:
            print("Error saving author:", e)
        else:
            return redirect('quotes:root')
    else:
        form = AuthorForm()
    return render(request, 'quotes/add_author.html', {'form': form})


@login_required
def add_quote(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            quote = form.save()
            return redirect('quotes:root')
    else:
        form = QuoteForm()
    return render(request, 'quotes/add_quote.html', {'form': form})


def author_detail(request, author_id):
    author = Author.objects.get(id=author_id)
    return render(request, 'quotes/author_detail.html', {'author': author})


def author_list(request):
    author = Author.objects.all()
    context = {'authors': author}
    return render(request, 'quotes/show.html', context)

# def detail(request, note_id):
#     note = get_object_or_404(Note, pk=note_id, user=request.user)
#     return render(request, 'noteapp/detail.html', {"note": note})


# @never_cache
# def author_detail(request, author_id):
#     author = Author.objects.get(pk=author_id)


# def anonymous_required(view_function, redirect_to=None):
#     """
#     Decorator for views that checks that the user is anonymous, redirecting
#     to the login page if necessary.
#     """
#     actual_decorator = user_passes_test(
#         lambda u: u.is_anonymous,
#         login_url=redirect_to,
#     )
#     if view_function:
#         return actual_decorator(view_function)
#     return actual_decorator