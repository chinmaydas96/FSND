import urllib
import os


def read_text():
    file_path = os.getcwd()
    os.chdir(file_path)
    quotes = open("word.txt")
    contents = quotes.read()
    quotes.close()
    check_word(contents)


def check_word(text_to_check):
    connection = urllib.urlopen(
        "http://www.wdylike.appspot.com/?q=" + text_to_check)
    output = connection.read()
    connection.close()
    if "true" in output:
        print ("please check the text")
    elif "false" in output:
        print ("everything is alright")
    else:
        print ("could not scan")


read_text()
