from const.desu_items import DESU_GENRES, DESU_KINDS, DESU_ORDERS
from const.urls import DESU_HEADERS, URL_DESU_API
from desureader.parsers.Parser import Parser
from desureader.utils.utils import get_html
from items import Manga, Chapter, Image, Genre, RequestForm, Kind, Order


class Desu(Parser):
    catalog_name = 'Desu'

    def __init__(self):
        self.url_api = URL_DESU_API
        self.headers = DESU_HEADERS
        self.catalog_id = 0

    def get_manga(self, manga: Manga):
        url = f'{self.url_api}/{manga.id}'
        html = get_html(url, self.headers)
        if html and html.status_code == 200 and html.json():
            data = html.json().get('response')
            manga.genres = [Genre(i.get('id'), i.get('text'), i.get('russian'), i.get('kind'))
                            for i in data.get("genres")]
            manga.score = data.get("score")
            manga.kind = data.get("kind")
            manga.description = data.get("description")
            manga.shikimori_id = data.get("shikimori_id")
            manga.volumes = data.get("chapters").get("last").get("vol")
            manga.chapters = data.get("chapters").get("last").get("ch")
            manga.status = data.get("status")
        return manga

    def search_manga(self, params: RequestForm):
        url = f'{self.url_api}'
        params = {'limit': params.limit, 'search': params.search, 'genres': ','.join([i.name for i in params.genres]),
                  'order': params.order.name, 'kinds': ','.join([i.name for i in params.kinds]), 'page': params.page}
        html = get_html(url, self.headers, params)
        manga = []
        if html and html.status_code == 200 and html.json():
            for i in html.json().get('response'):
                manga.append(Manga(i.get('id'), self.catalog_id, i.get('name'), i.get('russian')))
        return manga

    def get_chapters(self, manga: Manga):
        url = f'{self.url_api}/{manga.id}'
        html = get_html(url, self.headers)
        chapters = []
        if html and html.status_code == 200 and html.json():
            for i in html.json().get('response').get('chapters').get('list'):
                chapters.append(Chapter(i.get('id'), i.get('vol'), i.get('ch'), i.get('title'), 'ru'))
        return chapters

    def get_images(self, manga: Manga, chapter: Chapter):
        url = f'{URL_DESU_API}/{manga.id}/chapter/{chapter.id}'
        html = get_html(url, headers=self.headers)
        if html and html.status_code == 200 and html.json():
            return [Image(i.get('id'), i.get('page'), i.get('img'))
                    for i in html.json().get('response').get('pages').get('list')]
        return []

    def get_image(self, image: Image):
        return get_html(image.img)

    def get_preview(self, manga: Manga):
        return get_html(f'https://desu.me/data/manga/covers/preview/{manga.id}.jpg')

    def get_genres(self):
        return [Genre('', i['name'], i['russian'], '') for i in DESU_GENRES]

    def get_kinds(self) -> list[Kind]:
        return [Kind('', i['name'], i['russian']) for i in DESU_KINDS]

    def get_orders(self) -> list[Order]:
        return [Order('', i['name'], i['russian']) for i in DESU_ORDERS]