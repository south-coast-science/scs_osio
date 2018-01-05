# scs_osio
OpenSensors.io - device, organisation, topic and schema management tools for South Coast Science  air quality
monitoring projects.

**Required libraries:** 

* Third party: paho-mqtt
* SCS root: scs_core
* SCS host: scs_host_bbe, scs_host_bbe_southern, scs_host_posix or scs_host_rpi



**Typical PYTHONPATH:**

**Raspberry Pi, in /home/pi/.bashrc:**

    export PYTHONPATH=$HOME/SCS/scs_analysis/src:$HOME/SCS/scs_dev/src:$HOME/SCS/scs_osio/src:$HOME/SCS/scs_mfr/src:$HOME/SCS/scs_dfe_eng/src:$HOME/SCS/scs_host_rpi/src:$HOME/SCS/scs_core/src:$PYTHONPATH


**BeagleBone, in /root/.bashrc:**

    export PYTHONPATH=/home/debian/SCS/scs_dev/src:/home/debian/SCS/scs_osio/src:/home/debian/SCS/scs_mfr/src:/home/debian/SCS/scs_psu/src:/home/debian/SCS/scs_comms_ge910/src:/home/debian/SCS/scs_dfe_eng/src:/home/debian/SCS/scs_host_bbe/src:/home/debian/SCS/scs_core/src:$PYTHONPATH


**BeagleBone, in /home/debian/.bashrc:**

    export PYTHONPATH=\~/SCS/scs_dev/src:\~/SCS/scs_osio/src:\~/SCS/scs_mfr/src:\~/SCS/scs_psu/src:\~/SCS/scs_comms_ge910/src:\~/SCS/scs_dfe_eng/src:\~/SCS/scs_host_bbe/src:\~/SCS/scs_core/src:$PYTHONPATH
