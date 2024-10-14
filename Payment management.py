class Payment:
    def __init__(self, amount, payment_method):
        self.amount = amount
        self.payment_method = payment_method

class PaymentRepository:
    def __init__(self):
        self.payments = []

    def add_payment(self, payment):
        self.payments.append(payment)

    def get_total_payments(self):
        total = 0
        for payment in self.payments:
            total += payment.amount
        return total

    def get_payments_by_method(self, payment_method):
        payments = [payment for payment in self.payments if payment.payment_method == payment_method]
        return payments

# 创建支付存储库对象
payment_repository = PaymentRepository()

# 添加支付信息
payment1 = Payment(10, "credit card")
payment2 = Payment(20, "cash")
payment_repository.add_payment(payment1)
payment_repository.add_payment(payment2)

# 获取所有支付总额
total_payments = payment_repository.get_total_payments()
print(f"Total payments: ${total_payments}")

# 获取特定支付方式的支付信息
credit_card_payments = payment_repository.get_payments_by_method("credit card")
print("Credit card payments:")
for payment in credit_card_payments:
    print(f"Amount: ${payment.amount}")