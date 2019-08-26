Section 3 : Scalability, Amdahls Law and the USL
=======================================


Scalability
---------------
There are two basic types of scaling: "scaling in" and "scaling out"

Scaling "in"
    Just buy a faster Processor, faster momory, faster hardddisks -> "Make my threads faster."

Scaling "out"
    Get more processors, cores or machines -> "Give me more threads."


Amdahls Law
------------------
`Amdahls Law <https://en.wikipedia.org/wiki/Amdahl%27s_law>`_ formulates the theoretical upper limit for application speedup when scaling out by throwing more cores or computing nodes at a problem. 


The Universal Scalability Law "USL"
--------------------------------------
The `Universal Scalability Law <http://www.perfdynamics.com/Manifesto/USLscalability.html>`_ is even more brutal and an extension to Amdahls Law, because it describes how your parallelized application might even become slower when throwing more machines or cores at a given problem because of the quadratically increasing crosstalk penalty.


Consequences of the USL for writing your application
--------------------------------------------------------
If you want your application to leverage as much computing power as possible, you have to design it to scale out well. Consequences out of the USL are, that for this you must parallelize as much of your application as possible and minimize crosstalk between threads of execution. Especially for massively scaling applications (datacenter / supercomputer grade) crosstalk becomes a big problem, because it's impact grows quadratically with the number of threads/cores/machines.


