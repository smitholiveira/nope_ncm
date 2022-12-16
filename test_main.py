from unittest import TestCase
from main import func_yml, Login, Device

cred_iosxe = func_yml('pass.yml', 'cred_iosxe')
host_iosxe = func_yml('pass.yml', 'host_iosxe')

cred_nxos = func_yml('pass.yml', 'cred_nxos')
host_nxos = func_yml('pass.yml', 'host_nxos')


class Test(TestCase):
    def test_func_yml(self):
        self.assertTrue(cred_iosxe)  # if it returns a True value
        self.assertIsInstance(cred_iosxe, dict)  # if it is a dictionary
        # if it contains the following keys: username, password, secret
        [self.assertIn(k, cred_iosxe) for k in ['username', 'password', 'secret']]
        # self.fail()

    def test_login_nxos(self):
        device = Login(cred_nxos, host_nxos, 'cisco_nxos')
        if device:
            self.assertTrue(device.login())
        else:
            self.fail()

    def test_login_iosxe(self):
        device = Login(cred_iosxe, host_iosxe, 'cisco_ios')
        if device:
            self.assertTrue(device.login())
        else:
            self.fail()

    def test_device(self):
        self.device = Device(cred_iosxe, host_iosxe, 'cisco_ios')
        if self.device:
            self.assertTrue(self.device.login())
        else:
            self.fail()
