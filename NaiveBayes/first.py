import pandas
import numpy as np
with open("firstModel") as f:
    a = f.read().strip()
a = a.split("\n")[1:]
model = {}
for i in range(len(a)):
    z = a[i].split()
    model[z[0]] = {"spam": int(z[1]), "ham": int(z[2])}

emails = pandas.read_csv("emails.csv")
def Bayes(message):
    total = len(emails)
    amountOfSpam = sum(emails['spam'])
    amountOfHam = total - amountOfSpam
    message = message.lower()
    message = set(message.split())
    spam = [1.0]
    ham = [1.0]
    for word in message:
        if word in model:
            spam.append(model[word]['spam'] / amountOfSpam * total)
            ham.append(model[word]['ham'] / amountOfHam * total)
    prodSpam = np.prod(spam) * amountOfSpam
    prodHam = np.prod(ham) * amountOfHam
    return prodSpam / (prodSpam + prodHam)
print(Bayes("prize"))