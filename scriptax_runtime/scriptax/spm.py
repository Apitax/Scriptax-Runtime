import click
from pathlib import Path
import json

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

drivers_path = Path(Path(__file__).resolve().parents[2]).joinpath('drivers.json')


def make_file_if_not_exist():
    try:
        with open(drivers_path, 'r') as file:
            pass
    except:
        with open(drivers_path, 'w+') as file:
            json.dump({}, file)


@click.group(context_settings=CONTEXT_SETTINGS)
def spm():
    pass


@spm.command()
@click.argument('package')
@click.argument('driver', required=False)
def install(driver=None, **kwargs):
    package = kwargs['package']
    make_file_if_not_exist()
    with open(drivers_path, 'r') as file:
        data = json.load(file)
    if package in data and driver and driver in data[package]['drivers']:
        print("Error: " + driver + " already installed in package.")
        return
    if not driver and package in data:
        print("Error: " + package + " already installed.")
        return
    if not driver:
        data[package] = {'drivers': []}
    else:
        data[package]['drivers'].append(driver)
    with open(drivers_path, 'w') as file:
        json.dump(data, file)
        if driver:
            print(driver + " installed.")
        else:
            print(package + " installed.")


@spm.command()
@click.argument('package')
@click.argument('driver', required=False)
def uninstall(driver=None, **kwargs):
    package = kwargs['package']
    make_file_if_not_exist()
    with open(drivers_path, 'r') as file:
        data = json.load(file)
    if package in data and driver and driver not in data[package]['drivers']:
        print("Error: " + driver + " not installed in package.")
        return
    if package not in data:
        print("Error: " + package + " not installed.")
        return
    if not driver:
        data.pop(package, None)
    else:
        data[package]['drivers'].remove(driver)
    with open(drivers_path, 'w') as file:
        json.dump(data, file)
        if driver:
            print(driver + " uninstalled.")
        else:
            print(package + " uninstalled.")


@spm.command()
def list():
    make_file_if_not_exist()
    with open(drivers_path, 'r') as file:
        data = json.load(file)
        print('=== Drivers ===')
        print(json.dumps(data, indent=2, sort_keys=True))


if __name__ == '__main__':
    spm()
