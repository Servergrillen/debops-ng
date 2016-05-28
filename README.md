## [![DebOps project](http://debops.org/images/debops-small.png)](http://debops.org) apt_install

<!-- This file was generated by Ansigenome. Do not edit this file directly but
     instead have a look at the files in the ./meta/ directory. -->

[![Travis CI](http://img.shields.io/travis/debops/ansible-apt_install.svg?style=flat)](http://travis-ci.org/debops/ansible-apt_install)
[![test-suite](http://img.shields.io/badge/test--suite-ansible--apt__install-blue.svg?style=flat)](https://github.com/debops/test-suite/tree/master/ansible-apt_install/)
[![Ansible Galaxy](http://img.shields.io/badge/galaxy-debops.apt_install-660198.svg?style=flat)](https://galaxy.ansible.com/debops/apt_install)


The `debops.apt_install` Ansible role is meant to be used as an easy way to
install APT packages on hosts that don't require more extensive
configuration which would require a more extensive, custom Ansible role.
The role itself exposes several Ansible default variables which can be used
to specify custom lists of packages on different levels of Ansible
inventory (global, per-group or per-host).

### Installation

This role requires at least Ansible `v2.0.0`. To install it, run:

```Shell
ansible-galaxy install debops.apt_install
```

### Documentation

More information about `debops.apt_install` can be found in the
[official debops.apt_install documentation](http://docs.debops.org/en/latest/ansible/roles/ansible-apt_install/docs/).



### Are you using this as a standalone role without DebOps?

You may need to include missing roles from the [DebOps common
playbook](https://github.com/debops/debops-playbooks/blob/master/playbooks/common.yml)
into your playbook.

[Try DebOps now](https://github.com/debops/debops) for a complete solution to run your Debian-based infrastructure.





### Authors and license

`apt_install` role was written by:

- Maciej Delmanowski | [e-mail](mailto:drybjed@gmail.com) | [Twitter](https://twitter.com/drybjed) | [GitHub](https://github.com/drybjed)
- [Robin Schneider](http://ypid.de/) | [e-mail](mailto:ypid@riseup.net) | [Twitter](https://twitter.com/ypid) | [GitHub](https://github.com/ypid)

License: [GPLv3](https://tldrlegal.com/license/gnu-general-public-license-v3-%28gpl-3%29)

***

This role is part of the [DebOps](http://debops.org/) project. README generated by [ansigenome](https://github.com/nickjj/ansigenome/).
