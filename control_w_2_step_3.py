from random import random

dragon = {
    'hp': 2000,       # жизненная энергия, запас здоровья
    'defence': 120,   # защита 
    'str': 150,       # сила
    'weapon': 0       # оружие
}

hero = {

    'hp': 1000,
    'defence': 100,
    'str': 120,
    'weapon': 250,
    'shield': 150 ,    # щит
    'has_shield': False
}


def display_dragon_info(character_info):                   #вывод информации о драконе
    print(f'Здоровье:{character_info["hp"]}')
    print(f'Защита:{character_info["defence"]}')
    print(f'Сила:{character_info["str"]}')
    print(f'Оружие:{character_info["weapon"]}')



def display_hero_info(character_info):                   #вывод информации о герое
    print(f'Здоровье:{character_info["hp"]}')
    print(f'Защита:{character_info["defence"]}')
    print(f'Сила:{character_info["str"]}')
    print(f'Оружие:{character_info["weapon"]}')
    print(f'Щит:{character_info["shield"]}')


def modify_health(character, hp):
    # character['hp']+=hp
    health = character['hp']
    health_with_modification = health + hp
    if health_with_modification < 0:
        character["hp"] = 0

    else:
        character['hp'] = health_with_modification


def hero_attack():                   #ход героя
    print('Ход героя')
    if random()<=0.75:
        damage = hero['str'] + hero['weapon']-dragon['defence']
        modify_health(dragon, damage * -1)
        print(f"Дракон получил {damage} ед.урона")
        print("-------------------")
    else:
        print("Герой не попал!")
        print("-------------------")
  

def equip_shield():
    if not hero["has_shield"]:
        print("Герой одевает щит")
        hero["defence"] += hero["shield"]
        hero["has_shield"] = True

def remove_shield():
      if hero["has_shield"]:
        print("Щит рассыпается от мощного удара дракона")
        hero["defence"] -= hero["shield"]
        hero["has_shield"] = False


# def fire_ball():
#      if random()<=0.50:
#             print("Дракон выплевает огненый шар")
#             damage = dragon['str'] * 2


def hero_pass():
    print('Герой решил передохнуть')



def hero_turn():
    hero_action = input("Введите действие для героя:(attack,pass,defence):\n>").strip().lower()
    if hero_action == "attack":
        hero_attack()
    if hero_action == "pass":
        hero_pass()
    if hero_action == "defence":  
        equip_shield()

    display_dragon_info(dragon)
    print("==================== \n\n\n")    


def dragon_turn():                   #ход дракона
    print('Ход дракона')
    if random()<=0.50:
        if random()<=0.50:
            print("Дракон выплевает огненый шар")
            damage = dragon['str'] * 2
            if hero['has_shield']:
                print('Герой успешно отразил огненый шар')
                damage = 0
        else:
             damage = dragon['str'] + dragon['weapon']-hero['defence']
             damage = 0 if damage<=0 else damage
        modify_health(hero, damage * -1)
        print(f"Герой получил {damage} ед.урона")
        print("-------------------")
    else:
        print("Дракон проспал свой ход!")
        print("-------------------")
    display_hero_info(hero)
    print("====================\n\n\n")
 

#Это отдельный блок
print("Игра началась!)")
print("**********************")
print(">>>>>>>>>>>>>>>>>>>>>>")
while True:
    #первый ход
    hero_turn()
    dragon_hp = dragon['hp']    
    if dragon_hp <=0:
        print("**********************")
        print('Герой выиграл')
        print("**********************")
        break

    #второй ход
    dragon_turn()
    hero_hp = hero['hp']
    if hero_hp <=0:
        print("**********************")
        print('Дракон выиграл')
        print("**********************")
        break
    
    
