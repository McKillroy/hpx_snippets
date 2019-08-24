
Section 1 : Introduction to the Problem
=======================================

Part I : About this Document and the associated Git Repository
-----------------------------------------------------------

This is a draft  / work document I am using, while I am trying to get my head around HPX and build an HPX based distributed application.

The purpose of this document is twofold: It helps me learning and it is a collection of acquired knowledge and recipes which might find their way back into the HPX documentation if people find them useful.


Repository for this Documentation
  `HPX Snippets <https://github.com/McKillroy/hpx_snippets>`_ 


HPX by Ste||ar Group
  `Ste||ar Group HPX Homepage <http://stellar-group.org/libraries/hpx/>`_
  
  `HPX Master Documentation <https://stellar-group.github.io/hpx/docs/sphinx/branches/master/singlehtml/index.html>`_    
  
  `HPX Git Repository <https://github.com/STEllAR-GROUP/hpx>`_


Disclaimer
  These are not academic views, but my thoughts as I am developing an application based on HPX. I'm not a computer scientist, but a self taught hobbyist. So - even if you might find something useful here - read it with a grain of salt. I am always happy for constructive input. Use the issues of the GitHub repository to post your comments and suggestions.


Special thanks
  to Hartmut Kaiser, Thomas Heller and the Ste||ar group IRC channel for enduring me pestering people with unrelated C++ newbie questions, bloopers, false bug reports and other nonsense while I'm working on my project. Most of the writeups here is directly extracted from what I learned there and in private chats. Errors are solely my responsibility.


Copyright and License
  I am using the Boost License for this repository, the same license being used by the Ste||ar group for HPX. Please keep in mind that the text contains quotations from the HPX documentation and code snippets from the HPX source tree. I am trying as good as possible to make it clear when doing so, but it might happen I missed proper referencing on occasion. This is considered a bug and please tell me when you see it.




Part II : Moore's Law and "The Free Lunch is Over" problem
-----------------------------------------------------------

Read this article by Herb Sutter in Dr.Dobbs Journal: 

`The Free Lunch Is Over: A Fundamental Turn Toward Concurrency in Software <http://www.gotw.ca/publications/concurrency-ddj.htm>`_


Part III : Some thoughts on Concurrency, Parallelism and Distributed Computing
---------------------------------------------------------------------------

A. Concurrency
-----------------

  Concurrency happens, when several agents (read: threads of execution) have access to the same data at the same time, and at least one of them is writing to the data.

Note
  "At the same time" means within a time frame, where at least one of the agents treats the data as if it was "owner" of it, means had "exclusive access". E.g. a thread reading data two times and adding it up to double a value would receive a false result if there was a change between the two reads because of a second party writing to the data.

Corollary
  Concurrency is tightly connected to a clients expectation about the data.

Race Conditions
  From `Wikipedia <https://en.wikipedia.org/wiki/Race_condition>`_: *"A race condition or race hazard is the condition of an electronics, software, or other system where the system's substantive behavior is dependent on the sequence or timing of other uncontrollable events. It becomes a bug when one or more of the possible behaviors is undesirable."* 

B. Parallelism
---------------

  Parallelism is NOT concurrency! E.g. if there is read-only access to data, no concurrecy is happening but there might be parallel reads. This implies that immutable state can help avoiding concurrency problems where applicable.

C. Distributed Computing
--------------------------
Essentially distributed computing is parallel computing with some bonus problems:

* Increased crosstalk cost (network latency)
* Net Reliability and Congestion Issues
* Node Failure 
* Additional security issues

