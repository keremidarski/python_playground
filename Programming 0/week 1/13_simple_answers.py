while True:
    text = input('Enter text: ')

    if 'bye' in text or 'Bye' in text:
        print('Sayounara!')
        break

    if 'hello' in text or 'Hello' in text:
        print('Hello there, good stranger!')
    elif 'how are you' in text or 'How are you' in text:
        print('I am fine, thanks. How are you?')
    elif 'feelings' in text:
        print('I am a machine. I have no feelings.')
    elif 'age' in text:
        print('I have no age. Only current timestamp.')