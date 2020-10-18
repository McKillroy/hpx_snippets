
.. .. contents::

.. contents:: 
   :local: 

=========================================
HPX Macros for Components and Actions 
=========================================

When declaring and defining HPX components and -actions several macros are being used to create necessary boilerplate code. It is easy to get these wrong and make stupid mistakes, I am speaking out of experience! 

In the end, once learned it is just a recipe to be applied. In the meantime it can be a debugging hell if you don't know what you are doing.

The purpose of this document is to help others getting started with them and getting more secure about their use myself.



Creating a usable action: Define and Register
------------------------------------------------

I assume you already have a header and a source file pair with your function declaration and definition in them.

The process of creating a usable action from it then is a two-step process, consisting of an *action definition*, which defines a type and is done in the header file and an *action registration*, which is done in the source file. To be usable everywhere, *the registration also must be declared* in the header file. So - the second step has two steps which means in the end it comes down to using three macros - two in the header file and one in the source file:

.. code-block:: text

    Header file (.hpp): Action Definition
    Source file (.cpp): Action Registration
    Header file (.hpp): Declaration of the Action Registration


1. **Define** an action


    Internally defining an action with the according macro binds the local function address to the action type (a struct) which then is being used to call the function after receiving a serialized package with the information from a remote partner. 
    
    When an action is used locally the action struct is also working as a functor for synchronous local calls.

    Technically on creation the function address to the wrapped function is passed as an integral template argument (Implementation Detail, see ``hpx::actions::make_action`` in ``runtime\actions\basic_action.hpp`` if you are interested in the nitty gritty details).

    Since this is a type definition (not a function definition) there is no problem having these macros in the header file. Actually you need them in the header file only or stuff will break.

    **Special case**

    Declaring an action would be done like ``HPX_DECLARE_ACTION(myFunction_action)`` which expands to ``struct myFunction_action;`` - all actions are just structs. 
    You might want to use that in special situations, normally it's not needed, since actions (they are types) are already defined in the header file.


2. **Register** an action: A two-step process


    * **Registering the action is a two-phase process**

    The registration process is a combination of two things:

        1. The Definition of auxiliary functions in the source file
        2. The declaration of these functions in the header file. ( 1. and 2. Explained further below)

    * **A. Registering the action**

    Registering an action ("Action Registration") is done in the source file (.cpp) and defines auxiliary functions needed for serialization/deserialization of the action. 

    Example: 

    .. code-block:: C++
    
       // In the source file (.cpp)
       // Registers the action "my_namespace::my_function_action" with HPX and 
       // assigns the name "my_function_action_name_for_serialization" to it so it can be serialized. 
       // This new and system-wide unique C-Identifier is also being used for naming the auxiliary 
       // functions which are being created in the process.

       HPX_REGISTER_ACTION( my_namespace::my_function_action, my_function_action_name_for_serialization );

    my_function_action_name_for_serialization MUST be a system wide UNIQUE and valid C-Identifier !!!

    * **B. Declare an action registration**

    The Declaration of the auxiliary functions described above is done in the header file (.hpp) with **HPX_DECLARE_ACTION_REGISTRATION**.
    
    The arguments MUST be the same, just like when declaring and defining conventional functions in a header/source file pair.

    Example: 

    .. code-block:: C++
    
       // In the header file (.hpp)
       // Declares the action registration
       HPX_DECLARE_ACTION_REGISTRATION( my_namespace::my_function_action, my_function_action_name_for_serialization );


    Some Macros allow you to define the action and declare the registration in one move, e.g. **HPX_PLAIN_ACTION**.


**Several parameters influence macro usage:**

    * Static versus dynamic Linkage
    * Component actions (from methods) versus plain actions (from free functions or static member functions)
    * Having the functions inside a namespace or not.


Putting components and actions into shared libraries
--------------------------------------------------------


**HPX_COMPONENT_EXPORT** for components

**CAVEAT:** for functions used in actions You need to use your own export/import macros !!!


Action Macros
------------------


* **HPX_DECLARE_ACTION**


**File:** ``hpx/runtime/actions/basic_action.hpp``
   
**Prototype:**
    
**Parameters:**

**Description:**
    
    Expands to ``struct actionname;`` Just a simple struct declaration if you need it.
    
**Examples:**
    
.. code-block:: C++

    // expands to struct my_action;
    HPX_DECLARE_ACTION(my_action);




* **HPX_DEFINE_PLAIN_ACTION**


**File:** ``hpx/runtime/actions/plain_action.hpp``

**Prototype:**

    HPX_DEFINE_PLAIN_ACTION( QualifiedFunctionName, PlainActionName = QualifiedFunctionName_action) 

**Description:**

    | HPX_DEFINE_PLAIN_ACTION is being used to *define* a plain action. 
    | **HPX_DEFINE_PLAIN_ACTION is the only macro which is allowed inside a namespace.**
    | **All other macros MUST be used in the global namespace!** 
    |     
    | Don't confuse it with HPX_DECLARE_PLAIN_ACTION above!
    |     
    | It defines the action linked to the function you want to expose as described below. 
    | You can forward declare any action with ``struct action_name;``

