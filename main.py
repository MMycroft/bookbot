import sys
import pathlib as pl
import stats as st

def get_book_text(filepath: pl.Path) -> str:

    with open(filepath) as file:
        file_contents = file.read()

    return file_contents


def main():

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    base_dir: pl.Path = pl.Path(__file__).parent

    for book_path in sys.argv[1:]:

        book_text: str = get_book_text(base_dir / book_path)

        num_words: int = st.get_num_words(book_text)

        print(
            f"""============ BOOKBOT ============
            Analyzing book found at books/frankenstein.txt...
            ----------- Word Count ----------
            Found {num_words} total words
            --------- Character Count -------"""
        )

        char_counts: list[dict] = st.sort_char_counts(st.get_char_counts(book_text))
        for char_count in char_counts:
            if char_count["char"].isalpha():
                print(f'{char_count["char"]}: {char_count["count"]}')
        print("============= END ===============\n")

if __name__ == "__main__":
    main()
