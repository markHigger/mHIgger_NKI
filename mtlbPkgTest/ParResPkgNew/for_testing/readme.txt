ParResPkgNew C Shared Library

1. Prerequisites for Deployment 

Verify that version 9.3 (R2017b) of the MATLAB Runtime is installed.   

If the MATLAB Runtime is not installed, you can run the MATLAB Runtime installer.
To find its location, enter
  
    >>mcrinstaller
      
at the MATLAB prompt.

Alternatively, download and install the Macintosh version of the MATLAB Runtime for R2017b 
from the following link on the MathWorks website:

    http://www.mathworks.com/products/compiler/mcr/index.html
   
For more information about the MATLAB Runtime and the MATLAB Runtime installer, see 
Package and Distribute in the MATLAB Compiler SDK documentation  
in the MathWorks Documentation Center.    

NOTE: You will need administrator rights to run the MATLAB Runtime installer. 


2. Files to Deploy and Package

Files to Package for Shared Libraries
=====================================
-ParResPkgNew.dylib
-ParResPkgNew.h
-MCRInstaller.zip 
    Note: if end users are unable to download the MATLAB Runtime using the
    instructions in the previous section, include it when building your 
    component by clicking the "Runtime downloaded from web" link in the
    Deployment Tool.
-This readme file

3. Definitions

For information on deployment terminology, go to
http://www.mathworks.com/help and select MATLAB Compiler >
Getting Started > About Application Deployment >
Deployment Product Terms in the MathWorks Documentation
Center.

4. Appendix 

A. Mac systems:
In the following directions, replace MR by the directory where MATLAB or the MATLAB 
   Runtime is installed on the target machine.

If the environment variable DYLD_LIBRARY_PATH is undefined, set it to the following 
   string:

MR/v93/runtime/maci64:MR/v93/sys/os/maci64:MR/v93/bin/maci64

If it is defined, set it to the following:

${DYLD_LIBRARY_PATH}:MR/v93/runtime/maci64:MR/v93/sys/os/maci64:MR/v93/bin/maci64

    For more detailed information about setting the MATLAB Runtime paths, see Package and 
   Distribute in the MATLAB Compiler SDK documentation in the MathWorks Documentation 
   Center.


     
        NOTE: To make these changes persistent after logout on Linux 
              or Mac machines, modify the .cshrc file to include this  
              setenv command.
        NOTE: The environment variable syntax utilizes forward 
              slashes (/), delimited by colons (:).  



