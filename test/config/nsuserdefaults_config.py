import sys
import unittest

if sys.platform.startswith('darwin'):
    from nativeconfig.config import NSUserDefaultsConfig
    from test.config import TestConfigMixin


    class MyNSUserDefaultsConfig(NSUserDefaultsConfig):
        pass


    class TestNSUserDefaultsConfig(unittest.TestCase, TestConfigMixin):
        CONFIG_TYPE = MyNSUserDefaultsConfig

        def tearDown(self):
            try:
                c = self.CONFIG_TYPE.get_instance()
                c.reset()
            except OSError:
                pass

            TestConfigMixin.tearDown(self)

        def test_config_is_created_if_not_found(self):
            pass
