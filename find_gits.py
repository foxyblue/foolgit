import os
import pickle


def save_pickle(path, data):
    with open(path, 'wb') as w:
        pickle.dump(data, w, protocol=pickle.HIGHEST_PROTOCOL)
    print("Saved: {}".format(path))


def walker(path):
    locations = []
    for root, dirs, files in os.walk(path):
        for f in files:
            path = os.path.join(root, f)
            if '.git' in path and 'Trash' not in path:
                path, _ = path.split('.git')
                locations.append(path + '.git')
    return set(locations)


if __name__ == '__main__':
    gits = walker(os.path.expanduser('~/library/home/'))
    save_pickle('found_gits.pkl', gits)
