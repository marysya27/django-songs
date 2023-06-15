header_links = [
    {'title' : 'Головна', 'url_name' : 'home'},
    {'title' : 'Пісні', 'url_name' : 'show_songs'},
    {'title' : 'Альбоми', 'url_name' : 'show_albums'},
    {'title' : 'SadSvit', 'url_name' : 'about'},
]


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        context['header_links'] = header_links
        return context