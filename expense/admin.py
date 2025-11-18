# expense/admin.py
from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Transaction, Goal

class TransactionResource(resources.ModelResource):
    class Meta:
        model = Transaction

@admin.register(Transaction)
class TransactionAdmin(ImportExportModelAdmin):
    resource_class = TransactionResource
    list_display = ('id', 'user', 'amount', 'transaction_type', 'date')  # adapt to your model
    search_fields = ('title',)

admin.site.register(Goal)
