# Smart Urban Planning Decision Support System (Basic Prototype)

def suggest_area(traffic, pollution, green_space):
    score = 0

    # Lower traffic is better
    if traffic < 50:
        score += 2
    else:
        score += 1

    # Lower pollution is better
    if pollution < 50:
        score += 2
    else:
        score += 1

    # Higher green space is better
    if green_space > 50:
        score += 2
    else:
        score += 1

    if score >= 5:
        return "Highly Suitable for Development"
    elif score >= 4:
        return "Moderately Suitable"
    else:
        return "Not Suitable"

# Taking user input
print("Smart Urban Planning Decision Support System")

traffic = int(input("Enter traffic level (0-100): "))
pollution = int(input("Enter pollution level (0-100): "))
green_space = int(input("Enter green space availability (0-100): "))

result = suggest_area(traffic, pollution, green_space)

print("Decision:", result)