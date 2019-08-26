
Section 4 : HPX Basics
==========================

HPX is a standards conformant runtime written in C++ which can help you to parallelize your application with minimal overhead.

It specifically targets the problems of 

Starvation
    occurs when there is insufficient concurrent work available to maintain high utilization of all resources.

Latencies
    are imposed by the time-distance delay intrinsic to accessing remote resources and services.

Overhead
    is work required for the management of parallel actions and resources on the critical execution path which is not necessary in a sequential variant.

Waiting
    for contention resolution is the delay due to the lack of availability of oversubscribed shared resources.

The Definitions above are copied from the HPX Documentation: `What makes our systems slow? <https://stellar-group.github.io/hpx/docs/sphinx/branches/master/singlehtml/index.html#what-makes-our-systems-slow>`_

HPX is an implementation of the **ParalleX** model of execution: 

ParalleX
    Citation and .pdf download Links: `ParalleX: A Study of A New Parallel Computation Model <https://www.researchgate.net/publication/220953286_ParalleX_A_Study_of_A_New_Parallel_Computation_Model>`_
    


What can HPX do for you?
-------------------------------

* Help parallelizing your application and increasing CPU and node Utilization with a 
* Standards conformant interface
* Load Balancing
* Glueing together your distributed cluster

What can HPX NOT do for you
------------------------------
* Automagically parallelize your code and make a badly written application fast.
* Remove all danger of race conditions


   
