HPX Macros for Components and Actions
=========================================

When declaring and defining HPX components and -actions several macros are being used to create necessary boilerplate code. It is easy to get these wrong and make stupid mistakes, I am speaking out of experience! 

In the end, once learned it is just a recipe to be applied. In the meantime it can be a debugging hell if you don't know what you are doing.

The purpose of this document is to help others getting started with them and getting more secure about their use myself.

Several parameters influence how the macros should be used:

* Static versus dynamic Linkage
* Component actions (from methods) versus plain actions (from free functions)
* Having the source functions within a namespace or not.

The following Macros are being used:



HPX_DECLARE_ACTION and HPX_DECLARE_PLAIN_ACTION
    From ``hpx/runtime/actions/basic_action.hpp`` and ``hpx/runtime/actions/plain_action.hpp``:

    *Undocumented*

**Note:** These macros after a chain of macros finally lead to HPX_DECLARE_ACTION_2 which ends up with a simple struct declaration where the name depends on the parameters:

.. code-block:: C++

    struct name;

**Typical Use Case:** HK: yt?


HPX_DEFINE_PLAIN_ACTION
    This macro is being used to define a plain action. **This is the only macro which is allowed inside a namespace. All other macros MUST be used in the global namespace!** Don't confuse it with HPX_DECLARE_PLAIN_ACTION above!

Example use:

.. code-block:: C++

   // Some header file:
   
   namespace app{

     void my_free_function( );
     HPX_DEFINE_PLAIN_ACTION( my_free_function, my_free_function_action );

   };
   
   // Outside the namespace (!) :
   // Assign a name to the action which is usable in serialization. 
   // The namespace double colons would pose a problem otherwise.
   // It's a little bit like a typedef.
   HPX_REGISTER_ACTION_DECLARATION(app::my_free_function_action, my_free_function_action)

HPX_REGISTER_ACTION_DECLARATION
    From ``hpx/runtime/actions/basic_action.hpp``:

        *"Declare the necessary component action boilerplate code.* 

        *The macro HPX_REGISTER_ACTION_DECLARATION can be used to declare all the boilerplate code which is required for proper functioning of component actions in the context of HPX.*

        *The parameter action is the type of the action to declare the boilerplate for.*

        *This macro can be invoked with an optional second parameter. This parameter specifies a unique name of the action to be used for serialization purposes. The second parameter has to be specified if the first parameter is not usable as a plain (non-qualified) C++ identifier, i.e. the first parameter contains special characters which cannot be part of a C++ identifier, such as '<', '>', or ':'."*

**Note:** The macro is also used for plain actions, not just component actions.



HPX_PLAIN_ACTION
    From ``hpx/runtime/actions/plain_action.hpp``:

    *Defines a plain action type based on the given function func and registers it with HPX.*

    *The macro HPX_PLAIN_ACTION can be used to define a plain action (e.g. an action encapsulating a global or free function) based on the given function func. It defines the action type name representing the given function. This macro additionally registers the newly define action type with HPX.*

    *The parameter func is a global or free (non-member) function which should be encapsulated into a plain action. The parameter name is the name of the action type defined by this macro.*

**Note:** 



HPX_PLAIN_ACTION_ID
    From ``hpx/runtime/actions/plain_action.hpp``:
    
    *Defines a plain action type based on the given function func and registers it with HPX.*

    *The macro HPX_PLAIN_ACTION_ID can be used to define a plain action (e.g. an action encapsulating a global or free function) based on the given function func. It defines the action type actionname representing the given function.*

    *The parameter actionid specifies an unique integer value which will be used to represent the action during serialization.*

    *The parameter func is a global or free (non-member) function which should be encapsulated into a plain action. The parameter name is the name of the action type defined by this macro.*

    *The second parameter has to be usable as a plain (non-qualified) C++ identifier, it should not contain special characters which cannot be part of a C++ identifier, such as '<', '>', or ':'.*

**Note:** Looks like combining HPX_DEFINE_PLAIN_ACTION with HPX_REGISTER_ACTION_DECLARATION. Is that correct?



