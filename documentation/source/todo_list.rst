Work Doc : Current ToDo List
===============================

.. contents::

Open Questions
----------------

Threads
    * How can I get the Ids of all HPX worker threads?
    * How can I run code on a specific worker thread?

* Can I run local non-action functions directly with hpx?

* launch policies: How do I start an async action and force HPX to immediately start executing ( real time priority? )

What exactly do the Macros do? what is the underlying mechanic?
    | See also :doc:`macros_for_components_and_actions` and 
    | :doc:`hpx_macrodoc_for_doxygen`



 
* Which of HPX includes do I need when?
    One include to rule them all: ``<hpx/hpx.hpp>`` - how to narrow scope?


* Recommended build methods and examples.

    * VS, VSCODE, CMake, vcpkg, ...
    * HPX CMake commands explained: add_hpx_executable, add_hpx_library - These are almost entirely undocumented.


## Fades out - wait for changes
add_hpx_executable
add_hpx_component ## fragl auch f. actions
hpx_setup_target: Use this.


* iterate over threads for initialization:

.. code-block:: text


   [06:25:39] <Yorlik> NVM - found it: hpx::async<agns::game::Controller::start_action>(hpx::launch::sync, gcId);
   [06:29:29] <Yorlik> Argh - crap thats wrong ... fork maybe? 
   [07:59:14] <jbjnr_> Yorlik: fork will suspend the current task and immediately switch to the new one - but this would only work for a local action. If you wanted to do it remotely, you need to look at direct_Action
   [08:03:57] <Yorlik> How would I start a task immediately but async - is there a way to control that ?
   [08:07:11] <jbjnr_> fork policy should work, (I tend to use a high priority task and am prepared to wait)
   [08:08:22] <Yorlik> But you said fork suspends the current task. i want it to be non blocking but guarentee to start immediately 
   [08:08:30] <Yorlik> Or asap
   [08:09:35] <jbjnr_> "non blocking but guarentee to start immediately" - that's a contradiction unless you spawn a completely new worker thread to launch it on
   [08:09:57] <jbjnr_> can you reserve a core for a special thread pool for these realtime tasks?
   [08:10:12] <jbjnr_> (one at a time), or more threads in the pool if you need multiple
   [08:10:21] <jbjnr_> cores^
   [08:10:33] <Yorlik> I am starting this out of hpx_main and its essentially a task running for the lifetime of the program
   [08:11:01] <jbjnr_> Then the best thing to do would be create aseparate thread pool with 1 core in it and only run that task on that pool
   [08:11:31] <Yorlik> OK. Is there a way to iterate of my worker threads to initialize thread local objects?
   [08:11:32] <jbjnr_> then normal tasks will use the 'default' thread pool and your special task will be in it's own sandbox
   [08:12:29] <Yorlik> Makes sense. My default pool would have a lua engine in each OS thread. I'd like to initialize all of them at start. How could I iterate over them?
   [08:12:38] <jbjnr_> scroll down to the end of here - https://github.com/STEllAR-GROUP/hpx/blob/master/tests/unit/resource/named_pool_executor.cpp does this help you?
   [08:12:41] <Yorlik> And start an init  task on each
   [08:13:02] <jbjnr_> aha. That's slightly different
   [08:13:55] <Yorlik> i just want to call a function at startup on each thread which created the static thread local lua engine
   [08:14:09] <jbjnr_> yup. let me think a moment
   [08:14:17] <jbjnr_> I'm looking for an example to help you
   [08:14:18] <Yorlik> We don't keep state in the lua engines - they just run one off tasks that store data on the C++ side
   [08:14:36] <Yorlik> So we can run any gameobject message handlers on any lua state
   [08:16:41] <jbjnr_> if you are running this from main(), then just loop over the number of threads and async spawn a task for each lua engine/interpreter, if no other taks are running then each core will take one task automagically
   [08:17:11] <Yorlik> That I could do.
   [08:17:22] <Yorlik> I have a separate init function that would just do it
   [08:17:53] <jbjnr_> to be 100% certain that nothing else runs there, create a pool name "lua" or something and allocate N cores to it, then start N lua tasks on that pol. All other taks will go on the "default" pool
   [08:18:13] <jbjnr_> the default pool must have at least one core assigned to it
   [08:18:49] <Yorlik> How would I pin a task to a thread?
   [08:19:01] <jbjnr_> we plan to allow pools to coexist on the same cores (so on 1 4 core machine you could have a 4 core lua pool and a 1 core default pool and 1 core would have to run two worker threads, but we haven't enabled it yet)
   [08:19:36] <jbjnr_> look https://github.com/STEllAR-GROUP/hpx/blob/master/examples/resource_partitioner/simple_resource_partitioner.cpp#L89
   [08:19:36] <Yorlik> That might for example make sense for pipelining scenarios
   [08:19:48] <jbjnr_> step 1, create a lua pol (this example creates an MPI pool)
   [08:20:01] <jbjnr_> step 2, create an executor that is bound to that pools
   [08:20:14] <jbjnr_> step 3, async(executor, task)
   [08:20:26] <jbjnr_> step 1 must be done at startup, steps 2,3 can be done any time
   [08:21:00] <Yorlik> So I can pin to a pool, but not a thread in that pool? Would I need single thread pools then?
   [08:22:18] <jbjnr_> you could create N thread pools each with one core, but if the task never suspends, one it starts runing it will stay on the core it started on, so it is sort of pinned by default.
   [08:22:41] <jbjnr_> we do support launching on a single core within a pool, but there isn't an example and the API is 'in flux'
   [08:22:56] <jbjnr_> so it would be better to use N pools like the first example I showed you
   [08:23:18] <Yorlik> So I cannot iterate over the threads within a pool but just have several single threded pools I could then iterate over?
   [08:23:24] <jbjnr_> (named_pool_executor test)
   [08:23:39] <jbjnr_> yes.
   [08:23:52] <Yorlik> Which would spool any scheduling ifc.
   [08:23:59] <Yorlik> ifc=ofc
   [08:24:07] <Yorlik> err -- spool = spoil
   [08:24:11] <jbjnr_> it is possible to iterate over threads, but the API is a bit broken and you're better off using N pools and iterating over them with an executor for each
   [08:24:25] <Yorlik> But what about my scheduling then?
   [08:24:41] <Yorlik> I still would like to just give a tsk to the pool and not care where its running
   [08:25:01] <Yorlik> I simply want a guaranteed initialization at start. 
   [08:25:18] <jbjnr_> but you said these lua tasks run forever, so no other tasks can run there anyway?
   [08:25:30] <Yorlik> Nono
   [08:25:35] <Yorlik> The lua tasks are short
   [08:25:49] <Yorlik> But the task doing the main event loop runs forever
   [08:26:00] <Yorlik> It does the task construction
   [08:26:14] <jbjnr_> video chat?
   [08:26:16] <Yorlik> Like batching 100 objects for update into a task
   [08:26:20] <Yorlik> Sure
   [08:26:25] <jbjnr_> appear.in?
   [08:26:27] <Yorlik> Ya

-----------------------------------------------------------------------------

action = struct {} - 


Registrierung -  





Check and then Add to Tips
--------------------------------

* It seems when using hpx_add_executable it also takes care of proper installation setup



Caveats, gotchas and quirks
-------------------------------------
    * Confusing function and action names in macro parameters
