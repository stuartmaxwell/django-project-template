from django.views.generic import TemplateView

import logging

logger = logging.getLogger(__name__)


class HomePage(TemplateView):
    template_name = "website/home.html"
