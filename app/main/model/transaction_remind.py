from .. import db, flask_bcrypt

class TransactionRemind(db.Model):
    __tablename__ = "transaction_remind"

    TransactionRemindId = db.Column(db.Integer, primary_key=True, autoincrement=True)
    PaymentAccountId = db.Column(db.String(255), db.ForeignKey('payment_account.NumberPaymentAccount'))
    PaymentAccountRemindId = db.Column(db.String(255), db.ForeignKey('payment_account.NumberPaymentAccount'))
    Amount = db.Column(db.Integer)
    Content = db.Column(db.Text)
    CreatedDate = db.Column(db.DateTime)
    UpdatedDate = db.Column(db.DateTime)
    Status = db.Column(db.Integer)

    STATUS_CREATED = 0
    STATUS_PAYMENT = 1
    STATUS_DELETED = 2

    # @property
    # def __repr__(self):
    #     return "<PaymentAccount '{}'>".format(self.NumberPaymentAccount)