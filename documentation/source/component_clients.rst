What are "Client" Components (Typesafety)
=============================================

What are component "server" and "client" objects?
-------------------------------------------------

From the hpx documentation section `"terminology" <https://stellar-group.github.io/hpx/docs/sphinx/branches/master/singlehtml/index.html#terminology>`_:

.. code-block:: text

   " A component is a C++ object which can be accessed remotely. 
   A component can also contain member functions which can be invoked remotely. 
   These are referred to as component actions." 

**The component containing the functionality is called the "server".** Whenever you create an HPX component with the well known CRTP pattern, like:

.. code-block:: cpp

   struct SuperCoolComponent : public hpx::components::component_base< SuperCoolComponent > { 
    // your code ...
   }

You have created a component "server".

When creating member functions for your component and turning them into remotely callable actions (explanation of actions is beyond the scope of this document) which will return a future to the result you can call these actions with:

.. code-block:: cpp

   // example action invocation. Mind there are more ways to do this.
   myFuture = hpx::async<SuperCoolComponent::my_specal_action>( my_SuperCoolComponent_id );

``my_SuperCoolComponent_id`` is the AGAS address of the component we want to run the action ``my_special_action``.

The problem is: **Calling actions directly on the server component is not typesafe!** The compiler cannot check, if the required action actually exists for the component behind the id we pass as parameter.

``my_SuperCoolComponent_id`` is of type ``hpx::naming::id_type`` and is the AGAS equivalent of a ``void *`` in C++ (sortof...) . It has no type.

This is where "client" components come to the rescue. They are not required for using your core "server" component, but they give you a means to make the calls typesafe.

**Essentially a "client" component is a local, thin wrapper around the "server" component API to make the calls typesafe.** 

Basically you copy actions into your ``hpx::component::client_base`` derived component. 

**You can find good examples how to create client components in the hpx source tree at /examples/accumulator/\*.cpp**

**Pro Tip:** ``hpx::new_`` allows creating of remote server and local client components in one statement.

TODO: Code examples.
