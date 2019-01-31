"""Transforms pickle data into display model."""

import os
import json
import pickle
from collections import defaultdict


def load_pickle(path):
    with open(path, 'rb') as r:
        b = pickle.load(r)
    return list(b)


data = defaultdict(dict)

paths = load_pickle('found_gits.pkl')
for path in paths:
    components = path.split('/')
    group, repo = components[-3], components[-2]
    data[group].update({repo: path})

home = dict(data)['home']

model = [
    {
        'group': 'home',
        'repo': key,
        'path': value.replace(os.path.expanduser('~'), '~'),
    } for key, value in home.items()
]



from fool import console

from fool.content import  Column
from fool.windows import TableWindow


def git_view(screen, model):
    items = model

    main = TableWindow(w=120, items=items)
    columns = [
        Column(name='group', size=6, align='left'),
        Column(name='repo', size=20, align='left'),
        Column(name='path', size=40, align='left'),
    ]
    main.content = columns
    return [main]


console.display(git_view, model, close='q')
