from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Transaction, Category
from .forms import TransactionForm
from django.db.models import Sum
import csv
from django.http import HttpResponse

@login_required
def dashboard(request):
    transactions = Transaction.objects.filter(user=request.user).order_by('-date')[:10]
    filter_type = request.GET.get('filter', 'all')
    if filter_type in ['income', 'expense']:
        transactions = transactions.filter(transaction_type=filter_type)

    income = Transaction.objects.filter(user=request.user, transaction_type='income').aggregate(Sum('amount'))['amount__sum'] or 0
    expenses = Transaction.objects.filter(user=request.user, transaction_type='expense').aggregate(Sum('amount'))['amount__sum'] or 0
    balance = income - expenses

    # This gets expense totals grouped by category
    expense_by_category = Transaction.objects.filter(
        user=request.user, transaction_type='expense'
    ).values('category__name').annotate(total=Sum('amount'))

    # Separate labels and data for chart.js
    labels = [entry['category__name'] for entry in expense_by_category]
    data = [float(entry['total']) for entry in expense_by_category]

    return render(request, 'tracker/dashboard.html', {
        'transactions': transactions,
        'income': float(income),
        'expenses': float(expenses),
        'balance': float(balance),
        'filter_type': filter_type,
        'expense_by_category': expense_by_category,
        'labels': labels,
        'data': data
    })

@login_required
def export_transactions_csv(request):
    transactions = Transaction.objects.filter(user=request.user)
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="wealthwave_transactions.csv"'
    writer = csv.writer(response)
    writer.writerow(['Category', 'Amount', 'Type', 'Description', 'Date'])
    for transaction in transactions:
        writer.writerow([
            transaction.category.name if transaction.category else 'None',
            transaction.amount,
            transaction.transaction_type.title(),
            transaction.description,
            transaction.date
        ])
    return response

@login_required
def add_transaction(request):
    form = TransactionForm(request.user, request.POST or None)
    if request.method == 'POST' and form.is_valid():
        transaction = form.save(commit=False)
        transaction.user = request.user
        transaction.save()
        return redirect('dashboard')
    return render(request, 'tracker/add_transaction.html', {'form': form})

@login_required
def edit_transaction(request, transaction_id):
    transaction = get_object_or_404(Transaction, id=transaction_id, user=request.user)
    form = TransactionForm(request.user, request.POST or None, instance=transaction)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('dashboard')
    return render(request, 'tracker/add_transaction.html', {'form': form})


@login_required
def delete_transaction(request, transaction_id):
    transaction = get_object_or_404(Transaction, id=transaction_id, user=request.user)
    transaction.delete()
    return redirect('dashboard')

def signup(request):
    form = UserCreationForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = form.save()
        default_categories = ['Food', 'Rent', 'Salary', 'Entertainment']
        for cat in default_categories:
            Category.objects.create(user=user, name=cat)
        login(request, user)
        return redirect('dashboard')
    return render(request, 'tracker/signup.html', {'form': form})