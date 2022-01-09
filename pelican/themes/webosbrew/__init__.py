from os import path


def theme_dir():
    return path.dirname(__file__)


def templates_dir():
    return path.join(theme_dir(), 'templates')


def static_dir():
    return path.join(theme_dir(), 'static')


def scss_dir():
    return path.join(static_dir(), 'styles')
