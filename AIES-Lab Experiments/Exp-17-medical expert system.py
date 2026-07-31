# Medical Expert System

# Disease rules
rules = {
    "Fever": {"fever", "headache", "body pain"},
    "Cold": {"cough", "sneezing", "runny nose"},
    "Malaria": {"fever", "chills", "sweating"},
    "COVID-19": {"fever", "cough", "loss of smell"}
}

# Input symptoms
symptoms = set(input("Enter symptoms (comma separated): ").lower().split(","))

# Remove extra spaces
symptoms = {s.strip() for s in symptoms}

# Rule-based reasoning
found = False
for disease, rule in rules.items():
    if rule.issubset(symptoms):
        print("Possible Disease:", disease)
        found = True

if not found:
    print("No matching disease found.")
