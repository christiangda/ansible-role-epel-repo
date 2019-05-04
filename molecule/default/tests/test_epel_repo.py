import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_epel_repo_file(host):
    f = host.file('/etc/yum.repos.d/epel.repo')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_epel_release_is_installed(host):
    pkg = host.package("epel-release")

    assert pkg.is_installed
