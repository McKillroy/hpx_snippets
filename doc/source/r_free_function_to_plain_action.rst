.. r_free_function_to_plain_action.rst

Exporting a free function which also lives in a namespace, from a shared library (.dll or .so), and use it as plain  Action
-----------------------------------------------------------------------------------------------------------------------------------

**Step 1:** Function Declaration in the shared library header:

    .. code-block:: cpp

       namespace app {
           HPX_COMPONENT_EXPORT void myFreeFunction();
       }
       HPX_DEFINE_PLAIN_ACTION ( app::myFreeFunction, myFreeFunction_Action );

| Note: 
|   ``HPX_COMPONENT_EXPORT`` is necessary, or the function will not be exported and you'll get a missing symbol error at link time.
|   ``HPX_DEFINE_PLAIN_ACTION`` can be inside the namespace or in the global namespace. The function is referenced by its fully qualified name out of the perspective of the macro placement, the action identifier must be a C++ conformant identifier for serialization purposes. (Best stick with numbers, letters, underscores ...). If you decide to put the Macro inside the namespace, you must reference the action in step 2 and 3 with the namespace in front of it like ``app::myFreeFunction_Action``.


**Step 2:** Function implementation in the shared library source:

    .. code-block:: cpp

       HPX_REGISTER_ACTION (  myFreeFunction_Action );
       namespace app {
           void myFreeFunction() {
               // .. doing my thing here, "HelloWorld", etc. ...
           }
       }

| Note:
|   ``HPX_REGISTER_ACTION`` **MUST** be in the global namespace. It is sufficient to just reference the action name you have chosen in the header here.
|
|   It is NOT necessary to specify the ``HPX_COMPONENT_EXPORT`` Macro again.


**Step 3:** Action invocation in the executable or whoever uses this library:

    .. code-block:: cpp

       // of course, you need to be inside your hpx_main scope somehow.
       // This example "fires and forgets" the action on the local console locality.
       // Both lines are equivalent:
       hpx::apply( myFreeFunction_Action(), hpx::find_here() );
       hpx::apply <myFreeFunction_Action> ( hpx::find_here() );
