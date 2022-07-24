from googletrans import Translator
import os


def add_sub_file(path_of_file: str):
    ''' создает файл с двойными субтитрами в каталоге path'''
    translator = Translator()
    path_en_file = path_of_file
    path_ru_file = path_en_file.replace('en_US.srt', 'en+ru_EN+RU.srt')

    en_file = open(path_en_file, "r", encoding='utf-8')
    ru_file = open(path_ru_file, "w+", encoding='utf-8')

    lines_en = en_file.readlines()
    # итерация по строкам
    for i in range(0, len(lines_en) - 1):
        '''
        if (i - 2) % 4 != 0:
            ru_file.write(lines_en[i])      Если нужны только русские субтитры, а не двойные
            '''

        ru_file.write(lines_en[i])
        if (i - 2) % 4 == 0:
            translation = translator.translate(lines_en[i], dest='ru')
            print(translation.text)
            ru_file.write(translation.text)
            ru_file.write('\n')

    # закрываем файлы
    en_file.close()
    ru_file.close()

path_dir = str(input('Введите путь до директории с файлами субтитров (вложенные папки будут учитываться):'+'\n'))
#path_dir = r"D:\LEARNING\[04-2022] complete-python-developer-zero-to-mastery\03 Python Basics\026 Variables.en_US.srt"


for root, dirs, files in os.walk(path_dir):
    for file in files:
        if (file.endswith("en_US.srt")):
            print(os.path.join(root, file))
            add_sub_file(os.path.join(root, file))
add_sub_file(r"D:\LEARNING\[04-2022] complete-python-developer-zero-to-mastery\03 Python Basics\026 Variables.en_US.srt")


