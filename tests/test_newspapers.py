from newspapers import __version__, implementations


def news_has_fields(news: dict):
    return "img" in news and "link" in news and "title" in news


def test_version():
    assert __version__ == '0.1.0'


def test_clarin_last_news():
    clarin = implementations.Clarin()

    last_news_10 = clarin.last_news(limit=10)
    last_news_50 = clarin.last_news(limit=50)
    last_news_100 = clarin.last_news(limit=100)

    assert type(last_news_10) is list and type(last_news_50) is list and type(last_news_100) is list
    assert len(last_news_10) == 10 and len(last_news_50) == 50 and len(last_news_100) == 100

    for news in last_news_100:
        assert news_has_fields(news)


def test_lacapital_last_news():
    lacapital = implementations.LaCapital()

    last_news_10 = lacapital.last_news(limit=10)
    last_news_50 = lacapital.last_news(limit=50)
    last_news_100 = lacapital.last_news(limit=100)

    assert type(last_news_10) is list and type(last_news_50) is list and type(last_news_100) is list
    assert len(last_news_10) == 10 and len(last_news_50) == 50 and len(last_news_100) == 100

    for news in last_news_100:
        assert news_has_fields(news)


def test_rosario3_last_news():
    rosario3 = implementations.LaCapital()

    last_news_10 = rosario3.last_news(limit=10)
    last_news_50 = rosario3.last_news(limit=50)
    last_news_100 = rosario3.last_news(limit=100)

    assert type(last_news_10) is list and type(last_news_50) is list and type(last_news_100) is list
    assert len(last_news_10) == 10 and len(last_news_50) == 50 and len(last_news_100) == 100

    for news in last_news_100:
        assert news_has_fields(news)