HPX_REGISTER_ACTION
    From ``hpx/runtime/actions/basic_action.hpp``:

    *"Define the necessary component action boilerplate code.*

    *The macro HPX_REGISTER_ACTION can be used to define all the boilerplate code which is required for proper functioning of component actions in the context of HPX.*

    *The parameter action is the type of the action to define the boilerplate for.*

    *This macro can be invoked with an optional second parameter. This parameter specifies a unique name of the action to be used for serialization purposes. The second parameter has to be specified if the first parameter is not usable as a plain (non-qualified) C++ identifier, i.e. the first parameter contains special characters which cannot be part of a C++ identifier, such as '<', '>', or ':'.*

    **Note:** *This macro has to be used once for each of the component actions defined using one of the HPX_DEFINE_COMPONENT_ACTION or HPX_DEFINE_PLAIN_ACTION macros. It has to occur exactly once for each of the actions, thus it is recommended to place it into the source file defining the component. Only one of the forms of this macro HPX_REGISTER_ACTION or HPX_REGISTER_ACTION_ID should be used for a particular action, never both."*


* HPX_REGISTER_COMPONENT_MODULE
    From ``hpx/runtime/components/component_factory_base.hpp``:

    *This macro is used to define the required Hpx.Plugin entry points. This macro has to be used in exactly one compilation unit of a component module.*



* HPX_REGISTER_COMPONENT
    From ``hpx/runtime/components/component_factory.hpp``:

    *Undocumented*

Important HPX Macros by file 
-----------------------------

File: ``basic_action.hpp``

    | HPX_REGISTER_ACTION
    | HPX_REGISTER_ACTION_DECLARATION
    | HPX_REGISTER_ACTION_ID
 

File: ``component_action.hpp``

    HPX_DEFINE_COMPONENT_ACTION

File: ``plain_action.hpp``

    | HPX_DECLARE_PLAIN_ACTION
    | HPX_DEFINE_PLAIN_ACTION
    | HPX_PLAIN_ACTION
    | HPX_PLAIN_ACTION_ID

File: ``component_commandline.hpp``

    | HPX_DEFINE_COMPONENT_COMMANDLINE_OPTIONS
    | HPX_REGISTER_COMMANDLINE_MODULE
    | HPX_REGISTER_COMMANDLINE_MODULE_DYNAMIC

File: ``component_commandline_base.hpp``

    | HPX_REGISTER_COMMANDLINE_OPTIONS
    | HPX_REGISTER_COMMANDLINE_OPTIONS_DYNAMIC
    | HPX_REGISTER_COMMANDLINE_REGISTRY
    | HPX_REGISTER_COMMANDLINE_REGISTRY_DYNAMIC

File: ``component_factory.hpp``

    | HPX_REGISTER_COMPONENT
    | HPX_REGISTER_COMPONENT_DYNAMIC
    | HPX_REGISTER_DISABLED_COMPONENT_FACTORY
    | HPX_REGISTER_DISABLED_COMPONENT_FACTORY_DYNAMIC
    | HPX_REGISTER_ENABLED_COMPONENT_FACTORY
    | HPX_REGISTER_ENABLED_COMPONENT_FACTORY_DYNAMIC
    | HPX_REGISTER_MINIMAL_COMPONENT_FACTORY
    | HPX_REGISTER_MINIMAL_COMPONENT_FACTORY\_
    | HPX_REGISTER_MINIMAL_COMPONENT_FACTORY_1
    | HPX_REGISTER_MINIMAL_COMPONENT_FACTORY_2
    | HPX_REGISTER_MINIMAL_COMPONENT_FACTORY_3
    | HPX_REGISTER_MINIMAL_COMPONENT_FACTORY_DYNAMIC
    | HPX_REGISTER_MINIMAL_COMPONENT_FACTORY_DYNAMIC\_
    | HPX_REGISTER_MINIMAL_COMPONENT_FACTORY_DYNAMIC_1
    | HPX_REGISTER_MINIMAL_COMPONENT_FACTORY_DYNAMIC_2
    | HPX_REGISTER_MINIMAL_COMPONENT_FACTORY_DYNAMIC_3

File: ``component_factory_base.hpp``

    | HPX_REGISTER_COMPONENT_FACTORY
    | HPX_REGISTER_COMPONENT_MODULE
    | HPX_REGISTER_COMPONENT_MODULE_DYNAMIC

