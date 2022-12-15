import yaml


def func_yml(file_path_yaml, group):
    """ Read credentials from a yaml file. """
    with open(file_path_yaml) as f:
        file_yaml = f.read()
    yaml_dict = yaml.load(file_yaml, Loader=yaml.FullLoader)
    return yaml_dict[group]


if __name__ == '__main__':
    print(func_yml('pass.yml', 'devnet_iosxe'))
