import random
import pyqiwip2p
from config import secret


SECRET_QIWI_KEY = secret.SECRET_QIWI_KEY
new_bill = random.randrange(1, 9999999999999999999)
p2p = pyqiwip2p.QiwiP2P(auth_key=SECRET_QIWI_KEY)


def pay(amount):
    """Функция, отдающая ссылку на оплату через киви"""
    global new_bill, p2p
    new_bill = p2p.bill(bill_id=new_bill, amount=amount, lifetime=15)
    return new_bill.pay_url