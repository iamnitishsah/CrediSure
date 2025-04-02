from django.db import models

class LoanPrediction(models.Model):
    borrower_name = models.CharField(max_length=100)
    borrower_id = models.AutoField(primary_key=True)
    borrower_email = models.EmailField()
    borrower_phone = models.CharField(max_length=15)
    loan_amount = models.FloatField()
    emi = models.FloatField()
    tenure = models.IntegerField()
    rate_of_interest = models.FloatField()
    customer_age = models.IntegerField()
    gender = models.CharField(max_length=10)
    employment_type = models.CharField(max_length=20)
    residence_type = models.CharField(max_length=20)
    num_loans = models.IntegerField()
    secured_loans = models.IntegerField()
    unsecured_loans = models.IntegerField()
    new_loans_last_3_months = models.IntegerField()
    tier = models.CharField(max_length=10)
    credit_score = models.FloatField(null=True, blank=True)
    risk_level = models.CharField(max_length=20, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Prediction {self.borrower_id} :- {self.borrower_name}"