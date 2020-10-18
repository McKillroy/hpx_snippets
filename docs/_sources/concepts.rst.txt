
Section 5: Concepts needed to understand and leverage HPX
=====================================================================


===============================
General Programming Concepts
===============================

* `Typesafety <https://en.wikipedia.org/wiki/Type_safety>`_
* `Serialization <https://en.wikipedia.org/wiki/Serialization>`_
* `RPC <https://en.wikipedia.org/wiki/Remote_procedure_call>`_ 
* Operating System Threads and `Userspace Threads <https://en.wikipedia.org/wiki/Green_threads>`_ (a.k.a. "Green Threads", "Fibers" etc.). Not to be confused with "Tasks" (Small units of work), "Coroutines" (Yield-and-Resumable Subroutines) or "Strands" (Sequentially ordered units of execution).
* `Concurrency and Parallelism <https://en.wikipedia.org/wiki/Concurrency_(computer_science)>`_ 


=================
C++ Concepts   
=================

* `Declaration <https://en.cppreference.com/w/cpp/language/declarations>`_ versus `Definition <https://en.cppreference.com/w/cpp/language/definition>`_. See also `here <https://www.cprogramming.com/declare_vs_define.html>`_ for a newbie friendly explanation of the difference.
* C++ Template language basics
* `CRTP <https://en.wikipedia.org/wiki/Curiously_recurring_template_pattern>`_
* Function Local Static Variables combined with  Thread Local Storage
* Building and using dynamic libraries on your system(s)


===============
HPX Concepts
===============

* `How does it work? <hpx_basics.html#how-does-it-work>`_
* HPX Actions
* HPX Components, "Server" and "Client" Components
* HPX Serialization Implementation
* HPX Migration, Parcel
* HPX Macros
* AGAS
* Executor
* Launch Policy


