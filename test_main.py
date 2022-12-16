from unittest import TestCase
from main import func_yml, Login

cred_iosxe = func_yml('pass.yml', 'devnet_iosxe')
host_iosxe = [
    # 'sandbox-iosxe-recomm-1.cisco.com',
    'sandbox-iosxe-latest-1.cisco.com',
]

cred_nxos = func_yml('pass.yml', 'devnet_nxos')
host_nxos = ['sandbox-nxos-1.cisco.com']


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

