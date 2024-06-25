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


    
    def test_component_dns_dns_a_record(self):
        cdir = "batch_03/dns/dns_a_record"
        retcode = cloudicorn.main(["cloudicorn", "apply", cdir, '--force', '--set-var', "run_id={}".format(self.run_id)])
        assert retcode == 0
    
    def test_component_network_subnet(self):
        cdir = "batch_03/network/subnet"
        retcode = cloudicorn.main(["cloudicorn", "apply", cdir, '--force', '--set-var', "run_id={}".format(self.run_id)])
        assert retcode == 0
    
    def test_component_network_network_interface_application_security_group_association(self):
        cdir = "batch_03/network/network_interface_application_security_group_association"
        retcode = cloudicorn.main(["cloudicorn", "apply", cdir, '--force', '--set-var', "run_id={}".format(self.run_id)])
        assert retcode == 0
    
    def test_component_network_network_interface_security_group_association(self):
        cdir = "batch_03/network/network_interface_security_group_association"
        retcode = cloudicorn.main(["cloudicorn", "apply", cdir, '--force', '--set-var', "run_id={}".format(self.run_id)])
        assert retcode == 0
    
    def test_component_network_virtual_network_peering(self):
        cdir = "batch_03/network/virtual_network_peering"
        retcode = cloudicorn.main(["cloudicorn", "apply", cdir, '--force', '--set-var', "run_id={}".format(self.run_id)])
        assert retcode == 0
    
    def test_component_private_dns_private_dns_zone_virtual_network_link(self):
        cdir = "batch_03/private_dns/private_dns_zone_virtual_network_link"
        retcode = cloudicorn.main(["cloudicorn", "apply", cdir, '--force', '--set-var', "run_id={}".format(self.run_id)])
        assert retcode == 0
    
    def test_component_private_dns_private_dns_a_record(self):
        cdir = "batch_03/private_dns/private_dns_a_record"
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
