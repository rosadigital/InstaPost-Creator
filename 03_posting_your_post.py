from instabot import Bot
import io
import os
from win32com import client
import shutil

class Main():
    def instapost_function(self, post_name):
        try:
            current_directory = os.path.dirname(os.path.realpath(__file__))
            config_folder_to_delete = current_directory + "\\config"
            shutil.rmtree(config_folder_to_delete, ignore_errors=True)
        except:
            pass
        print('--------------------------------')
        print('Converting your PPT to a post on Instagram format.')

        '''Converting PPT into  JPEG'''
        Application = client.Dispatch("PowerPoint.Application")
        current_dir = os.path.dirname(os.path.realpath(__file__))
        pdf = Application.Presentations.Open(current_dir + '\\' + post_name + '.pptx')
        pdf.SaveAs(current_dir, 17)
        pdf.Close()
        Application.Quit()
        os.rename('Slide1.JPG', post_name + '_for_post.jpeg')

        try:
            print('Great, your post was created successfully.'
                  '\nNow, to post on Instagra, please, tap your login and password.')

            write_login = input('Please, write your instagram login here >>> : ')
            write_password = input('Now, please, write your instagram password here >>> : ')

            print('Starting to log in your profile to post your post')

            with io.open(post_name + "_for_description.txt", 'r', encoding='utf8') as f:
                text = f.read()

                '''logging to post'''
                bot = Bot()
                bot.login(username=write_login, password=write_password)
                bot.upload_photo(post_name + '_for_post.jpeg', caption=text)

        except:
            current_directory = os.path.dirname(os.path.realpath(__file__))
            config_folder_to_delete = current_directory + "\\config"
            shutil.rmtree(config_folder_to_delete, ignore_errors=True)

if __name__ == '__main__':
    post_name = input("Write the theme that you wrote while running 02_formatting_post.py."
                         "\n I.e if when running 02_formatting_post.py you wrote Christina_Aguilera, now write againg Christina_Aguilera."
                         "\n Write here, and press enter >>>: ")
    start = Main()
    start.instapost_function(post_name)
    '''After process: deleting folder created automatically while posting and showing final message'''
    current_directory = os.path.dirname(os.path.realpath(__file__))
    config_folder_to_delete = current_directory + "\\config"
    shutil.rmtree(config_folder_to_delete, ignore_errors=True)

    print('LEAVING your profile to post your post')
    print('\nUhuuuu!!! Post posted and process concluded.')