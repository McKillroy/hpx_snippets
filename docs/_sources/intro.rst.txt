
Section 2 : Introduction to the Problem
=======================================

.. contents::

Part I : Moore's Law and "The Free Lunch is Over" problem
--------------------------------------------------------------

Read this article by Herb Sutter, originally published in Dr.Dobbs Journal: 

`The Free Lunch Is Over: A Fundamental Turn Toward Concurrency in Software <http://www.gotw.ca/publications/concurrency-ddj.htm>`_

He made a follow-up: `Welcome to the jungle <https://herbsutter.com/welcome-to-the-jungle/>`_


Part II : Some thoughts on Concurrency, Parallelism and Distributed Computing
--------------------------------------------------------------------------------


-----------------
A. Concurrency
-----------------

  Concurrency happens, when several agents (read: threads of execution) have access to the same data at the same time, and at least one of them is writing to the data.

Note
  "At the same time" means within a time frame, where at least one of the agents treats the data as if it was "owner" of it, means had "exclusive access". E.g. a thread reading data two times and adding it up to double a value would receive a false result if there was a change between the two reads because of a second party writing to the data.

Corollary
  Concurrency is tightly connected to a clients expectation about the data.

Race Conditions
  From `Wikipedia <https://en.wikipedia.org/wiki/Race_condition>`_: *"A race condition or race hazard is the condition of an electronics, software, or other system where the system's substantive behavior is dependent on the sequence or timing of other uncontrollable events. It becomes a bug when one or more of the possible behaviors is undesirable."* 

---------------
B. Parallelism
---------------

  Parallelism is NOT concurrency! E.g. if there is read-only access to data, no concurrecy is happening but there might be parallel reads. This implies that immutable state can help avoiding concurrency problems where applicable.

--------------------------
C. Distributed Computing
--------------------------
Essentially distributed computing is parallel computing with some bonus problems:

* Increased crosstalk cost (network latency)
* Net Reliability and Congestion Issues
* Node Failure 
* Additional security issues

