from os import path
from typing import Callable


def theme_dir():
    return path.dirname(__file__)


def templates_dir():
    return path.join(theme_dir(), 'templates')


def static_dir():
    return path.join(theme_dir(), 'static')


def scss_dir():
    return path.join(theme_dir(), 'styles')


def pagination_data(current: int, total: int, link_maker: Callable[[int], str]):
    """
    @see https://gist.github.com/kottenator/9d936eb3e4e3c3e02598#gistcomment-3413141
    """

    def item(p):
        return {'href': link_maker(p), 'page': p, 'current': p == current}

    def disabled():
        return {'disabled': True}

    def gap():
        return {'gap': True}

    if total <= 10:
        return {
            'entries': list(map(lambda p: item(p), range(1, min(total, 10) + 1)))
        }

    center = [item(current - 2), item(current - 1), item(current), item(current + 1), item(current + 2)]
    filtered_center = list(filter(lambda p: 1 < p['page'] < total, center))
    include_three_left = current == 5
    include_three_right = current == total - 4
    include_left_dots = current > 5
    include_right_dots = current < total - 4

    if include_three_left:
        filtered_center.insert(0, item(2))
    if include_three_right:
        filtered_center.append(item(total - 1))

    if include_left_dots:
        filtered_center.insert(0, gap())
    if include_right_dots:
        filtered_center.append(gap())

    entries = [item(1), *filtered_center, item(total)]

    return {
        'prev': item(current - 1) if current > 1 else disabled(),
        'next': item(current + 1) if current < total else disabled(),
        'entries': entries
    }
