from os import path


def scss_dir():
    return path.join(path.dirname(__file__), 'static', 'styles')


def templates_dir():
    return path.join(path.dirname(__file__), 'templates')
