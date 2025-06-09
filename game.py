# Игра "Крестики-нолики" с обновлёнными названиями

def display_game_field(game_field):
    """Отображает текущее состояние игрового поля."""
    print("Текущее игровое поле:")
    for row in game_field:
        print(" | ".join(row))
        print("-" * 9)

def check_win(game_field, player):
    """Проверяет, есть ли победитель для указанного игрока."""
    # Проверка строк
    for row in game_field:
        if all(cell == player for cell in row):
            return True
    # Проверка столбцов
    for col in range(3):
        if all(row[col] == player for row in game_field):
            return True
    # Проверка диагоналей
    if all(game_field[i][i] == player for i in range(3)):
        return True
    if all(game_field[i][2 - i] == player for i in range(3)):
        return True
    return False

def check_draw(game_field):
    """Проверяет, закончилась ли игра ничьёй."""
    return all(all(cell != " " for cell in row) for row in game_field)

def main():
    # Инициализация игрового поля
    game_field = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        display_game_field(game_field)
        print(f"Ход игрока {current_player}")
        try:
            row = int(input("Введите номер строки (1-3): ")) - 1
            col = int(input("Введите номер столбца (1-3): ")) - 1
            if not (0 <= row <= 2 and 0 <= col <= 2):
                print("Некорректный ввод. Попробуйте снова.")
                continue
            if game_field[row][col] != " ":
                print("Эта ячейка уже занята. Попробуйте другую.")
                continue
            # Сделать ход
            game_field[row][col] = current_player
        except ValueError:
            print("Пожалуйста, введите число от 1 до 3.")
            continue

        # Проверка победы или ничьи
        if check_win(game_field, current_player):
            display_game_field(game_field)
            print(f"Поздравляем! Игрок {current_player} победил!")
            break
        elif check_draw(game_field):
            display_game_field(game_field)
            print("Ничья!")
            break

        # Смена игрока
        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    main()