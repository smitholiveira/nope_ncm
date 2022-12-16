import yaml
from netmiko import ConnectHandler, NetMikoAuthenticationException, NetMikoTimeoutException

exceptions = (NetMikoAuthenticationException, NetMikoTimeoutException, Exception)


def func_yml(file_path_yaml, group):
    """ Read credentials from a yaml file. """
    with open(file_path_yaml) as f:
        file_yaml = f.read()
    yaml_dict = yaml.load(file_yaml, Loader=yaml.FullLoader)
    return yaml_dict[group]


class Login:
    def __init__(self, var_credentials: dict, var_hosts: list, var_device_type):
        # self.var_credentials = var_credentials
        # self.var_hosts = var_hosts
        # self.var_device_type = var_device_type

        self.output = []

        for hosts in var_hosts:
            device = {
                'device_type': var_device_type,
                'host': hosts,
                # 'global_delay_factor': 2,
                # "read_timeout_override": 90,
                'session_log': 'output_high-level.log'
            }

            device.update(var_credentials)

            with ConnectHandler(**device) as net_connect:
                net_connect.enable()
                self.output.append(net_connect)

    def login(self):
        return self.output


if __name__ == '__main__':
    print(func_yml('pass.yml', 'devnet_iosxe'))