File: ``component_registry.hpp``

    | HPX_REGISTER_MINIMAL_COMPONENT_REGISTRY
    | HPX_REGISTER_MINIMAL_COMPONENT_REGISTRY\_
    | HPX_REGISTER_MINIMAL_COMPONENT_REGISTRY_2
    | HPX_REGISTER_MINIMAL_COMPONENT_REGISTRY_3
    | HPX_REGISTER_MINIMAL_COMPONENT_REGISTRY_DYNAMIC
    | HPX_REGISTER_MINIMAL_COMPONENT_REGISTRY_DYNAMIC\_
    | HPX_REGISTER_MINIMAL_COMPONENT_REGISTRY_DYNAMIC_2
    | HPX_REGISTER_MINIMAL_COMPONENT_REGISTRY_DYNAMIC_3

File: ``component_registry_base.hpp``

    | HPX_REGISTER_COMPONENT_REGISTRY
    | HPX_REGISTER_COMPONENT_REGISTRY_DYNAMIC
    | HPX_REGISTER_REGISTRY_MODULE
    | HPX_REGISTER_REGISTRY_MODULE_DYNAMIC

File: ``component_startup_shutdown.hpp``

    | HPX_DEFINE_COMPONENT_STARTUP_SHUTDOWN
    | HPX_REGISTER_SHUTDOWN_MODULE
    | HPX_REGISTER_SHUTDOWN_MODULE_DYNAMIC
    | HPX_REGISTER_STARTUP_MODULE
    | HPX_REGISTER_STARTUP_MODULE_DYNAMIC
    | HPX_REGISTER_STARTUP_SHUTDOWN_MODULE
    | HPX_REGISTER_STARTUP_SHUTDOWN_MODULE\_
    | HPX_REGISTER_STARTUP_SHUTDOWN_MODULE_DYNAMIC

File: ``component_startup_shutdown_base.hpp``

    | HPX_REGISTER_STARTUP_SHUTDOWN_FUNCTIONS
    | HPX_REGISTER_STARTUP_SHUTDOWN_FUNCTIONS_DYNAMIC
    | HPX_REGISTER_STARTUP_SHUTDOWN_REGISTRY
    | HPX_REGISTER_STARTUP_SHUTDOWN_REGISTRY_DYNAMIC

File: ``component_type.hpp``

    | HPX_DEFINE_COMPONENT_NAME
    | HPX_DEFINE_COMPONENT_NAME\_
    | HPX_DEFINE_COMPONENT_NAME_2
    | HPX_DEFINE_COMPONENT_NAME_3
    | HPX_DEFINE_GET_COMPONENT_TYPE
    | HPX_DEFINE_GET_COMPONENT_TYPE_STATIC
    | HPX_DEFINE_GET_COMPONENT_TYPE_TEMPLATE

File: ``derived_component_factory.hpp``

    | HPX_REGISTER_DERIVED_COMPONENT_FACTORY
    | HPX_REGISTER_DERIVED_COMPONENT_FACTORY\_
    | HPX_REGISTER_DERIVED_COMPONENT_FACTORY_3
    | HPX_REGISTER_DERIVED_COMPONENT_FACTORY_4
    | HPX_REGISTER_DERIVED_COMPONENT_FACTORY_DYNAMIC
    | HPX_REGISTER_DERIVED_COMPONENT_FACTORY_DYNAMIC\_
    | HPX_REGISTER_DERIVED_COMPONENT_FACTORY_DYNAMIC_3
    | HPX_REGISTER_DERIVED_COMPONENT_FACTORY_DYNAMIC_4


File: ``static_factory_data.hpp``

    | HPX_DECLARE_FACTORY_STATIC
    | HPX_DEFINE_FACTORY_STATIC
    | HPX_INIT_REGISTRY_COMMANDLINE_STATIC
    | HPX_INIT_REGISTRY_FACTORY_STATIC
    | HPX_INIT_REGISTRY_MODULE_STATIC
    | HPX_INIT_REGISTRY_STARTUP_SHUTDOWN_STATIC


File: ``naming/address.hpp``

    HPX_ADDRESS_VERSION


