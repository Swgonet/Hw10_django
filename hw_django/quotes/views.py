from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.cache import never_cache
from django.core.paginator import Paginator
from .forms import AuthorForm, QuoteForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test


from .models import Author, Quote
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
    # author = get_object_or_404(Author, pk=author_id)
    author = Author.objects.get(id=author_id)
    return render(request, 'quotes/author_detail.html', {'author': author})

def all_quotes(request):
    quotes = Quote.objects.all()
    return render(request, 'quotes/all_quotes.html', {'quotes': quotes})


def author_list(request):
    author = Author.objects.all()
    context = {'authors': author}
    return render(request, 'quotes/show.html', context)