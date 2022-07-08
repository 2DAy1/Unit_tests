def reverse_text(text):
    if not isinstance(text, str):
        raise ValueError(f'Вираз повинен бути типу string')
    return ' '.join(
        reverse_word(word)
        for word in text.split(' ')
    )


def reverse_word(word):
    reversed_alpha = [char for char in word if char.isalpha()]
    return ''.join(
        reversed_alpha.pop() if char.isalpha() else char
        for char in word
    )


if __name__ == '__main__':  # pragma: no cover

    cases = [
        ('abcd efgh', 'dcba hgfe'),
        ('akbcd efg!h', 'dcbka hgf!e'),
        ('', ''),
        ('a', 'a'),
        (' ', ' '),
        ("your funct10n shou1d  work on @ny amount of w0rd5  and other  Ch@r@cter5",
         "ruoy ntcnu10f duoh1s  krow no @yn tnuoma fo d0rw5  dna rehto  re@t@crhC5"),
    ]

    for text, reversed_text in cases:
        assert reverse_text(text) == reversed_text
