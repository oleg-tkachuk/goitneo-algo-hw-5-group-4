import timeit

# Implementing the Boyer-Moore, Knuth-Morris-Pratt, and Rabin-Karp algorithms

# Boyer-Moore Algorithm
def boyer_moore_search(text, pattern):
    def build_last(pattern):
        last = {}
        for i in range(len(pattern)):
            last[pattern[i]] = i
        return last

    last = build_last(pattern)
    n = len(text)
    m = len(pattern)
    i = m - 1
    if i > n - 1:
        return -1
    j = m - 1
    while True:
        if pattern[j] == text[i]:
            if j == 0:
                return i
            else:
                i -= 1
                j -= 1
        else:
            lo = last.get(text[i], -1)
            i = i + m - min(j, 1 + lo)
            j = m - 1
        if i > n - 1:
            break
    return -1

# Knuth-Morris-Pratt Algorithm
def knuth_morris_pratt_search(text, pattern):
    def build_prefix(pattern):
        prefix = [0] * len(pattern)
        j = 0
        for i in range(1, len(pattern)):
            while j > 0 and pattern[j] != pattern[i]:
                j = prefix[j - 1]
            if pattern[i] == pattern[j]:
                j += 1
            prefix[i] = j
        return prefix

    prefix = build_prefix(pattern)
    j = 0
    for i in range(len(text)):
        while j > 0 and text[i] != pattern[j]:
            j = prefix[j - 1]
        if text[i] == pattern[j]:
            j += 1
        if j == len(pattern):
            return i - (j - 1)
    return -1

# Rabin-Karp Algorithm
def rabin_karp_search(text, pattern):
    d = 256
    q = 101
    m = len(pattern)
    n = len(text)
    h = pow(d, m-1) % q
    p = 0
    t = 0
    result = []

    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q

    for s in range(n - m + 1):
        if p == t:
            match = True
            for i in range(m):
                if pattern[i] != text[s + i]:
                    match = False
                    break
            if match:
                return s
        if s < n - m:
            t = (t - h * ord(text[s])) % q
            t = (t * d + ord(text[s + m])) % q
            t = (t + q) % q
    return -1

# Timing the algorithms for each text and substring
def time_search_algorithm(algorithm, text, substring):
    return timeit.timeit(lambda: algorithm(text, substring), number=100)

def main():
    file_path_1 = './data/article_1.txt'
    file_path_2 = './data/article_2.txt'

    # Load the generated text files
    with open(file_path_1, 'r') as file:
        text1 = file.read()

    with open(file_path_2, 'r') as file:
        text2 = file.read()

    # Select substrings for testing
    existing_substring_1 = text1[500:520]  # Substring that exists in the text1
    existing_substring_2 = text2[200:220]  # Substring that exists in the text1
    fake_substring = "xyz"  # Substring that does not exist in the text

    # Testing on Text 1
    bm_time_text1_existing = time_search_algorithm(boyer_moore_search, text1, existing_substring_1)
    kmp_time_text1_existing = time_search_algorithm(knuth_morris_pratt_search, text1, existing_substring_1)
    rk_time_text1_existing = time_search_algorithm(rabin_karp_search, text1, existing_substring_1)

    bm_time_text1_fake = time_search_algorithm(boyer_moore_search, text1, fake_substring)
    kmp_time_text1_fake = time_search_algorithm(knuth_morris_pratt_search, text1, fake_substring)
    rk_time_text1_fake = time_search_algorithm(rabin_karp_search, text1, fake_substring)

    print(f"Homework 5 - Task 3 | \n Text 1, \n Algorithm: Boyer-Moore, \n existing substring, \n the search time is: {bm_time_text1_existing} seconds")
    print(f"Homework 5 - Task 3 | \n Text 1, \n Algorithm: Knuth-Morris-Pratt, \n existing substring, \n the search time is: {kmp_time_text1_existing} seconds")
    print(f"Homework 5 - Task 3 | \n Text 1, \n Algorithm: Rabin-Karp, \n existing substring, \n the search time is: {rk_time_text1_existing} seconds")

    print(f"Homework 5 - Task 3 | \n Text 1, \n Algorithm: Boyer-Moore, \n fake substring, \n the search time is: {bm_time_text1_fake} seconds")
    print(f"Homework 5 - Task 3 | \n Text 1, \n Algorithm: Knuth-Morris-Pratt, \n fake substring, \n the search time is: {kmp_time_text1_fake} seconds")
    print(f"Homework 5 - Task 3 | \n Text 1, \n Algorithm: Rabin-Karp, \n fake substring, \n the search time is: {rk_time_text1_fake} seconds")

    # Testing on Text 2
    bm_time_text2_existing = time_search_algorithm(boyer_moore_search, text2, existing_substring_2)
    kmp_time_text2_existing = time_search_algorithm(knuth_morris_pratt_search, text2, existing_substring_2)
    rk_time_text2_existing = time_search_algorithm(rabin_karp_search, text2, existing_substring_2)

    bm_time_text2_fake = time_search_algorithm(boyer_moore_search, text2, fake_substring)
    kmp_time_text2_fake = time_search_algorithm(knuth_morris_pratt_search, text2, fake_substring)
    rk_time_text2_fake = time_search_algorithm(rabin_karp_search, text2, fake_substring)

    print(f"Homework 5 - Task 3 | \n Text 2, \n Algorithm: Boyer-Moore, \n existing substring, \n the search time is: {bm_time_text2_existing} seconds")
    print(f"Homework 5 - Task 3 | \n Text 2, \n Algorithm: Knuth-Morris-Pratt, \n existing substring, \n the search time is: {kmp_time_text2_existing} seconds")
    print(f"Homework 5 - Task 3 | \n Text 2, \n Algorithm: Rabin-Karp, \n existing substring, \n the search time is: {rk_time_text2_existing} seconds")

    print(f"Homework 5 - Task 3 | \n Text 2, \n Algorithm: Boyer-Moore, \n fake substring, \n the search time is: {bm_time_text2_fake} seconds")
    print(f"Homework 5 - Task 3 | \n Text 2, \n Algorithm: Knuth-Morris-Pratt, \n fake substring, \n the search time is: {kmp_time_text2_fake} seconds")
    print(f"Homework 5 - Task 3 | \n Text 2, \n Algorithm: Rabin-Karp, \n fake substring, \n the search time is: {rk_time_text2_fake} seconds")

if __name__ == "__main__":
    print(f"Homework 5 - Task 3 | Starting...\n")
    main()
    print(f"\nHomework 5 - Task 3 | Done")
