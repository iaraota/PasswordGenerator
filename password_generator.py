import string
import random
import argparse
import sys


def password_generator(length=20, lowercase=True, uppercase=True, numbers=True, symbols=True, punctuation=False):
    """Strong Password Generator.

    Parameters
    ----------
    length : int, optional
        Password length. Default is 20.
    lowercase : bool, optional
        Include lowercase characters (abcdefghijklmnopqrstuvwxyz).
        Default is True.
    uppercase : bool, optional
        Include uppercase characters (ABCDEFGHIJKLMNOPQRSTUVWXYZ).
        Default is True.
    numbers : bool, optional
        Include numbers (0123456789).
        Default is True.
    symbols : bool, optional
        Include common symbols (@#$%_-).
        Default is True.
    punctuation : bool, optional
        Include all punctuation (!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~).
        Default is False.

    """
    if not any([lowercase, uppercase, numbers, symbols, punctuation]):
        sys.tracebacklimit = 0
        raise ValueError('Cannot set all characters to False!')
    string_symbols = '@#$_-' * 5
    chars = string.ascii_lowercase * lowercase
    chars += string.ascii_uppercase * uppercase
    chars += string.digits * numbers * 3
    chars += string_symbols * symbols
    chars += string.punctuation * punctuation

    print(''.join(random.choice(chars) for _ in range(length)))


parser = argparse.ArgumentParser(description='Strong Password Generator.')
parser.add_argument('--length', '-l', type=int,
                    default=20, help='Set password length. Default is 20')
parser.add_argument('--lowercase', '-lc', action='store_false',
                    help='Remove lowercase characters.')
parser.add_argument('--uppercase', '-uc', action='store_false',
                    help='Remove uppercase characters.')
parser.add_argument('--numbers', '-n', action='store_false',
                    help='Remove numbers.')
parser.add_argument('--symbols', '-s', action='store_false',
                    help='Remove common symbols (@#$_-).')
parser.add_argument('--punctuation', '-p',  action='store_true',
                    help=f'Include all punctuation.')


args = parser.parse_args()

password_generator(args.length, args.lowercase, args.uppercase,
                   args.numbers, args.symbols, punctuation=args.punctuation)
