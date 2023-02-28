import click
from searchor import Engine
from searchor import Information
import searchor.history


@click.group()
def cli():
    pass


@cli.command()
@click.option(
    "-o",
    "--open",
    is_flag=True,
    default=False,
    show_default=True,
    help="Opens your web browser to the generated link address",
)
@click.option(
    "-c",
    "--copy",
    is_flag=True,
    default=False,
    show_default=True,
    help="Copies the generated link address to your clipboard",
)
@click.argument("engine")
@click.argument("query")
def search(engine, query, open, copy):
    try:
        url = Engine[engine].search(query, copy_url=copy, open_web=open)
        click.echo(url)
        searchor.history.update(engine, query, url)
        if open:
            click.echo("opening browser...")
        if copy:
            click.echo("link copied to clipboard")
    except AttributeError:
        print("engine not recognized")



@cli.command()
@click.option(
  "-g",
  "--getinfo",
  is_flag=True,
  default=False,
  show_default=True,
  help="Gathers information about a topic"
)
@click.argument("topic", type=str)
def getinfo(getinfo, topic):
  try:
    click.echo(Information.getinfo(topic))
  finally:
    pass


@cli.command()
@click.option(
  "-ws",
  "--scrape",
  is_flag=True,
  default=False,
  show_default=True,
  help="Web scrapes a website"
)
@click.argument("url", type=str)
def webscrape(webscrape, url):
  click.echo(Information.scrape(url))


  
@cli.command()
@click.option(
    "-c",
    "--clear",
    is_flag=True,
    default=False,
    show_default=True,
    help="clears the search history",
)
def history(clear):
    if clear:
        searchor.history.clear()
    else:
        searchor.history.view()


if __name__ == "__main__":
    cli()
