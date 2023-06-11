import random
import pyqiwip2p
from django.http import HttpResponseBadRequest
import secret


def pay(amount):
    """Функция, отдающая ссылку на оплату через киви"""
    try:
        p2p = pyqiwip2p.QiwiP2P(auth_key=secret.SECRET_QIWI_KEY)
        new_bill = p2p.bill(bill_id=random.randint(1, 100000), amount=amount, lifetime=15)
        return new_bill.pay_url
    except Exception as e:
        return HttpResponseBadRequest("Ошибка с оплатой!")