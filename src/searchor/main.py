import click
from searchor import Engine


@click.command()
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
def cli(engine, query, open, copy):
    click.echo(
        eval(f"Engine.{engine}.search('{query}', copy_url={copy}, open_web={open})")
    )
    if open:
        click.echo("opening browser...")
    if copy:
        click.echo("link copied to clipboard")


if __name__ == "__main__":
    cli()
