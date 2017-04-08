# scs_osio
OpenSensors.io - device, organisation, topic and schema management tools for South Coast Science  air quality
monitoring projects.

Required libraries: 

* Third party: -
* SCS root: scs_core
* SCS host: scs_host_bbe, scs_host_posix or scs_host_rpi


Typical PYTHONPATH (Raspberry Pi, in .profile):

export PYTHONPATH=$HOME/SCS/scs_analysis:$HOME/SCS/scs_dev:$HOME/SCS/scs_osio:$HOME/SCS/scs_mfr:$HOME/SCS/scs_dfe_eng:$HOME/SCS/scs_host_rpi:$HOME/SCS/scs_core:$PYTHONPATH


Typical PYTHONPATH (Beaglebone, in .bashrc):

export PYTHONPATH=/home/debian/SCS/scs_dev:/home/debian/SCS/scs_osio:/home/debian/SCS/scs_mfr:/home/debian/SCS/scs_psu:/home/debian/SCS/scs_comms_ge910:/home/debian/SCS/scs_dfe_eng:/home/debian/SCS/scs_host_bbe:/home/debian/SCS/scs_core:$PYTHONPATH
