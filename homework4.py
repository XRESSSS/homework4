from pywebio.input import input as pw_input
from pywebio.input import TEXT
from pywebio.output import put_success, put_warning

cat_emoji = '🐈'
dog_emoji = '🐕'
turtle_emoji = '🐢'
hamster_emoji = '🐹'
fish_emoji = '🐟'
idk = '😭'

nessory_pet = 'fish'
nessory_pet2 = 'dog'
nessory_pet3 = 'turtle'
nessory_pet4 = 'hamster'
nessory_pet5 = 'cat'

# idк=i_dont know, use European teenager

can_pet_swin = False

user_pet = str(pw_input('Enter your pet', type=TEXT)).lower().strip()
pets_name = str(pw_input('Enter name of your pet', type=TEXT)).title().strip()
skills = pw_input('Can your pet swim?', required=False).lower().strip()

is_fish = user_pet == 'fish'
is_dog = user_pet == 'dog'
is_turtle = user_pet == 'turtle'
is_cat = user_pet == 'cat'
is_hamster = user_pet == 'hamster'

if user_pet == 'fish' or user_pet == 'turtle':
    can_pet_swin = True
if can_pet_swin:
    put_warning('Buy them aquarium')

if is_dog:
    put_warning(f' I\'m afraid of barking dogs, and {pets_name} too {dog_emoji}')

elif is_cat:
    put_success(f'cats {cat_emoji} catch mice')

elif is_turtle:
    put_success(f'the turtle {turtle_emoji} has a strong shell')

elif is_fish:
    put_success(f'fish can\'t be fried {fish_emoji}')

elif is_hamster:
    put_success(f'hamsters are small{hamster_emoji}')

else:
    put_warning(f'I don\'t know what kind of animal it is{idk}')
