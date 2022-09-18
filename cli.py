import click
from newspapers import implementations

diarios: list[implementations.Newspaper] = [
    implementations.Clarin(), 
    implementations.LaCapital(), 
    implementations.Rosario3(), 
    implementations.LaNacion(), 
    implementations.Perfil()
]


@click.command()
@click.option("--newspaper", required=True, help="Name of the newspaper to use, it can be: clarin, lacapital, rosario3, lanacion, perfil, all")
@click.option("--limit", default=10, help="The limit of news to get from the newspaper")
def diarios_cli(newspaper, limit):

    if newspaper == "all":

        news_gathered = dict(
            clarin=0,
            lacapital=0,
            rosario3=0,
            lanacion=0,
            perfil=0
        )

        for diario in diarios:
            last_news = diario.last_news(limit=limit)
            news_gathered[diario.name] = len(last_news)

            click.secho(f" Newspaper: {diario.name}", bg="yellow")

            for news in last_news:
                click.secho(f"{news['title']}", fg="green")
                click.secho(f"{news['link']}", fg="blue")
                click.echo()
        
        click.secho(f"Total news: {sum(news_gathered.values())}", bg="green")
        
        for newspaper_name in news_gathered.keys():
            click.secho(f"Total news for {newspaper_name}: {news_gathered[newspaper_name]}", bg="green")

    else:

        impl: implementations.Newspaper = None
        for diario in diarios:
            if diario.name == newspaper:
                impl = diario
                break
        
        if impl is None:
            click.echo(f"The newspaper {newspaper} is not available")
            return

        last_news = impl.last_news(limit=limit)

        for news in last_news:
            click.secho(f"{news['title']}", fg="green")
            click.secho(f"{news['link']}", fg="blue")
            click.echo()

        
        click.secho(f"Total news: {len(last_news)}", bg="green")


if __name__ == "__main__":
    diarios_cli()