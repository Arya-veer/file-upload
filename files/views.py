from .forms import DocumentForm
from django.shortcuts import *
from django.views.generic import DetailView, CreateView, DeleteView,ListView
from .models import Document


def uploadView(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload_url')
    else:
        form = DocumentForm()
    return render(request, 'files/upload_page.html', {
        'form': form
    })
class Files(ListView):
    model = Document
    template_name = 'files/home.html'
    context_object_name = 'files'
