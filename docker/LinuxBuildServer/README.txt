This README file is for the linux build server image requirements 
to be setup as a Jenkins agent if required.

Set it up as a local image that can be deployed to a server. And once build is ready
It should be possible to copy it back to the file server.

Requirements
1. RHEL 10
2. GCC,
C++
CMake
Ant 
Maven
Python 3
OpenJDK21
jenkins client

Install all build tools like ANt CMake, Maven, OpenJDK and Jenkins Client 
in a seperate directory structure as follows.

/buildtools
Ant, Maven, CMake
/Jenkins
OpenJDK, Jenkins client
Create a python virtual environment withing jenkins directory and add 
following packages to the virtual environment
click, numpy, matplotlib, pg8000, psychopg

Make sure jenkins client is configured to connect with jenkins server.