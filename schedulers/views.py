from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib import messages
from schedulers.task import send_email

# Create your views here.
class RegisterView(TemplateView):
    template_name = 'register.html'
    def get_context_data(self, **kwargs):        
        context = super().get_context_data(**kwargs)
        return context

    def post(self,request,*args, **kwargs):
        context = self.get_context_data()
        email = request.POST.get('email')
        psw = request.POST.get('psw')
        psw_repeat = request.POST.get('psw-repeat')
        if psw == psw_repeat:
            send_email.delay()
            messages.error(request, {'alert':'register success'})
        else:
            messages.error(request, {'alert':'register failed'})
            
        context['alert'] = True
        return super(TemplateView, self).render_to_response(context)



