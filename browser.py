from sys import argv
from os import mkdir, path


def main():
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
    _, target_dir = argv

    if not path.isdir(target_dir):
        mkdir(target_dir)


    while True:
        raw_input = input()
        site_name = raw_input.rpartition(".")[0]

        if raw_input == 'exit':
            exit()
        elif path.isfile(f'{target_dir}/{site_name}'):
            with open(f'{target_dir}/{site_name}', 'r') as f:
                print(f.read())
        elif raw_input.find('.') == -1:
            print('error wrong url')
        elif raw_input == 'bloomberg.com':
            print(bloomberg_com)
            write_to_file(bloomberg_com, target_dir, site_name)
        elif raw_input == 'nytimes.com':
            print(nytimes_com)
            write_to_file(nytimes_com, target_dir, site_name)
        else:
            print('error')


def write_to_file(url, target_dir, site_name):
    with open(f'{target_dir}/{site_name}', 'w') as f:
        print(url, file=f)


if __name__ == '__main__':
    main()
