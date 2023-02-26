spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    return [food['name'] for food in spicy_foods]
    

def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if food['heat_level'] > 5]
    # food = []

    # for food in spicy_foods:
    #     if food["heat_level"] > 5:
    #         food.append(food)
    

# print(): Buffalo Wings (American) | Heat Level: 🌶🌶🌶

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        name = food["name"]
        country = food['cuisine']
        heat = food['heat_level'] * "🌶"
        print(f"{name} ({country}) | Heat Level: {heat}")


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food 
    pass

def print_spiciest_foods(spicy_foods):
    print_spicy_foods(get_spiciest_foods(spicy_foods))
    # spicy_list = []

    # for food in spicy_foods:
    #     if food["heat_level"] > 5:
    #         spicy_list.append(food)
    
    # for food in spicy_list:
    #     name = food["name"]
    #     country = food['cuisine']
    #     heat = food['heat_level'] * "🌶"
    #     print(f"{name} ({country}) | Heat Level: {heat}")

    # pass

def get_average_heat_level(spicy_foods):
    
    # return sum([food["heat_level"] for food in spicy_foods]) / len(spicy_foods) also works 

    sum = 0
    for food in spicy_foods:
        heat = food['heat_level']
        sum += heat # the += means sum = sum + heat

    average = sum / len(spicy_foods) #sum divided by total number of spicy foods
    return average
    pass

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)

    return spicy_foods
    pass
