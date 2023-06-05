import sys

translate = {
    'CU': 'see you',
    ':-)': 'I’m happy',
    ':-(': 'I’m unhappy',
    ';-)': 'wink',
    ':-P': 'stick out my tongue',
    '(~.~)': 'sleepy',
    'TA': 'totally awesome',
    'CCC': 'Canadian Computing Competition',
    'CUZ': 'because',
    'TY': 'thank-you',
    'YW': 'you’re welcome',
    'TTYL': 'talk to you later'
}

while True:
    short_form = sys.stdin.readline().rstrip()

    print(translate.get(short_form, short_form))

    if short_form == 'TTYL':
        break
