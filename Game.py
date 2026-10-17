import random

bunker = {
    'name': '',
    'people': 4,
    'food': 10,
    'water': 10,
    'materials': 5,
    'inventory': []
}

events = [
    {'desc': 'Найден заброшенный склад припасов', 'type': 'supplies', 'food': 5, 'water': 5},
    {'desc': 'На бункер напали дикие мародеры', 'type': 'raiders', 'damage_people': 1, 'materials': 10},
    {'desc': 'Торговец предлагает обменять материалы на еду и воду', 'type': 'trader'},
    {'desc': 'Прорвало трубу в подвале! Потеряны запасы воды', 'type': 'leak', 'water_loss': 4},
    {'desc': 'Тихий день, выжившие смогли отдохнуть и укрепить стены', 'type': 'peace', 'materials_gain': 3},
]

print("********************")
print("**Бункер №404: Выживание**")

bunker['name'] = input('Введите имя лидера бункера: ')

print(f'\n{bunker["name"].capitalize()}, у вас есть 10 дней, чтобы выжить в убежище!\n')

def get_safe_choice(prompt, max_val):
    while True:
        try:
            choice = int(input(prompt))
            if 1 <= choice <= max_val:
                return choice
            else:
                print(f"⚠️ Введите число от 1 до {max_val}!")
        except ValueError:
            print("⚠️ Ошибка! Нужно ввести цифру, а не текст.")

for day in range(1, 11):

    print(f'\n--- ДЕНЬ {day}/10 ---')
    print(f'👥 Люди: {bunker["people"]} | 🍖 Еда: {bunker["food"]} | 💧 Вода: {bunker["water"]} | 🛠 Материалы: {bunker["materials"]} | 🎒 Инвентарь: {bunker["inventory"]}')

    current_event = random.choice(events)
    print(f'Событие: {current_event["desc"]}')

    if current_event['type'] == 'supplies':
        print('1. Забрать припасы себе')
        print('2. Оставить на складе')

        choice = get_safe_choice('Выберите действие (1 или 2): ', 2)

        if choice == 1:
            bunker['food'] += current_event['food']
            bunker['water'] += current_event['water']
            print(f'Вы получили +{current_event["food"]} еды и +{current_event["water"]} воды.')
        else:
            print('Вы решили не трогать склад.')

    elif current_event['type'] == 'raiders':
        print('1. Дать отпор (нужна Бита или Автомат)')
        print('2. Спрятаться и отдать часть материалов')

        choice = get_safe_choice('Выберите действие (1 или 2): ', 2)

        if choice == 1:
            if 'Автомат' in bunker['inventory']:
                print('🔫 Вы использовали автомат и легко отбили атаку мародеров без потерь!')
            elif 'Бита' in bunker['inventory']:
                bunker['inventory'].remove('Бита')
                print('🏏 Вы отбились битой, но она сломалась! Потерь среди людей нет.')
            else:
                bunker['people'] -= current_event['damage_people']
                print(f'❌ У вас не было оружия! Один человек погиб при защите. Люди: {bunker["people"]}')
        else:
            lost_mat = min(bunker['materials'], 5)
            bunker['materials'] -= lost_mat
            print(f'Вы отсиделись, но мародеры забрали {lost_mat} материалов.')

    elif current_event['type'] == 'trader':
        print('1. Купить Автомат за 8 материалов')
        print('2. Купить Биту за 4 материала')
        print('3. Купить Фильтрационную установку (вечная вода) за 10 материалов')
        print('4. Ничего не покупать')

        choice = get_safe_choice('Выберите действие (1-4): ', 4)

        if choice == 1:
            if bunker['materials'] >= 8:
                bunker['materials'] -= 8
                bunker['inventory'].append('Автомат')
                print('Вы купили Автомат.')
            else:
                print('Не хватает материалов!')
        elif choice == 2:
            if bunker['materials'] >= 4:
                bunker['materials'] -= 4
                bunker['inventory'].append('Бита')
                print('Вы купили Биту.')
            else:
                print('Не хватает материалов!')
        elif choice == 3:
            if bunker['materials'] >= 10:
                bunker['materials'] -= 10
                bunker['inventory'].append('Фильтр')
                print('Вы купили Фильтрационную установку.')
            else:
                print('Не хватает материалов!')
        else:
            print('Вы проводили торговца мимо.')

    elif current_event['type'] == 'leak':
        if 'Фильтр' in bunker['inventory']:
            print('🛡️ Фильтрационная установка помогла быстро перекрыть течь и спасти воду!')
        else:
            loss = min(bunker['water'], current_event['water_loss'])
            bunker['water'] -= loss
            print(f'💧 Пропало {loss} ед. воды из-за аварии.')

    elif current_event['type'] == 'peace':
        bunker['materials'] += current_event['materials_gain']
        print(f'Вы укрепили бункер и нашли +{current_event["materials_gain"]} материалов.')

    food_needed = bunker['people'] * 1
    water_needed = bunker['people'] * 1

    print("\n--- Вечерний рацион ---")
    if bunker['food'] >= food_needed:
        bunker['food'] -= food_needed
        print(f'🍖 Съедено {food_needed} еды.')
    else:
        bunker['food'] = 0
        bunker['people'] -= 1
        print('⚠️ Не хватило еды! Один человек умер от голода.')

    if 'Фильтр' not in bunker['inventory']:
        if bunker['water'] >= water_needed:
            bunker['water'] -= water_needed
            print(f'💧 Выпито {water_needed} воды.')
        else:
            bunker['water'] = 0
            bunker['people'] -= 1
            print('⚠️ Не хватило воды! Один человек умер от жажды.')
    else:
        print('💧 Фильтр производит воду автоматически, запасы воды не тратятся на жажды!')

    if bunker['people'] <= 0:
        print('*****************************')
        print('💀 Все жители бункера погибли. Игра окончена.')
        break

else:
    print('*****************************')
    print(f'🏆 Поздравляем, {bunker["name"].capitalize()}! Вы продержались все 10 дней в бункере!')
    print(f'Осталось людей: {bunker["people"]}, инвентарь: {bunker["inventory"]}')