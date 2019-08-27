.. r_free_function_to_plain_action.rst

How to make Plain Actions from Free Functions
===============================================

Use Case Variables: 
  1. Free Function Namespace
      * Inside a namespace
      * In the global namespace
  
  2. Free Function location and linkage
      * In main program source
      * In a separate header/source file pair
      * Inside a static or shared library 
  
  3. Free function return type
      * returning a value 
      * void return value
      * This just influences the way how the action created from it can be invoked.


Case 1 : Free function in the main program source in global namespace 
--------------------------------------------------------------------------------

Example sourcecode in the repository is at ``/src/action_and_component_macros/case_1``

Needed Macros:  
    main.cpp: `HPX_PLAIN_ACTION`_.

This is the most simple case, but also limited. It would not work for a header file because it would create double definitions when included into several source files.

Example:

.. code-block:: cpp

    #include <hpx/hpx.hpp>
    #include <hpx/hpx_main.hpp>

    #include <iostream>

    // Free function in GLOBAL namespace in main program
    int compute_something(int data)
    {
        return data * 42;
    }
    HPX_PLAIN_ACTION(compute_something, compute_something_action);

    int main(int argc, char* argv[])
    {
        std::cout << "Case 1:" << std::endl;

        // template parameter: Action name
        auto m_fut = hpx::async<compute_something_action>(hpx::find_here(), 42);

        std::cout << "Result: " << m_fut.get() << std::endl;

        return 0;
    }

| `HPX_PLAIN_ACTION`_ *defines* a free function AND *registers* it with HPX. 
| It could be called from other localities like this:

.. code-block:: cpp

  //example action invocation
  auto my_future = HPX::async<compute_something_action>(some_locality_id, 371);


Case 2 : Free function in the main program source in custom namespace 
--------------------------------------------------------------------------------

Example sourcecode in the repository is at ``/src/action_and_component_macros/case_2``

Needed Macros:
  main.cpp: `HPX_PLAIN_ACTION`_

This case works almost the same as case 1. You just have to apply the fully qualified function name to the macro instead. The namespace does NOT appear on the action, because it was defined and registered in the global namespace.


**Example:**

.. code-block:: cpp

    //main program
    #include <hpx/hpx.hpp>
    #include <hpx/hpx_main.hpp>
    
    #include <iostream>
    
    // Free function in CUSTOM namespace in main program
    namespace application {
        int compute_something( int data ) {
            return data * 42;
        }
    }; // namespace application
    HPX_PLAIN_ACTION( application::compute_something, compute_something_action );
    
    int main( int argc, char* argv[] ) {
        std::cout << "Case 2:" << std::endl;
    
        // template parameter: Action name (still without namespace qualifier!)
        auto m_fut = hpx::async<compute_something_action>( hpx::find_here( ), 42 );
    
        std::cout << "Result: " << m_fut.get( ) << std::endl;
    
        return 0;
    }

| `HPX_PLAIN_ACTION`_ *defines* a free function AND *registers* it with HPX. 
| It could be called from other localities like this:

.. code-block:: cpp

  //example action invocation
  // template parameter: Action name
  auto my_future = HPX::async<compute_something_action>(some_node_locality_id, 371);




Case 3 : Free function in main program in custom namespace in separate header/source file pair
-------------------------------------------------------------------------------------------------------

Example sourcecode in the repository is at ``/src/action_and_component_macros/case_3``

Needed Macros:  
  | header file: `HPX_DEFINE_PLAIN_ACTION`_, `HPX_REGISTER_ACTION_DECLARATION`_
  | source file: `HPX_REGISTER_ACTION`_

**Explanation:**

  Now it gets slightly more complex. The Action is defined inside the namespace and thus invoking it requires using the namespace qualifier on it. Definition and registration are now split into two macros and the registration is declared in the header file, while the registration itself happens in the source file. This construction allows using the headerfile in multiple sources without generating duplicate symbol errors at link time.

.. code-block:: cpp

  // actions.hpp
  #pragma once

  #include <hpx/hpx.hpp>
  
  namespace test {
  
      // Free function in namespace
      int some_function( );
  
      // Define the action (inside the namespace):
      // Parameters: function name, desired action name
      HPX_DEFINE_PLAIN_ACTION( some_function, some_function_action );
  
  }; // namespace test
  
  // Declare the Registering of the  Action (in global namespace)
  // Parameters: Fully qualified action name, desired action name for serialization
  // Note: When invoking the action we will still need the fully qualified action name!
  HPX_REGISTER_ACTION_DECLARATION( test::some_function_action, some_function_action_serialized );

.. code-block:: cpp

    // actions.cpp
    #include <hpx/hpx.hpp>

    #include "actions.hpp"

    namespace test {

        // Free function in namespace
        int some_function( ) {
            return 42;
        }

    } // namespace test

    // (outside namespace)
    // Parameters: Fully qualified action name, action name for serialization
    HPX_REGISTER_ACTION( test::some_function_action, some_function_action_serialized );


