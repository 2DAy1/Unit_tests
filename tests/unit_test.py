from unittest import TestCase, main
import anagrams


class TypycalAnagramsTest(TestCase):

    def test_string(self):
        self.assertEqual(isinstance(anagrams.reverse_text(''), str), True)
        self.assertEqual(isinstance(anagrams.reverse_word(''), str), True)

    def test_reverse(self):
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
            self.assertEqual(anagrams.reverse_text(text), reversed_text)


class AtypycalAnagramsTest(TestCase):

    def test_string(self):
        with self.assertRaises(ValueError) as e:
            anagrams.reverse_text(4)
        self.assertEqual(('Вираз повинен бути типу string', e.exception.args[0]))


if __name__ == '__main__':
    main()
