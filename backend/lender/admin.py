from django.contrib import admin
from .models import LoanPrediction


@admin.register(LoanPrediction)
class LoanPredictionAdmin(admin.ModelAdmin):
    list_display = (
        'borrower_id', 'borrower_name', 'borrower_email', 'borrower_phone',
        'loan_amount', 'emi', 'tenure', 'rate_of_interest', 'customer_age',
        'gender', 'employment_type', 'residence_type', 'num_loans',
        'secured_loans', 'unsecured_loans', 'new_loans_last_3_months', 'tier',
        'credit_score', 'risk_level', 'created_at'
    )
    list_filter = ('risk_level', 'employment_type', 'residence_type', 'tier')
    search_fields = ('borrower_name', 'borrower_email', 'borrower_phone', 'loan_amount')
    ordering = ('-created_at',)
    readonly_fields = ('credit_score', 'risk_level', 'created_at')