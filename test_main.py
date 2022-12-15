from unittest import TestCase
from main import func_yml


class Test(TestCase):
    def test_func_ini(self):
        devnet_iosxe = func_yml('pass.yml', 'devnet_iosxe')
        self.assertTrue(devnet_iosxe) # if it returns a True value
        self.assertIsInstance(devnet_iosxe, dict)  # if it is a dictionary
        # if it contains the following keys: username, password, secret
        [self.assertIn(k, devnet_iosxe) for k in ['username', 'password', 'secret']]
        # self.fail()
