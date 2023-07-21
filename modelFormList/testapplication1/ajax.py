import deserialize_form
from testapplication1.forms import formpAge
from dajax.core import Dajax
from testapplication1.models import modelForm1


@dajaxice_register
def send_form(request, form):
    dajax = Dajax()
    form = formpAge(deserialize_form(form))

    if form.is_valid():
        dajax.remove_css_class('#my_form input', 'error')
        dr = modelForm1()
        dr.name = form.cleaned_data.get('name')
        dr.number = form.cleaned_data.get('number')
        dr.save()

        dajax.alert("Dreamreal Entry %s was successfully saved." %
                    form.cleaned_data.get('name'))
    else:
        dajax.remove_css_class('#my_form input', 'error')
        for error in form.errors:
            dajax.add_css_class('#id_%s' % error, 'error')

    return dajax.json()