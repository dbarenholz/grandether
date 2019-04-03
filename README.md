# Welcome
Welcome to the github repository of Grand Ether for the course 2IC80. In this repo one can find all used configuration files and setup information necessary to perform the Kaminsky attack, as explained in the PDF.

## Attacker
The Attacker folder contains all files related to the attacker. First off, there are the corefile and the zone file (`attacker.db`). These are used for the configuration of coredns. Secondly, it contains the python scripts used for the kaminsky attack. The `Kaminsky.py` script's function is to poison the DNS cache by outspeeding the top level domain server. The `KaminskyAdvanced.py` attack performs the attack where the domain name is already in cache and these records are then overwritten by the attacker's data. 

## Authoritative
This folder contains all files necessary for configuring the Authoritative name sever using coredns.

## Recursive
This folder contains all files necessary for configuring the Recursive name sever using unbound.

## TLD NS
This folder contains all files necessary for configuring the top leve domain name sever using coredns.
