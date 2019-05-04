# Ansible Role: christiangda.epel_repo

[![Build Status](https://travis-ci.org/christiangda/ansible-role-epel-repo.svg?branch=master)](https://travis-ci.org/christiangda/ansible-role-epel-repo)
[![Ansible Role](https://img.shields.io/ansible/role/33302.svg)](https://galaxy.ansible.com/christiangda/epel_repo)

This role [install EPEL Repository](https://fedoraproject.org/wiki/EPEL)

## Requirements

This role work on RedHat, CentOS and Amazon Linux distributions

* RedHat
  * 6
  * 7
* CentOS
  * 6
  * 7
* Amazon Linux
  * 1
  * 2

## Role Variables

None.

## Dependencies

None.

## Example Playbook

**for RedHat/CentOS 6/7**

```yaml
- hosts: servers
    gather_facts: True
    roles:
        - christiangda.epel_repo
```

**for Amazon Linux 1/2 (my-playbook.yml)**

```yaml
- hosts: all
    gather_facts: True
    become: true
    become_user: root
    become_method: sudo
    remote_user: ec2-user
    roles:
        - christiangda.epel_repo
```

**Inventory file sample (inventory)**

```ini
[all]
10.14.x.y
10.14.v.z

[amazon-1]
10.14.x.y

[amazon-2]
10.14.v.z
```

**How to used it**

```bash
ansible-playbook my-playbook.yml \
    --inventory inventory \
    --private-key [~/location of my key.pem] \
    --become \
    --become-user=ec2-user \
    --user ec2-user
```

## Development / Contributing

This role is tested using [Molecule](https://molecule.readthedocs.io/en/latest/) and was developed using
[Python Virtual Environments](https://docs.python.org/3/tutorial/venv.html)

**Prepare your environment**

```bash
mkdir ansible-roles
cd ansible-roles/

python3 -m venv venv
source venv/bin/activate
pip install pip --upgrade
pip install pytest
pip install pytest-mock
pip install pylint
pip install rope
pip install autopep8
pip install yamllint
pip install molecule
pip install ansible
pip install docker-py
```

**Clone the role repository and create symbolic link**

```bash
git clone https://github.com/christiangda/ansible-role-epel-repo.git
ln -s ansible-role-epel_repo christiangda.epel-repo
cd ansible-role-epel-repo
```

**Execute the test**

```bash
molecule test
```

**Additionally if you want to test using VMs, I have a very nice [ansible-playground project](https://github.com/christiangda/ansible-playground) that use Vagrant and VirtualBox, try it!.**


## License

This module is released under the GNU General Public License Version 3:

* [http://www.gnu.org/licenses/gpl-3.0-standalone.html](http://www.gnu.org/licenses/gpl-3.0-standalone.html)

## Author Information

* [Christian González Di Antonio](https://github.com/christiangda)
