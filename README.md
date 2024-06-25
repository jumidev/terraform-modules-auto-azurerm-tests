# test suite for https://github.com/jumidev/terraform-modules-auto-azurerm

This test suite works by creating a set of real resources in azure to test that the underlying terraform components work.  Components are organized into batches.  Each batch creates the prerequisites for subsequent batches, and so on.

All resources in this test are free, their existance **should not** incur fees.  If they do, please open an issue.

# System requirements

- make
- python3 with virtualenv
- terraform or opentofu


## setup Azure credentials

Follow this guide to create a service principal on azure https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/guides/azure_cli

Make note of the AZURE_CLIENT_ID, AZURE_CLIENT_SECRET, AZURE_TENANT_ID, AZURE_SUBSCRIPTION_ID, set these as environment variables.  You can use tools like `direnv` to automatically set the env vars when you enter this directory

```
export AZURE_CLIENT_ID="xxxxxx-ffff-4444-9999-aaaaaaaaaa"
export AZURE_CLIENT_SECRET="xxxxxx-ffff-4444-9999-aaaaaaaaaa"
export AZURE_TENANT_ID="xxxxxx-ffff-4444-9999-aaaaaaaaaa"
export AZURE_SUBSCRIPTION_ID="xxxxxx-ffff-4444-9999-aaaaaaaaaa"
```

## setup Azure Storage

These test use an Azure storage account and container to store their remote states.  Go into the azure portal and create a storage account and container.  Make sure that the service principal above has rights to read and write to this storage account.

Add the account name and container name to the environment variables, e.g:

```
export TEST_AZURE_STORAGE_ACCOUNT=testcloudicorn
export TEST_AZURE_STORAGE_CONTAINER=test
```

## Setup virtual env

The included makefile has a task to automatically create a virtual env and populate with necessary requirements (including the latest release of cloudicorn-cli)

`make venv`

You can also install requirements outside of a virtual env:

`pip3 install --user -r requirements.txt`

### Cloudicorn-cli

If you do not want to use the pypi release of cloudicorn-cli, want to use the Either install from pip or clone the git repo and install.

## make sure terraform / opentofu is installed

`cloudcorn_setup --terraform`



# Running tests

Included Makefile has two tasks to run tests:

`make test_venv` # runs tests using the virtual env

`make test`  # doesn't use the venv

Tests create a resource group with a random name (e.g. test_a3f4f654).  To avoid cluttering your azure subscription, this resource group is automatically deleted (along with all sub resources) after every test run.

Terraform states are NOT deleted, they will persist in the specified azure container.