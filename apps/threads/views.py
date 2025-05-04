from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Thread

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
    fields = ['title', 'content']
    success_url = reverse_lazy('threads:thread_list')

    def test_func(self):
        thread = self.get_object()
        return self.request.user == thread.author


class ThreadDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Thread
    template_name = 'threads/thread_confirm_delete.html'
    success_url = reverse_lazy('threads:thread_list')

    def test_func(self):
        thread = self.get_object()
        return self.request.user == thread.author
