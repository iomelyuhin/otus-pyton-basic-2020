from django.shortcuts import render


def main_view(request):
    return render(request, 'main/index.html')
    # return render(request, 'animals/index.html', {'animals': animals})
