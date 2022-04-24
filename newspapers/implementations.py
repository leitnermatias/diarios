from .newspaper import Newspaper, get_html, validate_tags, get_json, create_news_dict


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

                a_tag = wrapper.select_one("a.link-new")
                h2_tag = wrapper.select_one("h2")
                img_tag = wrapper.select_one("img.img-responsive.intelResolution.lazyload")

                if not validate_tags(a_tag, h2_tag, img_tag):
                    continue

                link = a_tag.get("href", None)
                title = h2_tag.text
                img_src = img_tag.get("src", None)

                if link is not None and title is not None and img_src is not None:
                    news = create_news_dict(title, link, img_src)
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
                news = create_news_dict(title, link, img_src)
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
                news = create_news_dict(title, link, img_src)
                last_news.append(news)

        return last_news


class LaNacion(Newspaper):
    def __init__(self):
        super().__init__("lanacion")

    def last_news(self, limit: int = 10):

        titles = list()

        page = 1
        while page < 5:
            response = get_json(
                'https://www.lanacion.com.ar/pf/api/v3/content/fetch/acuArticlesSource?query={"size":100,"page":' + str(
                    page) + "}")

            content_elements = response.get("content_elements", None)

            if content_elements is not None:
                [titles.append(title) for title in content_elements]
            else:
                break

            page += 1

        last_news = list()

        for title in titles:

            if len(last_news) == limit:
                break

            title_text = None
            link = None
            img_src = None
            if "headlines" in title and "website_url" in title and "promo_items" in title:
                headlines = title["headlines"]
                link = f"""https://www.lanacion.com.ar{title["website_url"]}"""
                promo_items = title["promo_items"]

                if "basic" in headlines and "basic" in promo_items:
                    title_text = headlines["basic"]

                    if "url" in promo_items["basic"]:
                        img_src = promo_items["basic"]["url"]

            if title_text is not None and link is not None and img_src is not None:
                news = create_news_dict(title_text, link, img_src)
                last_news.append(news)

        return last_news


class Perfil(Newspaper):
    def __init__(self):
        super().__init__("perfil")

    def last_news(self, limit: int = 10):
        html = get_html("https://www.perfil.com/ultimo-momento")

        soup = self.parser(html, "html.parser")

        title_wrapper = soup.select("article.articulo")

        last_news = list()

        for wrapper in title_wrapper:

            if len(last_news) == limit:
                break

            a_tag = wrapper.select_one("a")
            h2_tag = wrapper.select_one("h2")
            img_tag = wrapper.select_one("img.img-fluid")

            if not validate_tags(a_tag, h2_tag, img_tag):
                continue

            title = h2_tag.text
            link = a_tag.get("href", None)
            img_src = img_tag.get("src", None)

            if title is not None and link is not None and img_src is not None:
                news = create_news_dict(title, link, img_src)
                last_news.append(news)

        return last_news
