import click


class OrderCommands(click.Group):
    def list_commands(self, ctx: click.Context) -> list[str]:
        return list(self.commands)


@click.group(cls=OrderCommands)
def cli():
    """
    Creates documents and fine-tunes Llama2

    To get started, obtain a Replicate/OpenAI API Key and set it like this:

    \b
        $ llama init --provider replicate
        Enter key: ...

    """


@cli.command()
def init():
    """Initializes API keys"""
    click.echo("Keys")


@cli.command()
@click.option("-s", "--src", help="Path to file to finetune")
@click.option("-o", "--out", "output", help="Path to output")
def create(src, output, _type="instruct_chat"):
    """Creates dataset"""
    click.echo(f"Source: {src}")
    click.echo(f"Destination: {output}")


@cli.command()
def tune():
    """Fine-tunes dataset"""
