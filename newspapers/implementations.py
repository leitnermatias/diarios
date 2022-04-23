from .newspaper import Newspaper, get_html, validate_tags


class Clarin(Newspaper):
    def __init__(self):
        super().__init__("clarin")

    def last_news(self, limit: int = 10) -> list[dict]:

        last_news = list()

        for i in range(int(limit / 10)):
            url = f"https://www.clarin.com/ultimo-momento/ondemand/{i * 10}"
            html = get_html(url)

            soup = self.parser(html, "html.parser")

            title_wrappers = soup.select("li.list-format.list")

            for wrapper in title_wrappers:

                news = dict()

                a_tag = wrapper.select_one("a.link-new")
                h2_tag = wrapper.select_one("h2")
                img_tag = wrapper.select_one("img.img-responsive.intelResolution.lazyload")

                if not validate_tags(a_tag, h2_tag, img_tag):
                    continue

                link = a_tag.get("href", None)
                title = h2_tag.text
                img_src = img_tag.get("src", None)

                if link is not None and title is not None and img_src is not None:
                    news["title"] = title
                    news["link"] = link
                    news["img"] = img_src
                    last_news.append(news)

        return last_news


class LaCapital(Newspaper):
    def __init__(self):
        super().__init__("lacapital")

    def last_news(self, limit: int = 10) -> list[dict]:
        html = get_html("https://www.lacapital.com.ar/secciones/ultimo-momento.html")

        soup = self.parser(html, "html.parser")

        last_news = list()

        title_wrappers = soup.select("article.ultimas-noticias-entry-container")

        for wrapper in title_wrappers:

            if len(last_news) == limit:
                break

            a_tag = wrapper.select_one("a.cover-link")
            h2_tag = wrapper.select_one("h2.entry-title")
            img_tag = wrapper.select_one("picture > img")

            if not validate_tags(a_tag, h2_tag, img_tag):
                continue

            link = a_tag.get("href", None)
            title = h2_tag.text
            img_src = img_tag.get("data-td-src-property", None)

            if link is not None and title is not None and img_src is not None:
                news = dict()
                news["title"] = title
                news["img"] = img_src
                news["link"] = link

                last_news.append(news)

        return last_news


class Rosario3(Newspaper):
    def __init__(self):
        super().__init__("rosario3")

    def last_news(self, limit: int = 10) -> list[dict]:
        html = get_html("https://www.rosario3.com/seccion/ultimas-noticias/")

        soup = self.parser(html, "html.parser")

        last_news = list()

        title_wrappers = soup.select("article")

        for wrapper in title_wrappers:

            if len(last_news) == limit:
                break

            a_tag = wrapper.select_one("a.cover-link")
            h2_tag = wrapper.select_one("h2.title")
            img_tag = wrapper.select_one("figure > img")

            if not validate_tags(a_tag, h2_tag, img_tag):
                continue

            title = h2_tag.text
            link = a_tag.get("href", None)
            img_src = img_tag.get("src", None)

            if title is not None and link is not None and img_src is not None:
                news = dict()
                news["title"] = title
                news["link"] = link
                news["img"] = img_src
                last_news.append(news)

        return last_news
