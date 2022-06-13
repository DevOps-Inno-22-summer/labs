# Ansible
Here we'll be working with GCP. We assume that Ansible is called from Google Cloud Shell.

# Install Ansible
By default Cloud Shell doesn't have ansible installed by it has the latest python and pip. Running `pip install` will correctly install packages for local user.

```
pip install ansible requests google-auth
```

After that we need to make sure that our PATH var has:
`~/.local/bin`.

# References
* Using [ansible wight GCE](https://docs.ansible.com/ansible/latest/scenario_guides/guide_gce.html)