.. code-block:: cpp

    // main.cpp
    #include <hpx/hpx.hpp>
    #include <hpx/hpx_main.hpp>

    #include "actions.hpp"

    #include <iostream>

    int main( ) {

        std::cout << "Case 3:" << std::endl;

        // template parameter: Fully qualified action name
        auto m_fut = hpx::async<test::some_function_action>( hpx::find_here( ) );

        std::cout << "Result: " << m_fut.get( ) << std::endl;

        return 0;
    }





Case 4: Exporting a free function which also lives in a namespace, from a shared library (.dll or .so), and use it as plain  Action
--------------------------------------------------------------------------------------------------------------------------------------

Example sourcecode in the repository is at ``/src/action_and_component_macros/case_4``

Macros needed:
  | Library header: `HPX_COMPONENT_EXPORT`_, `HPX_DEFINE_PLAIN_ACTION`_, `HPX_REGISTER_ACTION_DECLARATION`_
  | Library source file: `HPX_REGISTER_ACTION`_

**Explanation:** 

  If you look closely, then you will easily see, that the only difference to case 3 here is, that you need the **HPX_COMPONENT_EXPORT** macro here to get the shared library symbol export. The rest it pretty much identical.


**Step 1:** Library Header File: Contains Function *declaration* and action *definition* along with the `HPX_COMPONENT_EXPORT`_ macro for symbol export:

    .. code-block:: cpp

       // file: actions.hpp
       #pragma once

       #include <hpx/hpx.hpp>
       
       namespace test {
       
           // Free function in namespace
           HPX_COMPONENT_EXPORT int some_function( );
       
           // Define the action (inside the namespace):
           // Parameters: function name, desired action name
           HPX_DEFINE_PLAIN_ACTION( some_function, some_function_action );
       
       }; // namespace test
       
       // Declare the Registering of the  Action (in global namespace)
       // Parameters: Fully qualified action name, desired action name for serialization
       // Note: When invoking the action we will still need the fully qualified action name!
       HPX_REGISTER_ACTION_DECLARATION( test::some_function_action, some_function_action_serialized );


| **Note:** 
|   `HPX_COMPONENT_EXPORT`_ is necessary, or the function will not be exported and you'll get a missing symbol error at link time.
|   **Caveat:** The name of the `HPX_COMPONENT_EXPORT`_ macro is confusing: It works for *plain actions* as well as for *components* and their *component actions*. It simply expands to __declspec(dllimport).
|   `HPX_DEFINE_PLAIN_ACTION`_ can be inside the namespace or in the global namespace. The function is referenced by its fully qualified name out of the perspective of the macro placement, the action identifier must be a C++ conformant identifier for serialization purposes. (Best stick with numbers, letters, underscores ...). If you decide to put the Macro inside the namespace, you must reference the action in step 2 and 3 with the namespace in front of it like ``app::myFreeFunction_Action``.


**Step 2:** Library source file: *Function implementation* and *action registration*:

    .. code-block:: cpp

       // file: actions.cpp
       #include <hpx/hpx.hpp>

       #include "actions.hpp"
       
       namespace test {
       
           // Free function in namespace
           int some_function( ) {
               return 42;
           }
       
       } // namespace test
       
       // (outside namespace)
       // Parameters: Fully qualified action name, action name for serialization
       HPX_REGISTER_ACTION( test::some_function_action, some_function_action_serialized );


| **Note:**
|   `HPX_REGISTER_ACTION`_ MUST be in the global namespace. It is sufficient to just reference the action name you have chosen in the header here.
|   It is NOT necessary to specify the `HPX_COMPONENT_EXPORT`_ Macro again.


**Step 3:** Library user: *Action invocation* in the executable or whoever uses this library:

    .. code-block:: cpp

       // file: main.cpp
       #include <hpx/hpx.hpp>
       #include <hpx/hpx_main.hpp>
       
       #include "actions.hpp"
       
       #include <iostream>
       
       int main( ) {
       
           std::cout << "Case 3:" << std::endl;
       
           // template parameter: Fully qualified action name
           auto m_fut = hpx::async<test::some_function_action>( hpx::find_here( ) );
       
           std::cout << "Result: " << m_fut.get( ) << std::endl;
       
           return 0;
       }


.. _HPX_COMPONENT_EXPORT: https://stellar-group.github.io/hpx/docs/sphinx/latest/singlehtml/index.html#c.HPX_COMPONENT_EXPORT
.. _HPX_DEFINE_PLAIN_ACTION: https://stellar-group.github.io/hpx/docs/sphinx/latest/singlehtml/index.html#c.HPX_DEFINE_PLAIN_ACTION
.. _HPX_PLAIN_ACTION: https://stellar-group.github.io/hpx/docs/sphinx/latest/singlehtml/index.html#c.HPX_PLAIN_ACTION
.. _HPX_REGISTER_ACTION_DECLARATION: https://stellar-group.github.io/hpx/docs/sphinx/latest/singlehtml/index.html#c.HPX_REGISTER_ACTION_DECLARATION
.. _HPX_REGISTER_ACTION: https://stellar-group.github.io/hpx/docs/sphinx/latest/singlehtml/index.html#c.HPX_REGISTER_ACTION
