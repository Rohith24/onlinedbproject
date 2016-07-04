from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from models import College
from urlparse import urlparse,parse_qs
class CollegeListView(ListView):
    model = College
    #template_name = "mycolleges.html"
    #context_object_name = "clg_list"
    def get_queryset(self):
        location=self.kwargs.get('location')
        if not location:
            location = self.request.GET.get('location')
        if location:
            return College.objects.filter(location__iexact=location)
        else:
            return super(CollegeListView, self).get_queryset()


class CollegeDetailsView(DetailView):
    model = College
    def get_object(self, queryset=None):
        # pk=self.request.GET.get('pk')
        acronym=self.kwargs.get("acronym")
        if acronym:
            return College.objects.get(acronym__iexact=acronym)
        else:
            return College.objects.get(pk=self.kwargs['pk'])

class CollegeCreateView(CreateView):
    model = College
    fields = ['name', 'Acronym', 'location', 'contact']

    def get_success_url(self):
        return reverse("college-list-view")
        #return super(CollegeCreateView, self).get_success_url()

class CollegeUpdateView(UpdateView):
    model = College
    fields = ['name', 'Acronym', 'location', 'contact']
    template_name_suffix = '_update_form'

    def get_object(self, queryset=None):
        # pk=self.request.GET.get('pk')
        acronym = self.kwargs.get("acronym")
        if acronym:
            return College.objects.get(acronym__iexact=acronym)
        else:
            return College.objects.get(pk=self.kwargs['pk'])

    def get_success_url(self):
        return reverse("college-list-view")

class CollegeDeleteView(DeleteView):
    model = College
    success_url = reverse_lazy('delete-data')
    def get_object(self, queryset=None):
        # pk=self.request.GET.get('pk')
        # acronym = self.kwargs.get("acronym")
        # if pk:
        #     return College.objects.get(acronym__iexact=acronym)
        # else:
        return College.objects.get(pk=self.kwargs['pk'])

    def get_success_url(self):
        return reverse("college-list-view")