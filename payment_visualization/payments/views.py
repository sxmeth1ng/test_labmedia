import json
import calendar
from django.shortcuts import render
from .models import Payment


def index(request):
    payments = Payment.objects.select_related('payer').order_by('pay_date')

    scatter_data = []
    for p in payments:

        ts = calendar.timegm(p.pay_date.timetuple()) * 1000
        scatter_data.append({'x': ts, 'y': float(p.amount)})

    bar_labels = [
        f"{p.payer.first_name} {p.payer.last_name}" for p in payments
        ]
    bar_values = [float(p.amount) for p in payments]

    context = {
        'scatter_data_json': json.dumps(scatter_data),
        'bar_labels_json': json.dumps(bar_labels),
        'bar_values_json': json.dumps(bar_values),
    }
    return render(request, 'index.html', context)
