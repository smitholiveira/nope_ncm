import yaml
from netmiko import ConnectHandler, NetMikoAuthenticationException, NetMikoTimeoutException


exceptions = (
    NetMikoAuthenticationException,
    NetMikoTimeoutException,
    Exception)


def func_yml(file_path_yaml, group):
    """ Read key/value and list from a yaml file. """
    with open(file_path_yaml) as f:
        file_yaml = f.read()
    yaml_dict = yaml.load(file_yaml, Loader=yaml.FullLoader)
    return yaml_dict[group]


class Login:
    def __init__(self, var_credentials: dict, var_hosts, var_device_type):
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
                # 'banner_timeout': 20,
                'session_log': 'output_high-level.log'
            }

            try:
                device.update(var_credentials)
                net_connect = ConnectHandler(**device)
                net_connect.enable()
                self.output.append(net_connect)

            except exceptions as error:
                print(error)

    def login(self):
        return self.output


class Device(Login):
    def __init__(self, var_credentials, var_hosts, var_device_type):
        super().__init__(var_credentials, var_hosts, var_device_type)

    def prompt(self):
        net_connect = self.login()

        output = []
        for net in net_connect:
            try:
                display = net.find_prompt()
                output.append(display)
            except exceptions as error:
                print(error)

        return output

    def show(self, var_command):
        net_connect = self.login()

        output = []
        for net in net_connect:
            for command in var_command:
                try:
                    display = net.send_command(command, max_loops=1000, delay_factor=5)
                    output.append(display)
                except exceptions as error:
                    print(error)

            return output

    def config(self, var_command):
        net_connect = self.login()

        output = []
        for net in net_connect:
            try:
                display = net.send_config_set(var_command, max_loops=1000, delay_factor=5)
                output.append(display)
            except exceptions as error:
                print(error)

        return output

    def save(self):
        net_connect = self.login()

        output = []
        for net in net_connect:
            try:
                display = net.save_config()
                output.append(display)
            except exceptions as error:
                print(error)

        return output


cred_iosxe = func_yml('pass.yml', 'cred_iosxe')
host_iosxe = func_yml('pass.yml', 'host_iosxe')

cred_nxos = func_yml('pass.yml', 'cred_nxos')
host_nxos = func_yml('pass.yml', 'host_nxos')

if __name__ == '__main__':
    iosxe = Device(cred_iosxe, host_iosxe, 'cisco_ios')
    print(iosxe.prompt())
    print(iosxe.show(['sh clock', 'sh snmp location']))
    print(iosxe.config(['ip host dns.google 8.8.8.8', 'ip host dns9.quad9.net 9.9.9.9']))
    print(iosxe.save())