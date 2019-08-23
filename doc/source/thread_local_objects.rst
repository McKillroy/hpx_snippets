Thread Local Storage and Function Local  Statics
====================================================

* Have a persistent thread local object in every worker thread which can be found by running tasks (e.g. a LuaState).

Concepts to understand: 
    * Thread Local Storage
    * Function Local Static Variables


.. code-block:: cpp
   :caption: Thread Local Storage  ( C++ ) "LuaEngine"
   :name: thread_local_storage

   class lua_engine {
     lua_engine()
     {
       // ... initialize your LUA engine here
     }
   };

   // retrieve reference to the thread local static lua_engine
   lua_engine& thread_local_lua_engine() {
     // function local static - acts like a singleton
     static thread_local lua_engine engine; 
     return engine;
   }


| **Caveat:** Always get this reference anew after a yield(), a future.get() or any other hpx::thread suspending operation.
|   *Note:*
|   --> get the reference EVERY time when starting a lua function.        
|   --> make a wrapper for lua calls.
   
