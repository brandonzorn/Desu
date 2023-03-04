from nlightreader.consts import URL_DESU_API, DESU_HEADERS, URL_DESU, DesuItems
from nlightreader.items import Manga, Chapter, Image, Genre, RequestForm, Kind, Order
from nlightreader.parsers.Parser import Parser
from nlightreader.utils.utils import get_html, get_data


class Desu(Parser):
    catalog_name = 'Desu'

    def __init__(self):
        self.url_api = URL_DESU_API
        self.headers = DESU_HEADERS
        self.catalog_id = 0

    def get_manga(self, manga: Manga):
        url = f'{self.url_api}/{manga.content_id}'
        html = get_html(url, self.headers)
        if html and html.status_code == 200 and html.json():
            data = get_data(html.json(), ['response'], {})
            manga.genres = [Genre(i.get('id'), self.catalog_id, i.get('text'), i.get('russian'))
                            for i in data.get("genres")]
            manga.score = data.get("score")
            manga.kind = data.get("kind")
            manga.description = data.get("description")
            manga.volumes = data.get("chapters").get("last").get("vol")
            manga.chapters = data.get("chapters").get("last").get("ch")
            manga.status = data.get("status")
        return manga

    def search_manga(self, form: RequestForm):
        url = f'{self.url_api}'
        params = {'limit': form.limit, 'search': form.search, 'genres': ','.join([i.name for i in form.genres]),
                  'order': form.order.name, 'kinds': ','.join([i.name for i in form.kinds]), 'page': form.page}
        html = get_html(url, self.headers, params)
        manga = []
        if html and html.status_code == 200 and html.json():
            for i in get_data(html.json(), ['response']):
                manga.append(Manga(i.get('id'), self.catalog_id, i.get('name'), i.get('russian')))
        return manga

    def get_chapters(self, manga: Manga):
        url = f'{self.url_api}/{manga.content_id}'
        html = get_html(url, self.headers)
        chapters = []
        if html and html.status_code == 200 and html.json():
            for i in get_data(html.json(), ['response', 'chapters', 'list']):
                chapters.append(Chapter(i.get('id'), self.catalog_id, i.get('vol'), i.get('ch'), i.get('title'), 'ru'))
        return chapters

    def get_images(self, manga: Manga, chapter: Chapter):
        url = f'{URL_DESU_API}/{manga.content_id}/chapter/{chapter.content_id}'
        html = get_html(url, headers=self.headers)
        images = []
        if html and html.status_code == 200 and html.json():
            for i in get_data(html.json(), ['response', 'pages', 'list']):
                image_id = i.get('id')
                page = i.get('page')
                img: str = i.get('img')
                images.append(Image(image_id, page, img))
        return images

    def get_image(self, image: Image):
        return get_html(image.img)

    def get_preview(self, manga: Manga):
        return get_html(f'https://desu.me/data/manga/covers/preview/{manga.content_id}.jpg')

    def get_genres(self):
        return [Genre('', self.catalog_id, i['name'], i['russian']) for i in DesuItems.GENRES]

    def get_kinds(self) -> list[Kind]:
        return [Kind('', self.catalog_id, i['name'], i['russian']) for i in DesuItems.KINDS]

    def get_orders(self) -> list[Order]:
        return [Order('', self.catalog_id, i['name'], i['russian']) for i in DesuItems.ORDERS]

    def get_manga_url(self, manga: Manga) -> str:
        return f"{URL_DESU}/manga/{manga.content_id}"
