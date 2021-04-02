from io import BytesIO
from django.shortcuts import render, HttpResponse, Http404
from django.views.generic import DetailView

from django.template.loader import get_template
from xhtml2pdf import pisa
from core.models import Foo


def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None


class PdfViewPage(DetailView):
    template_name = 'core/pdf.html'
    model = Foo
    context_object_name = 'foo'

    def get(self, request, *args, **kwargs):

        foo = self.get_object()
        if self.request.user != foo.user:
            raise Http404

        data = {
            'id': foo.id,
            'username': foo.user.username,
            'amount': foo.amount,
        }
        pdf = render_to_pdf('core/pdf.html', data)
        if pdf is None:
            return Http404  # return meaningful error if you want
        else:
            return HttpResponse(pdf, content_type='application/pdf')


def pdf_view_page(request):

    if request.method == 'GET':
        return render(request, 'core/form.html')

    if request.method == 'POST':

        target_id = request.POST.get('id')

        try:
            foo = Foo.objects.get(id=target_id)
        except Foo.DoesNotExist:
            raise Http404

        if request.user != foo.user:  # Make sure the requesting user owns the object
            raise Http404

        data = {
            'id': foo.id,
            'username': foo.user.username,
            'amount': foo.amount,
        }
        pdf = render_to_pdf('core/pdf.html', data)
        return HttpResponse(pdf, content_type='application/pdf')
