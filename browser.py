from sys import argv
from os import mkdir, path
from _collections import deque
nytimes_com = '''
This New Liquid Is Magnetic, and Mesmerizing

Scientists have created “soft” magnets that can flow 
and change shape, and that could be a boon to medicine 
and robotics. (Source: New York Times)


Most Wikipedia Profiles Are of Men. This Scientist Is Changing That.

Jessica Wade has added nearly 700 Wikipedia biographies for
 important female and minority scientists in less than two 
 years.

'''

bloomberg_com = '''
The Space Race: From Apollo 11 to Elon Musk

It's 50 years since the world was gripped by historic images
 of Apollo 11, and Neil Armstrong -- the first man to walk 
 on the moon. It was the height of the Cold War, and the charts
 were filled with David Bowie's Space Oddity, and Creedence's 
 Bad Moon Rising. The world is a very different place than 
 it was 5 decades ago. But how has the space race changed since
 the summer of '69? (Source: Bloomberg)


Twitter CEO Jack Dorsey Gives Talk at Apple Headquarters

Twitter and Square Chief Executive Officer Jack Dorsey 
 addressed Apple Inc. employees at the iPhone maker’s headquarters
 Tuesday, a signal of the strong ties between the Silicon Valley giants.
'''


class Browser:
    def __init__(self):
        self.history = deque()

    def start(self):
        target_dir = argv[1]

        if not path.isdir(target_dir):
            mkdir(target_dir)

        while True:
            raw_input = input()
            site_name = raw_input.rpartition(".")[0]
            file_path = f'{target_dir}/{site_name}'
            if site_name:
                self.history.append(site_name)
            if raw_input == 'exit':
                exit()
            elif raw_input == 'back':
                if len(self.history) > 1:
                    self.read_file(f'{target_dir}/{self.history[-2]}')
            elif path.isfile(file_path):
                self.read_file(file_path)
            elif raw_input.find('.') == -1:
                print('error wrong url')
            elif raw_input == 'bloomberg.com':
                print(bloomberg_com)
                self.write_to_file(bloomberg_com, file_path)
            elif raw_input == 'nytimes.com':
                print(nytimes_com)
                self.write_to_file(nytimes_com, file_path)
            else:
                print('error')

    def read_file(self, file_path):
        with open(file_path, 'r') as f:
            print(f.read())


    def write_to_file(self, url, file_path):
        with open(file_path, 'w') as f:
            print(url, file=f)


if __name__ == '__main__':
    Browser().start()
