#!/usr/bin/env python3

import tornado.ioloop
import tornado.web
import tornado.options
import logging
import json
import toml
import os
import pprint
import subprocess

#globals/defaults

repo_names = []
repo_paths = []

class MainHandler(tornado.web.RequestHandler):
    def initialize(self):
        self.logger = logging.getLogger('tugboat')
        self.logger.setLevel(logging.INFO)

    def post(self):
        self.logger.info('recieved event from GitHub')
        data = json.loads(self.request.body.decode('utf-8'))
        get_the_right_stuff(data)

def set_sail():
    return tornado.web.Application([
        (r"/", MainHandler),
        ])

def get_the_right_stuff(data):
    repo_name = data['repository']['name']
    if repo_name in repo_names:
        repo_path = repo_paths[repo_names.index(repo_name)]
        pull_the_lever(repo_path)

def pull_the_lever(repo_path):
    print('pulling {}'.format(repo_path))
    command = subprocess.run(["git", "-C", repo_path, "pull"], check=True)


def load_config(config_name='config.toml'):
    config = {}
    if not os.path.isfile(config_name):
        print('Missing config.toml!\nDid you make sure to rename config.toml.default?')
        exit(1)
    with open(config_name, 'r', encoding='utf-8') as fp:
        config.update(toml.load(fp))
    
    return config


if __name__ == "__main__":
    #dirty configuration
    config = load_config()
    port = config['connection']['port']
    address = config['connection']['address']
    repo_names = config['repos']['repo_names']
    repo_paths = config['repos']['repo_paths']
    if len(repo_names) != len(repo_paths):
        print('You must have an equal number of repo names and repo paths\nPlease check your configuration file')
        exit(1)
    
    #check that everything is a repo
    for path in repo_paths:
        name = repo_names[repo_paths.index(path)]
        if os.path.isdir(path + '/.git'):
            print('{} is a git repo located at {}'.format(name,path ))
        else:
            print('There is no git repo named {} at {}, exiting...'.format(name, path))
            exit(1)


    boat = set_sail()
    try:
        boat.listen(port, address)
        print('Bound to {} on port {}'.format(address, port))
    except:
        print('Could not bind to {} on port {}'.format(address, port))
        exit(1)
    tornado.ioloop.IOLoop.current().start()
