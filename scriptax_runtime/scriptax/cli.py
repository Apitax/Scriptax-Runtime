import click
from scriptax_runtime.invoker import execute

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


@click.group(context_settings=CONTEXT_SETTINGS, invoke_without_command=True)
@click.version_option(version='0.0.1')
@click.pass_context
@click.argument('file')
@click.option('--debug', is_flag=True)
def scriptax(ctx, **kwargs):
    if ctx.invoked_subcommand is None:
        print("Executing file: " + kwargs['file'])
        print()
        block_status, visitor = execute(file=kwargs['file'], debug=kwargs['debug'])
        print("RESULT: " + str(block_status.result))


@scriptax.command()
@click.argument('file')
def file(**kwargs):
    print(kwargs['file'])


if __name__ == '__main__':
    scriptax()
