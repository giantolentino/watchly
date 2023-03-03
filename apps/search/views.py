from django.shortcuts import render


def search(request):
    # Handle the search functionality here
    return render(request, "search/results.html")
