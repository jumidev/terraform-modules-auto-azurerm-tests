#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import unittest
from cloudicorn_core import assert_azurerm_sp_creds, AzureUtils
import datetime, cloudicorn

TEST_AZURE_STORAGE_ACCOUNT = os.getenv("TEST_AZURE_STORAGE_ACCOUNT", None)
TEST_AZURE_STORAGE_CONTAINER = os.getenv("TEST_AZURE_STORAGE_CONTAINER", None)
TEST_RUN_ID = os.getenv("TEST_RUN_ID", None)

class TestAzureComponents(unittest.TestCase):

    def setUp(self):
        assert TEST_AZURE_STORAGE_ACCOUNT != None
        assert TEST_AZURE_STORAGE_CONTAINER != None
        self.current_date_slug = datetime.date.today().strftime('%Y-%m-%d')
        self.run_id = TEST_RUN_ID
        self.azure_utils = AzureUtils()
        self.resource_client = self.azure_utils.resource_client
        
    # DELETE POST TEST
    # def tearDown(self):
    #     self.resource_client.resource_groups.begin_delete("test_{}".format(self.run_id))


    
    def test_component_dns_dns_zone(self):
        cdir = "batch_02/dns/dns_zone"
        retcode = cloudicorn.main(["cloudicorn", "apply", cdir, '--force', '--set-var', "run_id={}".format(self.run_id)])
        assert retcode == 0
    
    def test_component_network_network_interface(self):
        cdir = "batch_02/network/network_interface"
        retcode = cloudicorn.main(["cloudicorn", "apply", cdir, '--force', '--set-var', "run_id={}".format(self.run_id)])
        assert retcode == 0
    
    def test_component_network_application_security_group(self):
        cdir = "batch_02/network/application_security_group"
        retcode = cloudicorn.main(["cloudicorn", "apply", cdir, '--force', '--set-var', "run_id={}".format(self.run_id)])
        assert retcode == 0
    
    def test_component_network_virtual_network(self):
        cdir = "batch_02/network/virtual_network"
        retcode = cloudicorn.main(["cloudicorn", "apply", cdir, '--force', '--set-var', "run_id={}".format(self.run_id)])
        assert retcode == 0
    
    def test_component_network_network_security_group(self):
        cdir = "batch_02/network/network_security_group"
        retcode = cloudicorn.main(["cloudicorn", "apply", cdir, '--force', '--set-var', "run_id={}".format(self.run_id)])
        assert retcode == 0
    
    def test_component_network_subnet_service_endpoint_storage_policy(self):
        cdir = "batch_02/network/subnet_service_endpoint_storage_policy"
        retcode = cloudicorn.main(["cloudicorn", "apply", cdir, '--force', '--set-var', "run_id={}".format(self.run_id)])
        assert retcode == 0
    
    def test_component_private_dns_private_dns_zone(self):
        cdir = "batch_02/private_dns/private_dns_zone"
        retcode = cloudicorn.main(["cloudicorn", "apply", cdir, '--force', '--set-var', "run_id={}".format(self.run_id)])
        assert retcode == 0
    
    def test_component_storage_storage_account(self):
        cdir = "batch_02/storage/storage_account"
        retcode = cloudicorn.main(["cloudicorn", "apply", cdir, '--force', '--set-var', "run_id={}".format(self.run_id)])
        assert retcode == 0

    # def test_rg(self):

    #     cdir = "azurerm/resource_group"
    #     retcode = cloudicorn.main(["cloudicorn", "apply", cdir, '--force', '--set-var', "run_id={}".format(self.run_string)])
    #     assert retcode == 0
    #     # second apply, should not change anything
    #     retcode = cloudicorn.main(["cloudicorn", "apply", cdir, '--force', '--set-var', "run_id={}".format(self.run_string)])
    #     assert retcode == 0

if __name__ == '__main__':
    unittest.main()
