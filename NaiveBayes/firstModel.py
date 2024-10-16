import pandas
import numpy
def process_email(text):
    text = text.lower()
    return list(set(text.split()))
emails = pandas.read_csv("emails.csv")
emails['words'] = emails['text'].apply(process_email)
apriorSpam = sum(emails['spam']) / len(emails)
model = {}
for index, email in emails.iterrows():
    for word in email['words']:
        if word not in model:
            model[word] = {'spam' : 1, "ham" : 1}
        elif email['spam']:
            model[word]['spam'] += 1
        else:
            model[word]["ham"] += 1
s = 'word spam ham\n'
for i in model:
    s += f"{i} {model[i]['spam']} {model[i]['ham']}\n"
with open("firstModel", 'w') as f:
    f.write(s)
print(model['sale'])