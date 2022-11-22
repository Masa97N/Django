import  logging
from django.urls import reverse_lazy
from django.views import generic
from.forms import InquiryForm

logger=logging.getLogger(__name__)

class IndexView(generic.TemplateView):
    template_name="index.html"

class InquiryView(generic.FormView):
    template_name="inquiry.html"
    form_class = InquiryForm
    success_url = reverse_lazy('diary:inquiry')
