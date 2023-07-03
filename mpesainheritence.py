class MpesaTransaction:
    def __init__(self, transaction_id, amount):
        self.transaction_id = transaction_id
        self.amount = amount

    def process_transaction(self):
        raise NotImplementedError("subclass to use this method")


class DepositTransaction(MpesaTransaction):
    def process_transaction(self):
        print(f"Deposit Transaction with ID {self.transaction_id} processed")


class WithdrawalTransaction(MpesaTransaction):
    def process_transaction(self):
        print(f"Withdrawal Transaction with ID {self.transaction_id} processed")


class PaymentTransaction(MpesaTransaction):
    def __init__(self, transaction_id, amount, recipient):
        super().__init__(transaction_id, amount)
        self.recipient = recipient

    def process_transaction(self):
        print(f"Payment transaction with id {self.transaction_id} processed. Amount{self.amount}. Recipient{self.recipient}")


deposit = DepositTransaction("DHTY", 2000)
withdrawal = WithdrawalTransaction("DFTY", 5000)
payment = PaymentTransaction("DGHT", 1500, " Robert")
deposit.process_transaction()
withdrawal.process_transaction()
payment.process_transaction()
