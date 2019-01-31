import os


def walker(path):
    for root, dirs, files in os.walk(path):
        for f in files:
            path = os.path.join(root, f)
            if '.git' in path:
                print(path)

if __name__ == '__main__':
    walker(os.path.expanduser('~'))
