
import seaborn as sns

def add(a,b):
    return a + b

def multiply(a,b):
    return a * b

def divide(a,b):
    return a / b

def subtract(a,b):
    return a - b

def add_new(a,b):
    return a + b + 10

def plot_data(data):
    sns.lineplot(data=data)
    sns.show()