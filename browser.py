from _collections import deque
from os import mkdir, path
from re import match
from sys import argv

import requests


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
            if not site_name:
                site_name = raw_input.rpartition(".")[2]
            if site_name.find('.') != -1:
                tmp = site_name.split('.')
                site_name = f'{tmp[1]}_{tmp[0]}'
            file_path = f'{target_dir}/{site_name}'

            if raw_input == 'exit':
                exit()
            elif raw_input == 'back':
                if len(self.history) > 1:
                    self.read_file(f'{target_dir}/{self.history[-2]}')
            elif raw_input.find('.') == -1:
                self.read_file(file_path) if path.isfile(file_path) else print('error wrong url')
            elif match(r'[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)', raw_input):
                content = self.get_site(raw_input)
                self.history.append(site_name)
                print(content)
                self.write_to_file(content, file_path)
            else:
                print('error')

    def get_site(self, raw_input: str):
        if not raw_input.startswith('http'):
            raw_input = f'https://{raw_input}'
        req = requests.get(raw_input, headers={'User-Agent': 'Mozilla/5.0'})
        if not req:
            print(req.status_code, req.reason)
        return req.text

    def read_file(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            print(f.read())

    def write_to_file(self, content, file_path):
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)


if __name__ == '__main__':
    Browser().start()
