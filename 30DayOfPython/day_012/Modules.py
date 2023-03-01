#Exercises: Day 12
# Question 1
import random
import string

def generate_random_user_id():
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for i in range(6))
print(generate_random_user_id())

# Question 2
def user_id_gen_by_user():
    num_chars = int(input("Enter the users ID: "))
    num_ids = int(input("Enter the number of user IDs to generate: "))
    characters = string.ascii_letters + string.digits

    user_ids = []
    for i in range(num_ids):
        user_id = ''.join(random.choice(characters) for j in range(num_chars))
        user_ids.append(user_id)
    return user_ids
print(user_id_gen_by_user())

# Question 3
def rgb_color_gen():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    return "rgb({}, {}, {})".format(red, green, blue)

print(rgb_color_gen())

#Exercise level 2
#Question 1
def list_of_hexa_colors(num_colors):
    hexa_chars = string.digits + 'abcdef'
    hexa_colors = []
    for i in range(num_colors):
        hexa_color = ''.join(random.choice(hexa_chars) for j in range(6))
        hexa_colors.append('#' + hexa_color)
    return hexa_colors

print(list_of_hexa_colors(6))

# Question 2

def list_of_rgb_colors(num_colors):
    rgb_colors = []
    for i in range(num_colors):
        red = random.randint(0, 20)
        green = random.randint(0, 20)
        blue = random.randint(0, 20)
        rgb_colors.append((red, green, blue))

    return rgb_colors

print(list_of_rgb_colors(6))

# Question 3
def generate_colors(color_type, num):
    colors = []
    if color_type == 'hexa':
        for i in range(num):
            color = "#"
            for j in range(6):
                color += random.choice("1234defg")
            colors.append(color)
    elif color_type == 'rgb':
        for i in range(num):
            color = "rgb("
            for j in range(3):
                color += str(random.randint(0, 255))
                if j < 2:
                    color += ","
            color += ")"
            colors.append(color)
    return colors
print(generate_colors('hexa', 3)) 
print(generate_colors('hexa', 1)) 
print(generate_colors('rgb', 3))  
print(generate_colors('rgb', 1))  

#Exercises: Level 3
# Question 1
def shuffle_list(input_list):
    shuffled_list = input_list.copy()
    random.shuffle(shuffled_list)
    return shuffled_list

my_list = [1, 3, 5, 7, 9]
print(shuffle_list(my_list))

# Question 2
def unique_random_numbers():
    random_numbers = random.sample(range(10), 7)
    return random_numbers

print(unique_random_numbers())