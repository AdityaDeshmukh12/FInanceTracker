from django.shortcuts import render, redirect
from .models import Transaction
from .forms import TransactionForm
from django.db.models import Sum

def home(request):
    # Process form submission
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TransactionForm()

    # Retrieve past transactions and calculate balances
    transactions = Transaction.objects.all().order_by('-date')
    total_income = Transaction.objects.filter(transaction_type='income').aggregate(Sum('amount'))['amount__sum'] or 0
    total_expenses = Transaction.objects.filter(transaction_type='expense').aggregate(Sum('amount'))['amount__sum'] or 0
    balance = total_income - total_expenses

    context = {
        'form': form,
        'transactions': transactions,
        'total_income': total_income,
        'total_expenses': total_expenses,
        'balance': balance,
    }
    return render(request, 'tracker/home.html', context)
