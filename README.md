AuroraInterface
======
##A set of Celery tasks to communicate with Aurora Inverter
###Dependencies
*A version of curtronics C program for aurora communication that I have edited to allow for JSON format retrieval.
--*[https://bitbucket.org/keverly/aurorac](My edited version) (required)
--*Credit to Curtis Blank. [http://www.curtronics.com/Solar/AuroraData.html](Original Work)
*[http://www.celeryproject.org/](Celery)
###Setup
Each session must begin with initializing an Inverter with an address and a port.
``` initInverter("2", "/dev/ttyUSB0") ```
###Methods
Once the Inverter has been initialized, we can begin requsting data.
```getAll(address, stringNum = "0")```
###Usage
Typical usage case
```
import tasks

initInverter("2", "/dev/ttyUSB0")
result = getAll.delay("2")
print result.get()
```