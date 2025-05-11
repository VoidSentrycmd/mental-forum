from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import Thread, Comment

class ThreadListView(ListView):
    model = Thread
    template_name = 'threads/thread_list.html'
    context_object_name = 'threads'
    queryset = Thread.objects.filter(parent__isnull=True).order_by('-created_at')

class ThreadDetailView(DetailView):
    model = Thread
    template_name = 'threads/thread_detail.html'
    context_object_name = 'thread'

class ThreadCreateView(LoginRequiredMixin, CreateView):
    model = Thread
    template_name = 'threads/thread_form.html'
    fields = ['title', 'content', 'parent']
    success_url = reverse_lazy('threads:thread_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ThreadUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Thread
    template_name = 'threads/thread_form.html'
    fields = ['title', 'content', 'parent']
    success_url = reverse_lazy('threads:thread_list')

    def test_func(self):
        return self.request.user == self.get_object().author

class ThreadDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Thread
    template_name = 'threads/thread_confirm_delete.html'
    success_url = reverse_lazy('threads:thread_list')

    def test_func(self):
        return self.request.user == self.get_object().author

def add_comment(request, pk):
    thread = get_object_or_404(Thread, pk=pk)
    if request.method == 'POST' and request.user.is_authenticated:
        content = request.POST.get('content', '').strip()
        if content:
            Comment.objects.create(thread=thread, author=request.user, content=content)
    return redirect('threads:thread_detail', pk=pk)
