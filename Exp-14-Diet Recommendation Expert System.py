age = int(input("Enter age: "))
bmi = float(input("Enter BMI: "))
condition = input("Enter health condition (diabetes/bp/none): ").lower()

if bmi < 18.5:
    diet = "High-protein and calorie-rich diet"
elif bmi >= 18.5 and bmi < 25:
    diet = "Balanced diet with fruits, vegetables, and proteins"
else:
    diet = "Low-fat and low-sugar diet"

# Additional rules based on health condition
if condition == "diabetes":
    diet += " + avoid sugary foods and include whole grains"
elif condition == "bp":
    diet += " + reduce salt intake and include potassium-rich foods"

print("\nRecommended Diet Plan:")
print(diet)
