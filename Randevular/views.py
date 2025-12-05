from django.shortcuts import render


def randevu_al(request):
    return render(request, 'Randevu.html', {'title': 'Randevu Sayfası'})


def psikologlar(request):
    return render(request, 'Psikologlar.html', {'title': 'Psikologlar Sayfası'})
