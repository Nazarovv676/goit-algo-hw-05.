import timeit

# Алгоритм Кнута-Морріса-Пратта
def kmp_search(text, pattern):
    def compute_lps(pattern):
        lps = [0] * len(pattern)
        length = 0
        i = 1
        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            elif length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
        return lps

    if not pattern or not text:
        return -1  # Якщо текст чи підрядок порожній

    lps = compute_lps(pattern)
    i = j = 0
    while i < len(text):
        if text[i] == pattern[j]:
            i += 1
            j += 1
        if j == len(pattern):
            return i - j  # Знайдено
        elif i < len(text) and text[i] != pattern[j]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return -1  # Не знайдено

# Алгоритм Рабіна-Карпа
def rabin_karp_search(text, pattern, prime=101):
    m, n = len(pattern), len(text)
    hash_pattern = sum(ord(pattern[i]) * (256 ** (m - i - 1)) for i in range(m)) % prime
    hash_text = sum(ord(text[i]) * (256 ** (m - i - 1)) for i in range(m)) % prime
    h = (256 ** (m - 1)) % prime
    for i in range(n - m + 1):
        if hash_pattern == hash_text:
            if text[i:i + m] == pattern:
                return i  # Знайдено
        if i < n - m:
            hash_text = (hash_text - ord(text[i]) * h) * 256 + ord(text[i + m])
            hash_text %= prime
    return -1  # Не знайдено

# Алгоритм Боєра-Мура
def boyer_moore_search(text, pattern):
    def bad_character_heuristic(pattern):
        bad_char = {}
        for i, char in enumerate(pattern):
            bad_char[char] = i  # Зберігаємо позицію символу
        return bad_char

    if not pattern or not text:
        return -1  # Якщо текст чи підрядок порожній

    bad_char = bad_character_heuristic(pattern)
    m, n = len(pattern), len(text)
    s = 0
    while s <= n - m:
        j = m - 1
        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1
        if j < 0:
            return s  # Знайдено
        s += max(1, j - bad_char.get(text[s + j], -1))  # Якщо символа немає в шаблоні, повертаємо -1
    return -1  # Не знайдено

# Порівняння ефективності
def compare_algorithms(file1, file2, substrings):
    try:
        with open(file1, 'r', encoding='windows-1251') as f1, open(file2, 'r', encoding='utf-8') as f2:
            text1, text2 = f1.read(), f2.read()
    except Exception as e:
        print(f"Помилка читання файлів: {e}")
        return {}

    results = {}
    for text, filename in zip([text1, text2], [file1, file2]):
        if len(text) > 1_000_000:  # Якщо текст занадто великий, скорочуємо його
            print(f"Увага: скорочуємо текст {filename} для оптимізації.")
            text = text[:1_000_000]
        
        results[filename] = {}
        for substring in substrings:
            print(f"Обробка підрядка '{substring}' у файлі {filename}...")
            try:
                times = {
                    'KMP': timeit.timeit(lambda: kmp_search(text, substring), number=1),
                    'Rabin-Karp': timeit.timeit(lambda: rabin_karp_search(text, substring), number=1),
                    'Boyer-Moore': timeit.timeit(lambda: boyer_moore_search(text, substring), number=1),
                }
                results[filename][substring] = times
            except Exception as e:
                print(f"Помилка для підрядка '{substring}' у файлі {filename}: {e}")
    return results

# Тестові файли та підрядки
file1 = 'article1.txt'
file2 = 'article2.txt'
substrings = ["реалізації", "not_existing_substring"]  # Вказати потрібні підрядки

# Запуск порівняння
results = compare_algorithms(file1, file2, substrings)

# Виведення результатів
for filename, substr_data in results.items():
    print(f"Результати для {filename}:")
    for substring, times in substr_data.items():
        print(f"  Підрядок: {substring}")
        for algorithm, time_taken in times.items():
            print(f"    {algorithm}: {time_taken:.5f} сек.")