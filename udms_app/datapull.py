#!/usr/bin/python3
docstr = """
Datapull

Usage: datapull.py [-h] (<file> <config>)

Options:
  -h --help                                     show this message and exit
"""
from docopt import docopt
import yaml

from cappy import API

def main(args=docopt(docstr)):
    with open(args[_config], 'r') as config_file:
        global config
        config = yaml.load(config_file.read())

    data_pulls = []
    errs_pulls = []
    for project in redcap_configs:
        data, errs = get_redcap_data(project, project['cappy_version'])
        data_pulls.append(data)
        errs_pulls.append(errs)
        for datum in data:
            serialize_redcap_data(datum)

    write_output(data_pulls, errs_pulls)


def get_redcap_data(project_config, cappy_version):
    """
    Goes and returns a tuple with the data that was gotten
    and any possible errors we received

    if we need to pass args to the calls in the future add
    the object to the yaml config and pass it as kwargs
    """
    api = API(project_config['token'], project_config['url'], cappy_version)
    data = {}
    errs = {}
    if project_config['reports']:
        try:
            data['reports'] = str(api.export_reports().content, 'utf-8')
        except Exception as ex:
            errs['reports'] = ex
    if project_config['metadata']:
        try:
            data['metadata'] = str(api.export_metadata().content, 'utf-8')
        except Exception as ex:
            errs['metadata'] = ex

    return data, errs

def write_output(data, errs):
    """
    Writes the output to a file in a directory based on the project name
    and the date that the data was taken
    """
    data_path = config['data_path']
    for datum in data:
        # write out the data to a file that is the
        # name of the project with the date and the type
        # of data
        pass
    for err in errs:
        # do something
        pass


if __name__ == "__main__":
    main(args=docopt(docstr))
