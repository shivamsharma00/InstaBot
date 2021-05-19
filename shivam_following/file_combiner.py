# This script combines the text file and returns a csv file with all the values.
import os

class Combiner:


    def __init__(self, path):
        self.path = path
        # CHANGE THE DIRECTORY
        os.chdir(self.path)
        self.follow_list = []

    def read_folder(self):

        for file in os.listdir():
            if file.endswith('.txt'):
                file_path = f'{self.path}/{file}'
                f = open(file_path, 'r')
                for line in f:
                    if line not in self.follow_list:
                        self.follow_list.append(line)

        with open('shivam_following.txt', 'w') as w:
            for l in self.follow_list:
                w.write(l)

        print('OK Done!')


p = 'Z:\Projects\instagram\shivam_following'
c = Combiner(p)
c.read_folder()
# c.csv_maker()
