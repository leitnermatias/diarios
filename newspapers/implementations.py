from newspaper import Newspaper


class Clarin(Newspaper):
    def __init__(self):
        super().__init__("clarin")

    def last_news(self, limit: int = 10):

        last_news = []

        for i in range(int(limit / 10)):

            url = f"https://www.clarin.com/ultimo-momento/ondemand/{i * 10}"
            html = self.get_html(url)

            soup = self.parser(html, "html.parser")

            title_wrappers = soup.select("li.list-format.list")

            for wrapper in title_wrappers:

                news = dict()

                a_tag = wrapper.select_one("a.link-new")
                h2_tag = wrapper.select_one("h2")
                img_tag = wrapper.select_one("img.img-responsive.intelResolution.lazyload")

                link = a_tag.get("href", None)
                title = h2_tag.text
                img_src = img_tag.get("src", None)

                if link is not None and title is not None and img_src is not None:
                    news["title"] = title
                    news["link"] = link
                    news["img"] = img_src
                    last_news.append(news)
