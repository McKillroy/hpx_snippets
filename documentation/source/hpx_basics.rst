
Section 4 : HPX Basics
==========================

.. contents::

Introduction to HPX
-------------------------

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


How does it work?
--------------------

HPX provides a runtime environment to allow running your programs in parallel - be it locally on the cores of your desktop computer or on a datacenter with potentially thousands of remote machines, processors and cores.

To achieve that, HPX provides a set of technologies you can use to parallelize your program with as little overhead as possible. And since with parallelization comes concurrency, HPX also provides a model to manage concurrency in your application. And with distributed applications comes networking, so HPX provides that too.

The purpose of following sections is, to provide you with an introduction to the various techniques used in HPX enabled applications to achieve the goals of parallelization, concurrency management and transport in a distributed environment.

When an HPX application or cluster is starting (Description of the bootstrap process) ...

Once the application or the cluster of nodes with your aplication is up an running and the nodes are connected it is ready to run the workload.

HPX is strongly oriented to be compliant with existing and upcoming C++ standards like parallel algorithms, threading, concurrency TS and others.

--------------------
Parallelization
--------------------

* Parallelization in HPX is achieved by submitting tasks to the HPX runtime. 

.. code-block:: cpp
   :caption: Async task example

    // prepare data
    std::string the_question = "What is the meaning of life, the universe and everything?";
    // submit task to HPX - returns immediately, while the task is running in the background
    auto future_result = hpx::async( // param 1: The callable - here a lambda
        [](std::string question) { troll_user_for_10e6_years(question); return "The answer is 42."; },
        hpx::find_here(),            // param 2: locality - here the local machine
        the_question                 // param(s): callable arg(s) - here a single string
    );
    future_result.wait();                                 // this will block until the future is ready.
    std::string finally_the_answer = future_result.get(); // ready, because we waited for it
    hpx::cout << finally_the_answer << hpx::endl;
    

* This can be done synchronously ( = "blocking" - you wait for the task to finish) or asynchronously (the call returns immediately and you receive a future to the results which you can use, once they are available) like in the "Async task example" above.

* A task can be a conventional callable, like a function, a functor or a lambda (for local execution) or a so called action, which is a serializable representation of a callable that can be sent over the transport to be run on a remote node (a so-called "locality"). 

    * Submitting the task returns a future you can pass around, wait for or dump.
    * The example above can run only locally, because the callable is a lambda and not an action. More on actions, and how they are created from callables :doc:`macros_for_components_and_actions`.

A task is a small unit of work. You do not always have to create your tasks manually. E.g. when using parallel algorithms or parallel for loops, HPX is chopping the bigger task for you into pieces which are then separately submitted to the runtime and which return a combined future, which is ready, when all the sub-tasks are completed.

---------------
Concurrency
---------------

The main construct to manage concurrency in HPX is the future. "Futurize everything" is a proverb used within the HPX community to describe that. Using futures does not protect you from all potential concurrency issues, but it allows you to manage them.

---------------
Distribution
---------------

Running your application as a parallelized AND distributed app is not much different than running it locally on a pool of HPX worker threads. The only difference is, that your threads now run locally AND remotely on the nodes of your cluster. Therefore, when submitting your task, you also need to provide the so called localities your application is allowed to run on.

* Where are the tasks created? 
* How is the distribution of tasks coordinated?
* What about distributed containers?



