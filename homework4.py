from pywebio.input import input as pw_input
from pywebio.input import TEXT
from pywebio.output import put_success, put_warning


cat_emoji = '🐈'
dog_emoji = '🐕'
turtle_emoji = '🐢'
hamster_emoji = '🐹'
fish_emoji = '🐟'
idk = '😭'

# idк=i_dont know, use European teenager


can_pet_swin = False
user_pet = str(pw_input('Enter your pet', type=TEXT)).lower().strip()
pets_name = str(pw_input('Enter name of your pet', type=TEXT)).title().strip()


if user_pet == 'fish' or user_pet == 'turtle':
    can_pet_swin = True
    put_warning('Buy them aquarium')

if user_pet == 'dog':
    put_warning(f' I\'m afraid of barking dogs, and {pets_name} too {dog_emoji}')

elif user_pet == 'cat':
    put_success(f'cats {cat_emoji} catch mice')

elif user_pet == 'turtle':
    put_success(f'the turtle {turtle_emoji} has a strong shell')

elif user_pet == 'fish':
    put_success(f'fish can\'t be fried {fish_emoji}')

elif user_pet == 'hamster':
    put_success(f'hamsters are small{hamster_emoji}')

else:
    put_warning(f'I don\'t know what kind of animal it is{idk}')
