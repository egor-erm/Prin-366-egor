def analyze_text(text):
    # Приводим текст к нижнему регистру
    text = text.lower()
    
    # Убираем знаки препинания
    for symbol in ",.!?;:-()\"":
        text = text.replace(symbol, "")
    
    words = text.split()
    
    word_count = {}
    total_length = 0
    
    # Подсчет частоты слов и общей длины
    for word in words:
        total_length += len(word)
        
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    
    # Вычисление средней длины слова
    average_length = total_length / len(words) if words else 0
    
    print("Количество слов:", len(words))
    print("Средняя длина слова:", round(average_length, 2))
    print("\nЧастота слов:")
    
    # Сортировка слов по частоте
    for word in sorted(word_count, key=word_count.get, reverse=True):
        print(f"{word}: {word_count[word]}")


text_input = input("Введите текст для анализа: ")
analyze_text(text_input)
