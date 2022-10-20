import click
from searchor import Engine
import searchor.history as sh

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
        result = eval(f"Engine.{engine}.search('{query}', copy_url={copy}, open_web={open})")
        click.echo(result)
        if open:
            click.echo("opening browser...")
        if copy:
            click.echo("link copied to clipboard")
    except AttributeError:
        click.echo(f"{engine} is not a recognized search engine")

@cli.command()
def history():
    click.echo("history command, coming soon")
    click.echo(sh.DATA_PATH)

if __name__ == "__main__":
    cli()
