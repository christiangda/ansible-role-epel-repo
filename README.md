Ansible Role: epel-repo
=========
[![Build Status](https://travis-ci.org/christiangda/ansible-role-epel-repo.svg?branch=master)](https://travis-ci.org/christiangda/ansible-role-epel-repo)

This module [install EPEL Repository](https://fedoraproject.org/wiki/EPEL)

Requirements
------------

This role work on RedHat, CentOS and Amazon Linux distributions

specific version:
* RedHat
  * 6
  * 7
* CentOS
  * 6
  * 7
* Amazon Linux
  * 1
  * 2

Role Variables
--------------

* defaults/main.yml
  * show_debug_messages -->  when true, show some debug messagges in execution
* vars/main.yml
  * epel_package --> package name for distributions
  * epel_repo_file_path --> location of epel repo file in all distribution supported by this role

Dependencies
------------

None.

Example Playbook
----------------

for RedHat/CentOS 6/7

    - hosts: servers
      gather_facts: True
      roles:
         - christiangda.epel-repo

for Amazon Linux 1/2 (my-playbook.yml)

    - hosts: all
      gather_facts: True
      become: true
      become_user: root
      become_method: sudo
      remote_user: ec2-user
      roles:
        - christiangda.epel-repo

Inventory file sample (inventory)

    [all]
    10.14.x.y
    10.14.v.z

    [amazon-1]
    10.14.x.y

    [amazon-2]
    10.14.v.z

How to used it

    ansible-playbook my-playbook.yml \
      --inventory inventory \
      --private-key [~/location of my key.pem] \
      --become \
      --become-user=ec2-user \
      --user ec2-user
      [--extra-vars "show_debug_messages=True"] --> additional


License
-------

This module is released under the GNU General Public License Version 3:

* [http://www.gnu.org/licenses/gpl-3.0-standalone.html](http://www.gnu.org/licenses/gpl-3.0-standalone.html)

Author Information
------------------

* [Christian González](https://github.com/christiangda)
