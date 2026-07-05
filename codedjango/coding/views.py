from django.shortcuts import render
from .models import CodingChallenge, CodingReview, UserBookmark, CodingSolution
from .forms import CodingChallengeForm
from django.shortcuts import get_object_or_404

# Create your views here.
def all_coding(request):
    codings = CodingChallenge.objects.all()
    return render(request, 'coding/all_coding.html', {'codings': codings})


def coding_detail(request, coding_id):
    coding = get_object_or_404(CodingChallenge, pk=coding_id)
    return render(request, 'coding/coding_detail.html', {'coding': coding})


def code_store(request):
    stores = None
    if request.method == 'POST':
        form = CodingChallengeForm(request.POST)
        if form.is_valid():
            code_challenge = form.cleaned_data['code_challenge']
            stores = CodingChallenge.objects.filter(id=code_challenge.id)
    else:
        form = CodingChallengeForm()
    return render(request, 'coding/code_store.html', {'stores': stores, 'form': form})