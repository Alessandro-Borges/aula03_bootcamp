### Exercício 5: Detecção de Anomalias em Dados de Transações
# Você está trabalhando em um sistema de detecção de fraude e precisa identificar 
# transações suspeitas. Uma transação é considerada suspeita se o valor for superior 
# a R$ 10.000 ou se ocorrer fora do horário comercial (antes das 9h ou depois das 18h). 
# Dada uma transação como `transacao = {'valor': 12000, 'hora': 20}`, verifique se ela é suspeita.


import random

# Example usage:
num_transactions = 100  # Change this value to generate more or fewer transaction
trans_suspeita = []

# Using for num in num_transactions::
# This approach tries to iterate over the elements of num_transactions. However, num_transactions is not an iterable in your code; it's just an integer representing the number of transactions to generate. Therefore, this approach will raise an error because you're trying to iterate over an integer.
# Even if num_transactions were an iterable (like a list), using for num in num_transactions: would iterate over the values of num_transactions, not the number of times specified by num_transactions. This would not achieve the intended behavior of repeating an action a fixed number of times.

def generate_dummy_data(num_transactions):
    dummy_data = []
    for _ in range(num_transactions):
        valor = random.randint(100, 100000)  # Random value between 100 and 100000
        hora = random.randint(0, 23)  # Random hour of the day
        transacao = {'valor': valor, 'hora': hora}
        dummy_data.append(transacao)
    return dummy_data

def validate_transaction(dados):
    for transaction in dados:
        if transaction['valor'] > 10000 and (transaction['hora'] < 9 or transaction['hora'] > 18):
            trans_suspeita.append(transaction)
    



dummy_data = generate_dummy_data(num_transactions)

validate_transaction(dummy_data)
#print(dummy_data)

print(trans_suspeita)


