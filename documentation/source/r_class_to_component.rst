.. r_class_to_component.rst

Turning a struct or class into a component and use it's methods
==================================================================
  
There are two fundamental ways to do this:
  - Do it the basic way
  - Wrap the client side of things into a wrapper object to have typesafety and ease of mind
    
In this tutorial I'm doing it the dumb way without a client object, because that needs to be done anyways and such is always the first thing to do.

**Step 1:** Define your object and component actions in the header file

    .. code-block:: cpp

       ////////////////////////////
       // Component Library Header
       // myObj.hpp
       /* Boilerplate: Includes, etc ... */
       namespace app {
         struct HPX_EXPORT_COMPONENT myObj : PUBLIC hpx::components::component_base<myObj> {
           string sayHello();
           // Variant 1: Let the macro chose a default name for the action ("sayHello_action" in this case)
           HPX_DEFINE_COMPONENT_ACTION(myObj, sayHello); 
           string sayGoodBye(string sender);
           // Variant 2: Chose a custom name for the action ("sayGoodBye_a" in this case)
           HPX_DEFINE_COMPONENT_ACTION(myObj, sayGoodBye, sayGoodBye_a); // chosing a custom action name
           // We are not exposing this method as an action;
           void setName(string name);
           private:
           string name_ = "Nobody";
         };
         // Variant A: Inside the namespace: 
         // In this case the action will be known globally as app::myobj_component_sayHello_action
         HPX_REGISTER_ACTION_DECLARATION ( myObj::sayHello_action, myobj_component_sayHello_action );
       };
       // Variant B: Outside the namespace
       HPX_REGISTER_ACTION_DECLARATION ( app::myObj::sayGoodBye_a, myobj_component_sayGoodBye_a );


**Step 2:** Implement your methods in the source and add additional Macros to announce the component and the actions to HPX

    .. code-block:: cpp

       ////////////////////////////
       // Component Library
       // myObj.cpp
       /* Boilerplate: Includes, etc ... */

       string app:myObj::sayHello(){
           return "Hello ! I am " + (this->name_);
       }
       string app:myObj::sayGoodBye(string sender){
           return "Bye " + sender + "!";
       }
       void setName(string name){
           this->name_ = name;
       }

       // Announce everything to HPX:
       // 1. Needed for all components
       HPX_REGISTER_COMPONENT_MODULE ( );

       // 2. myObj component
       using myObj_component      = app::myObj;
       using myObj_component_type = hpx::components::component<app::myObj>;
       HPX_REGISTER_COMPONENT ( myObj_component_type, myObj_component );

       // 3. myObj component actions
       // These must match HPX_REGISTER_ACTION_DECLARATION in the header
       HPX_REGISTER_ACTION ( app::myObj::sayHello_action, app::myobj_component_sayHello_action );
       HPX_REGISTER_ACTION ( app::myObj::sayGoodBye_a,         myobj_component_sayGoodBye_a    );


**Step 3:** Use your component and actions in your HPX Application

    .. code-block:: cpp

       ////////////////////////////
       // Application Header
       // File: MyApp.hpp
       /* Boilerplate: Includes, etc ... */

       #include "myObj.hpp"

      /* other code ... */
      // This is really a very limited example ...
      // get our local locality id
      hpx::id_type here = hpx::find_here ( ); 
      // async + remote class instantiation (in this example: remote==local)
      hpx::future<hpx::id_type> fut = hpx::new_<app::myObj> ( here ); 
      // get new app::myObj instance id and wait for it if necessary
      hpx::id_type mObjId = fut.get ( ); 
      // start the sayHello Action on our object
      auto rFut = hpx::async<app::myObj::sayHello_action> ( mObjId );
      // wait for hello to finish and return a result
      cout << "Hello from new object: " << rFut.get ( ) << endl; 
      
      /* other code ... */
