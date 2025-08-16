from pathlib import Path

def get_num_words(text: str) -> int:
    words: list[str] = text.split()
    return len(words)

def get_char_counts(text: str) -> dict[str,int]:
    counts: dict[str, int] = {}
    for c in text:
        char: str = c.lower()
        if char not in counts:
            counts[char] = 0
        counts[char] += 1
    return counts

def sort_char_counts(char_counts: dict[str,int]) -> list[dict]:

    def sort_on(item: dict[str,int]) -> int:
        return item["count"]

    char_count_list: list[dict] = []
    for char, count in char_counts.items():
        char_count_list.append({"char": char, "count": count})

    char_count_list.sort(reverse=True, key=sort_on)

    return char_count_list

