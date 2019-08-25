Static Thread Local Objects: e.g. Lua States 
=============================================

How to have a persistent thread local object in every worker thread which can be found by running tasks (e.g. a LuaState).

If you have objects you want to use frequently from several HPX tasks, like a scripting engine, you might want to create these objects only once and then use them from any task runing on that thread.

This could be done by leveraging the following

C++ concepts: 
    * Function Local Static Variables: Create once and use for the entire runtime of the application
    * Thread Local Storage: Have that object only available in a specific OS worker thread to tame possible concurrency issues.
    * Combine the above and win!


.. code-block:: cpp
   :caption: Static Thread Local Storage  ( C++ ) "LuaEngine"
   :name: static_thread_local_storage

   // boilerplate, includes, etc ...

   struct lua_engine {
     lua_engine()
     {
       // ... initialize your LUA engine here
     }
     someReturnValueType run_lua_code (std::string & luaCode){
      // ... implementation
     }
   };

   // retrieve a reference to the thread local static lua_engine
   lua_engine& thread_local_lua_engine() {
     // function local static - initialized only once per OS thread
     static thread_local lua_engine engine; 
     return engine;
   }

   // Wrapper function to never have an invalid lua_engine reference 
   // when calling into it and running Lua code
   someReturnValueType run_luacode(std::string & luaCode){
      return thread_local_lua_engine().run_lua_code(luaCode);
   }

   int main(){
    auto result = run_luacode( "print('Hello, World!')" );
    return 0;
   }


Caveat
  Always get the object reference anew after a yield(), a future.get() or any other hpx::thread suspending operation.
| *Note:*
| --> make a wrapper for lua calls to be safe. It's low overhead.
| *Solution:* See wrapper function ``run_luacode`` above.

Explanation
  | If an HPX async gets suspended, it is not guaranteed, it will be resumed on the same OS worker thread. The retrieved reference to the LuaState/-Engine could (but doesn't have to) be invalid if the task is resumed. Therefore you could not naively use any LuaState local data and believe it persists between calls, because the calls might be done in different OS threads and go to different LuaStates specific to the respective OS thread. So you have two problems to solve: 
  |  1. Always make sure you have a valid reference 
  |  2. Never assume persistence of local data on that object, here a LuaState / LuaEngine.
   