**Parameters:**

    | Non Member Function: (Free Function or static member), 
    | *Note:* Fully Qualified if outside namespace (Out of the perspective of the Macro placement)
    | *Note:* Second Parameter defaults to "_action" being appended like ``FunctionName_action`` 

**Examples:**

    | HPX_DEFINE_PLAIN_ACTION( my_function )
    | results in an action definition: my_function_action

    | HPX_DEFINE_PLAIN_ACTION( my_function, my_function_a )
    | results in an action definition: my_function_a

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




* **HPX_PLAIN_ACTION**


**File:** ``hpx/runtime/actions/plain_action.hpp``

**Prototype:**

**Description:**

| *Defines a plain action type based on the given function func and registers it with HPX.*
| *The macro HPX_PLAIN_ACTION can be used to define a plain action (e.g. an action encapsulating a global or free function) based on the given function func. It defines the action type name representing the given function. This macro additionally registers the newly define action type with HPX.*
| *The parameter func is a global or free (non-member) function which should be encapsulated into a plain action. The parameter name is the name of the action type defined by this macro.*

**Parameters:**

**Examples:**

.. code-block:: C++

   // Put example code here ...




* **HPX_DECLARE_PLAIN_ACTION**



**File:** ``hpx/runtime/actions/plain_action.hpp``
   
**Prototype:**
    
**Description:**  

    *Undocumented*
    Definition + Registration Declaration ???
    Still requires proper registration in the sources.
    
**Note:** These macros after a chain of macros finally lead to HPX_DECLARE_ACTION_2 which ends up with a simple struct declaration where the name depends on the parameters:
    
**Parameters:**
    
**Examples:**
   
.. code-block:: C++

    struct name;





* **HPX_REGISTER_ACTION**


**File:** ``hpx/runtime/actions/basic_action.hpp``

**Prototype:**

**Parameters:**

**Description:**

| *"Define the necessary component action boilerplate code.*
| *The macro HPX_REGISTER_ACTION can be used to define all the boilerplate code which is required for proper functioning of component actions in the context of HPX.*
| *The parameter action is the type of the action to define the boilerplate for.*
| *This macro can be invoked with an optional second parameter. This parameter specifies a unique name of the action to be used for serialization purposes. The second parameter has to be specified if the first parameter is not usable as a plain (non-qualified) C++ identifier, i.e. the first parameter contains special characters which cannot be part of a C++ identifier, such as '<', '>', or ':'.*

**Note:** *This macro has to be used once for each of the component actions defined using one of the HPX_DEFINE_COMPONENT_ACTION or HPX_DEFINE_PLAIN_ACTION macros. It has to occur exactly once for each of the actions, thus it is recommended to place it into the source file defining the component. Only one of the forms of this macro HPX_REGISTER_ACTION or HPX_REGISTER_ACTION_ID should be used for a particular action, never both."*

**Examples:**

.. code-block:: C++

   // Put example code here ...





* **HPX_REGISTER_ACTION_DECLARATION**



**File:** ``hpx/runtime/actions/basic_action.hpp``

**Prototype:**

**Parameters:**

**Description:**
        
| *"Declare the necessary component action boilerplate code.* 
| *The macro HPX_REGISTER_ACTION_DECLARATION can be used to declare all the boilerplate code which is required for proper functioning of component actions in the context of HPX.*
| *The parameter action is the type of the action to declare the boilerplate for.*
| *This macro can be invoked with an optional second parameter. This parameter specifies a unique name of the action to be used for serialization purposes. The second parameter has to be specified if the first parameter is not usable as a plain (non-qualified) C++ identifier, i.e. the first parameter contains special characters which cannot be part of a C++ identifier, such as '<', '>', or ':'."*

**Note:** The macro is also used for plain actions, not just component actions.

**Examples:**

.. code-block:: C++

   // Put example code here ...
   



Component Macros 
--------------------



* **HPX_REGISTER_COMPONENT_MODULE**


**File:** ``hpx/runtime/components/component_factory_base.hpp``

**Prototype:**

**Parameters:**
    None

**Description:**

    | This macro is used to define the required Hpx.Plugin entry points.
    | It has to be used in exactly one compilation unit of a component module.
    | It creates the module wide component registry.

**Examples:**

.. code-block:: C++

   // In the source file (.cpp)
   // needed only once per component source file
   HPX_REGISTER_COMPONENT_MODULE();


* **HPX_REGISTER_COMPONENT**


**File:** ``hpx/runtime/components/component_factory.hpp``

**Prototype:**

**Parameters:**

**Description:**

    Needed once per component in the source file. Creates auxiliary functions (component factories) to remotely create the component. 

**Examples:**

.. code-block:: C++

   // Put example code here ...
   HPX_REGISTER_COMPONENT


Macros for Shared Library Symbol Export for Actions and Components
------------------------------------------------------------------------

* **HPX_COMPONENT_EXPORT**


**File:** ``hpx/config/export_definitions.hpp``

**Prototype:**

    | HPX_COMPONENT_EXPORT class-key attr class-head-name base-clause { member-specification }

**Parameters:**

    None

**Description:**

    | HPX_COMPONENT_EXPORT is needed to export the symbol names when putting the components or functions into a shared library.

**Examples:**

.. code-block:: C++

   // In the header file (.hpp)

