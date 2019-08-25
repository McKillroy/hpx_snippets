.. r_creating_and_referencing_components.rst

Creating and Referencing Components
======================================

Boilerplate:
...............

Mind you - I am abbreviating stuff:

.. code-block:: cpp

   using hpx::naming::id_type;
   using hpx::find_here;
   using hpx::future;
   using hpx::new_;
   using hpx::local_new;
   using hpx::get_ptr;
   

Lets get started: 

Instancing
...........

.. code-block:: cpp

   future<id_type> new_<Component>(id_type)
   // in real code:
   auto my_thing_fut = new_<my_thing_type>( find_here() )

creates a new instance of component on locality *`id_type`* and returns an hpx::future to it

Note: the name ``new_`` was chosen to avoid the name name clash with the ``new`` keyword.


If you want to create the component locally and synchronously you just use 

.. code-block:: cpp

   future<id_type> local_new<Component>()
   // in real code:
   auto my_thing_fut = local_new<my_thing_type>( )

Note, that in both cases you get the id to the new instance with 

.. code-block:: cpp

   id_type  future<id_type>.get();
   // e.g.
   auto my_thing_id = my_thing_fut.get();

In the sync case it's just a very present (read: immediate) future.
So - you might just abbreviate it to:

.. code-block:: cpp

   id_type  local_new<Component>().get();

Pointers
.........

Now, for local and direct ( = faster) access to the instance you might want to have a pointer to it:

.. code-block:: cpp

   future <std::shared_ptr <Component> >   get_ptr <Component> (id_type); 
   //e.g.
   auto my_thing_shptr_fut = get_ptr <my_thing_type> (my_thing_id); 
   auto my_thing_shptr = my_thing_shptr_fut.get();

There are caveats: 

#. ``get_ptr<>`` works on only if the id refers to an object that is local to its invocation (same locality). 
#. ``get_ptr<>`` actually returns a ``future<shared_ptr<>>``, but you don't need to use ``get_ptr<>`` as you can always use 'id' to refer to the instance.
#. ``get_ptr<>`` would give you some optimization, but prevents the object from being migrated as long as you hold a shared_ptr to it. 

There is a sync overload to get the pointer: 

  .. code-block:: cpp

   auto p = get_ptr<Component>(hpx::launch::sync, id);

here 'p' is not a future, but the shared_ptr<> directly.


Destroying Components
.......................

Components are Garbage Collected after going out of scope and having shared pointers released.

