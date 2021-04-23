from instabot import Bot
import io
import os
from win32com import client
import shutil


class Main:
    '''This is a method to delete the config directory.
    This directory is created when user log in Instagram, and has to be deleted before log in again.
    Otherwise, we will have an error to run this code.
    Also, this is a static method because it is needed to our process,
    it should be outside our class, but, to keep our code organized, we put it here.'''
    @staticmethod
    def delete_config_folder():
        current_directory = os.path.dirname(os.path.realpath(__file__))
        config_folder_to_delete = current_directory + "\\config"
        return shutil.rmtree(config_folder_to_delete, ignore_errors=True)

    def __init__(self, post_name):
        self.post_name = post_name

    def ppt_to_jpeg(self):
        post_name = self.post_name

        print('--------------------------------')
        print('Converting your PPT to a post on Instagram format.')

        '''Converting PPT into  JPEG'''
        application = client.Dispatch("PowerPoint.Application")
        current_dir = os.path.dirname(os.path.realpath(__file__))
        pdf = application.Presentations.Open(current_dir + '\\' + post_name + '.pptx')
        pdf.SaveAs(current_dir, 17)
        pdf.Close()
        application.Quit()
        os.rename('Slide1.JPG', post_name + '_for_post.jpeg')


class InstagramBot:
    def __init__(self, login, password, post_name):
        self.login = login
        self.password = password
        self.post_name = post_name

    def login_and_posting(self):
        print('\nStarting to log in your profile to post your post.')
        bot = Bot()
        bot.login(username=self.login, password=self.password)
        print('\nBot logged successfully.')

        print('\nStarting to post.')
        illustration_to_post = self.post_name + '_for_post.jpeg'
        text_for_description = io.open(post_name + "_for_description.txt", 'r', encoding='utf8').read()
        bot.upload_photo(photo=illustration_to_post, caption=text_for_description)
        print('LEAVING your profile to post your post')
        print('\nUhuuuu!!! Post posted and process concluded.')


if __name__ == '__main__':
    # Before process: deleting folder created automatically while posting last time
    Main.delete_config_folder()

    # Converting PPT to JPEG
    post_name = input("Write the theme that you wrote while running 02_formatting_post.py."
                      "\n I.e if when running 02_formatting_post.py you wrote Christina_Aguilera, now write again Christina_Aguilera."
                      "\n Write here, and press enter >>>: ")
    start = Main(post_name)
    start.ppt_to_jpeg()
    print('PPT converted to JPEG successfully.')

    # Login and posting on Instagram
    print('\nNow, to post on Instagram, please, tap your profile and password.')

    write_login = input('Please, write your instagram profile here >>> : ')
    write_password = input('Now, please, write your instagram password here >>> : ')

    start = InstagramBot(write_login, write_password, post_name)
    start.login_and_posting()

    '''After process: deleting folder created automatically while posting and showing final message'''
    Main.delete_config_folder()
