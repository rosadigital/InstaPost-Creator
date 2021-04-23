import wikipedia
import pandas as pd
import requests
from bs4 import BeautifulSoup
import codecs

class Main():
    def information(self, search_input, language):
        option_for_info = input("\n Now choose one of the options bellow, and press enter:"
                                "\n 01 - to input your own adjusted text; or"
                                "\n 02 - to get a text from wikipedia."
                                "\n Write here >>>: ")

        if option_for_info == "01":
            '''setting up info out of wikipedia'''
            summary_original = input("Write the text here: ")
            summary_original_len = len(summary_original)

        else:
            '''setting up language'''
            wikipedia.set_lang(language)

            '''setting up searching on wikipedia'''
            summary_original = wikipedia.summary(search_input)
            summary_original_len = len(summary_original)

        print('\n Creating text for your post.')

        '''Adjusting text to the limit of characters of post description'''
        limits = [200, 2000]

        for limit in limits:
            if limit == 200:  # create text for post
                if summary_original_len < limit:  # does not adjust the text for the limit of characters
                    file = codecs.open(search_input + "_for_post.txt", "w", encoding="utf-8")
                    file.write(summary_original)
                    file.close()
                else:  # does adjust the text for the limit of characters
                    pd.set_option('display.max_rows', None)
                    pd.set_option('display.max_columns', None)

                    '''creating dataframe'''
                    amount_of_characters_to_table = []
                    accumulated_amount_of_characters_to_table = []
                    summary_of_sentence_adjusted_to_table = []

                    table_of_sentence = {
                        'amount_of_characters': amount_of_characters_to_table,
                        'text': summary_of_sentence_adjusted_to_table
                    }

                    '''make split of sentences into groups'''
                    summary = summary_original.split(".")

                    '''count the amount of sentences and insert period on each sentence'''
                    groups_of_sentence = len(summary)
                    n = 0
                    while n < groups_of_sentence:
                        summary_of_sentence_adjusted = summary[n] + "."
                        summary_of_sentence_adjusted_to_table.append(summary_of_sentence_adjusted)

                        amount_of_characters = len(summary_of_sentence_adjusted)
                        amount_of_characters_to_table.append(amount_of_characters)

                        n += 1

                    '''creating dataframe'''
                    table_of_sentence = pd.DataFrame(data=table_of_sentence)

                    '''creating column amount_of_characters_accumulated'''
                    amount_of_characters_accumulated_to_table = []
                    table_of_sentence['amount_of_characters_accumulated'] = table_of_sentence[
                        'amount_of_characters'].cumsum()
                    table_of_sentence = table_of_sentence[
                        ["amount_of_characters", "amount_of_characters_accumulated", "text"]]

                    '''remerging sentences until instagram limit'''
                    '''01 - removing lines over the instagram limit'''
                    table_of_sentence = table_of_sentence[table_of_sentence['amount_of_characters_accumulated'] < limit]

                    '''02 - merging text lines'''
                    final_sentence_merged = []
                    final_sentence_merged = ''.join(table_of_sentence['text'])

                    f = open(search_input + "_for_post.txt", "w", encoding="utf-8")
                    f.write(final_sentence_merged)
                    f.close()

            else:
                if summary_original_len < limit:  # does not adjust the text for the limit of characters
                    file = codecs.open(search_input + "_for_description.txt", "w", encoding="utf-8")
                    file.write(summary_original)
                    file.close()
                else:  # does adjust the text for the limit of characters
                    pd.set_option('display.max_rows', None)
                    pd.set_option('display.max_columns', None)

                    '''creating dataframe'''
                    amount_of_characters_to_table = []
                    accumulated_amount_of_characters_to_table = []
                    summary_of_sentence_adjusted_to_table = []

                    table_of_sentence = {
                        'amount_of_characters': amount_of_characters_to_table,
                        'text': summary_of_sentence_adjusted_to_table
                    }

                    '''make split of sentences into groups'''
                    summary = summary_original.split(".")

                    '''count the amount of sentences and insert period on each sentence'''
                    groups_of_sentence = len(summary)
                    n = 0
                    while n < groups_of_sentence:
                        summary_of_sentence_adjusted = summary[n] + "."
                        summary_of_sentence_adjusted_to_table.append(summary_of_sentence_adjusted)

                        amount_of_characters = len(summary_of_sentence_adjusted)
                        amount_of_characters_to_table.append(amount_of_characters)

                        n += 1

                    '''creating dataframe'''
                    table_of_sentence = pd.DataFrame(data=table_of_sentence)

                    '''creating column amount_of_characters_accumulated'''
                    amount_of_characters_accumulated_to_table = []
                    table_of_sentence['amount_of_characters_accumulated'] = table_of_sentence[
                        'amount_of_characters'].cumsum()
                    table_of_sentence = table_of_sentence[
                        ["amount_of_characters", "amount_of_characters_accumulated", "text"]]

                    '''remerging sentences until instagram limit'''
                    '''01 - removing lines over the instagram limit'''
                    table_of_sentence = table_of_sentence[table_of_sentence['amount_of_characters_accumulated'] < limit]

                    '''02 - merging text lines'''
                    final_sentence_merged = []
                    final_sentence_merged = ''.join(table_of_sentence['text'])

                    f = open(search_input + "_for_description.txt", "w", encoding="utf-8")
                    f.write(final_sentence_merged)
                    f.close()
        print('\n Text created for your post.')

    def ilustration(self, search_input):
        print('\n Getting illustration for your post.')

        '''getting images'''
        try:
            '''getting image on wikipedia'''
            # Coletar a primeira página da lista de artistas
            page = requests.get('https://pt.wikipedia.org/wiki/' + search_input)
            soup = BeautifulSoup(page.text, 'html.parser')
            img = soup.find(class_='image')
            img = img.find_next()
            img_url = ' http:' + (img['src'])

            r = requests.get(img_url, allow_redirects=True)
            open(search_input + '.jpeg', 'wb').write(r.content)
            print('\n Illustration gotten for your post.')
        except:
            print("Sorry, but the image on wikipedia is not so good."
                  "\n Please, one better on google.")

        print('\n Uhuuuu!!! Process concluded.')

if __name__ == '__main__':
    search_input = input("Write the theme that you would like to research on Wikipedia for your post."
                         "\n Note: please, write the theme as can be found on wikipedia URL."
                         "\n I.e from https://pt.wikipedia.org/wiki/Christina_Aguilera, just write the end Christina_Aguilera."
                         "\n Write here, and press enter >>>: ")
    start = Main()
    language = input("Write the language that you would like to research on Wikipedia for your post."
                     "\n Set `prefix` to one of the two letter prefixes found on the `list of all Wikipedias http://meta.wikimedia.org/wiki/List_of_Wikipedias"
                     "\n I.e 'pt' for portuguese, 'en' for english or 'zh' for chinese."
                     "\n Write here, and press enter >>>: ")
    start.information(search_input, language)
    start.ilustration(search_input)
