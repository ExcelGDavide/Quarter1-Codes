full_name=input("Enter your full name (First, Middle, Last):")
first, middle, last = [part.strip() for part in full_name.split(",")]
first = first.capitalize()
last = " ".join([word.capitalize() for word in last.split()])
middle_initial = middle[0].upper() + "."
formatted_name = f"{last}, {first} {middle_initial}"
print("Formatted Name:", formatted_name)