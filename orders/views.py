from django.shortcuts import get_object_or_404, render
from django.core.mail import send_mail
from .models import Order

# Create your views here.
def update_order_status(request):
    # order = get_object_or_404(Order, id=order_id)  # Asegúrate de descomentar y ajustar si necesitas obtener un pedido
    if request.method == 'POST':
        status = request.POST.get('status')
        if status in [choice[0] for choice in Order.STATUS_CHOICES]:
            # order.status = status
            # order.save()
            send_mail(
                'El estado de su pedido ha cambiado a:',  # Asunto
                f'Su pedido ha sido actualizado al nuevo estado:  {status}',  # Mensaje
                'tucorreo@correo.com',  # Correo del remitente
                ['destinario@correo.com'],  # Lista de destinatarios
                fail_silently=False
            )
    return render(request, 'update_order_status.html')
    # return render(request, 'update_order_status.html', { 'order': order})
