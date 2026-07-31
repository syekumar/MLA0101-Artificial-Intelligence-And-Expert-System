symptoms = {
    "fever": True,
    "cough": True,
    "body_pain": True
}

def has_flu():
    return (symptoms["fever"] and
            symptoms["cough"] and
            symptoms["body_pain"])

if has_flu():
    print("Disease: Flu")
else:
    print("Disease Not Found")
