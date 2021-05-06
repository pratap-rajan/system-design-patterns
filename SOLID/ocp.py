from bs4 import BeautifulSoup
from urllib.request import urlopen
import ssl

# To Mute the SSL Certificate Verification
ssl._create_default_https_context = ssl._create_unverified_context


def read_localfile(file):
    '''Read file'''
    return open(file, "r").read()


def number_of_words(content):
    '''Count number of words in a file'''
    return len(content.split())


def count_word_occurrences(word, content):
    '''Count number of word occurrences in a file'''

    counter = 0
    for e in content.split():
        if word.lower() == e.lower():
            counter += 1
    return counter


def percentage_of_word(word, content):
    '''Calculate ratio of number of word occurrences to number of all words in a text'''
    total_words = number_of_words(content)
    word_occurrences = count_word_occurrences(word, content)
    return word_occurrences/total_words


def percentage_of_word_in_localfile(word, file):
    '''Calculate ratio of number of word occurrences to number of all words in a text file'''
    content = read_localfile(file)
    return percentage_of_word(word, content)


def get_text_from_url(url):
    '''Extract html as string from given url'''
    page = urlopen(url).read()
    soup = BeautifulSoup(page, features="html.parser")
    text = soup.get_text()
    return text


if __name__ == "__main__":

    # Print out ratio of 'and' occurrences to the total number of words in the 'ufo.txt'
    print(percentage_of_word_in_localfile('and', 'random.txt'))

    content = get_text_from_url('https://en.wikipedia.org/wiki/Main_Page')
    print(count_word_occurrences('and', content))