![](https://github.com/ananasness/iu-devops-labs/blob/master/screenshots/lab6/1.png?raw=true)
![](https://github.com/ananasness/iu-devops-labs/blob/master/screenshots/lab6/2.png?raw=true)

```bash
iu-devops-labs git:(master) ✗ ansible-playbook ansible/playbooks/docker.yml --become --become-user root

PLAY [all] *****************************************************************************************************************************************************************

TASK [Gathering Facts] ****************************************************************************************************************************************************
The authenticity of host '51.250.93.171 (51.250.93.171)' can't be established.
ECDSA key fingerprint is SHA256:dRM0Ksff1LcMRLeRCiuqTivWkC8jKNGrRENmcvNP668.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Enter passphrase for key '/Users/ananas/.ssh/id_rsa': 
ok: [51.250.93.171]

TASK [geerlingguy.docker : include_tasks] **********************************************************************************************************************************
skipping: [51.250.93.171]

TASK [geerlingguy.docker : include_tasks] **********************************************************************************************************************************
included: /Users/ananas/.ansible/roles/geerlingguy.docker/tasks/setup-Debian.yml for 51.250.93.171

TASK [geerlingguy.docker : Ensure old versions of Docker are not installed.] ***********************************************************************************************
ok: [51.250.93.171]

TASK [geerlingguy.docker : Ensure dependencies are installed.] *************************************************************************************************************
ok: [51.250.93.171]

TASK [geerlingguy.docker : Ensure additional dependencies are installed (on Ubuntu < 20.04 and any other systems).] ********************************************************
skipping: [51.250.93.171]

TASK [geerlingguy.docker : Ensure additional dependencies are installed (on Ubuntu >= 20.04).] *****************************************************************************
ok: [51.250.93.171]

TASK [geerlingguy.docker : Add Docker apt key.] ****************************************************************************************************************************
changed: [51.250.93.171]

TASK [geerlingguy.docker : Ensure curl is present (on older systems without SNI).] *****************************************************************************************
skipping: [51.250.93.171]

TASK [geerlingguy.docker : Add Docker apt key (alternative for older systems without SNI).] ********************************************************************************
skipping: [51.250.93.171]

TASK [geerlingguy.docker : Add Docker repository.] *************************************************************************************************************************
changed: [51.250.93.171]

TASK [geerlingguy.docker : Install Docker.] ********************************************************************************************************************************
skipping: [51.250.93.171]

TASK [geerlingguy.docker : Install Docker (with downgrade option).] ********************************************************************************************************
changed: [51.250.93.171]

TASK [geerlingguy.docker : Ensure /etc/docker/ directory exists.] **********************************************************************************************************
skipping: [51.250.93.171]

TASK [geerlingguy.docker : Configure Docker daemon options.] ***************************************************************************************************************
skipping: [51.250.93.171]

TASK [geerlingguy.docker : Ensure Docker is started and enabled at boot.] **************************************************************************************************
ok: [51.250.93.171]

TASK [geerlingguy.docker : Ensure handlers are notified now to avoid firewall conflicts.] **********************************************************************************

RUNNING HANDLER [geerlingguy.docker : restart docker] **********************************************************************************************************************
changed: [51.250.93.171]

TASK [geerlingguy.docker : include_tasks] **********************************************************************************************************************************
included: /Users/ananas/.ansible/roles/geerlingguy.docker/tasks/docker-compose.yml for 51.250.93.171

TASK [geerlingguy.docker : Check current docker-compose version.] **********************************************************************************************************
ok: [51.250.93.171]

TASK [geerlingguy.docker : set_fact] ***************************************************************************************************************************************
ok: [51.250.93.171]

TASK [geerlingguy.docker : Delete existing docker-compose version if it's different.] **************************************************************************************
ok: [51.250.93.171]

TASK [geerlingguy.docker : Install Docker Compose (if configured).] ********************************************************************************************************
changed: [51.250.93.171]

TASK [geerlingguy.docker : include_tasks] **********************************************************************************************************************************
skipping: [51.250.93.171]

TASK [../roles/deploy_app : Pull image] ************************************************************************************************************************************
changed: [51.250.93.171]

TASK [../roles/deploy_app : Run container] *********************************************************************************************************************************
changed: [51.250.93.171]

PLAY RECAP *****************************************************************************************************************************************************************
51.250.93.171              : ok=17   changed=7    unreachable=0    failed=0    skipped=8    rescued=0    ignored=0   
```