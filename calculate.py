def calculate_battle_level(vehicle_tier, vehicle_type, battles_played, N):
    battle_levels = {
        'Light': {
            1: [1, 2],
            2: [2, 3],
            3: [3, 4, 5, 6],
            4: [4, 5, 6, 7, 8, 9, 10],
            5: [8, 9, 10, 11, 12, 13],
            6: [9, 10, 11, 12, 13],
            7: [8, 9, 10, 11],
            8: [8, 9, 10, 11, 12, 13],
            9: [9, 10, 11, 12, 13],
            10: [10, 11, 12, 13]
        },
        'Medium': {
            2: [2, 3],
            3: [3, 4, 5, 6],
            4: [4, 5, 6, 7, 8],
            5: [6, 7, 8, 9],
            6: [7, 8, 9, 10],
            7: [8, 9, 10, 11],
            8: [9, 10, 11],
            9: [11, 12, 13],
            10: [10, 11, 12, 13]
        },
        'Heavy': {
            4: [4, 5],
            5: [6, 7, 8, 9, 10],
            6: [7, 8, 9, 10, 11],
            7: [8, 9, 10, 11, 12],
            8: [9, 10, 11, 12],
            9: [10, 11, 12, 13],
            10: [10, 11, 12, 13]
        },
        'SPGs': {
            2: [3, 4, 5],
            3: [4, 5, 6, 7, 8],
            4: [6, 7, 8, 9, 10],
            5: [8, 9, 10, 11],
            6: [10, 11],
            7: [11, 12],
            8: [12, 13],
            9: [9, 10, 11, 12],
            10: [10, 11, 12, 13],
        },
        'Tank Destroyers': {
            2: [3, 4, 5],
            3: [4, 5, 6],
            4: [5, 6, 7, 8],
            5: [6, 7, 8, 9],
            6: [7, 8, 9, 10],
            7: [8, 9, 10, 11],
            8: [9, 10, 11, 12],
            9: [10, 11, 12, 13],
            10: [10, 11, 12, 13]
        },
    }
    
    # Определяем допустимый диапазон боевых уровней для данного транспортного средства
    allowed_battle_levels = battle_levels.get(vehicle_type, {}).get(vehicle_tier, [])
    
    # Если количество сыгранных боев равно 0, возвращаем минимально допустимый уровень боя
    if not allowed_battle_levels or battles_played == 0:
        return allowed_battle_levels[0] if allowed_battle_levels else None
    
    # Вычисляем индекс текущего уровня боя
    if battles_played < N:
        index = min(battles_played, len(allowed_battle_levels) - 1)
    else:
        index = len(allowed_battle_levels) - 1  # Последний доступный уровень, если B >= N
    
    # Возвращаем уровень боя по индексу
    return allowed_battle_levels[index]

# Пример использования функции
vehicle_tier = 10  # Уровень транспортного средства
vehicle_type = 'Heavy'  # Тип транспортного средства
battles_played = 0  # Количество сыгранных боев
N = 10  # Переменная диапазона

predicted_battle_level = calculate_battle_level(vehicle_tier, vehicle_type, battles_played, N)
print(f"Предсказанный уровень боя: {predicted_battle_level}")
