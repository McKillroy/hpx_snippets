Get Component Pointer from id_type
=====================================

Sometimes you need a pointer to an HPX component. Here's how to get it:

.. code-block:: cpp 
   :caption: hpx::get_ptr 
   :name: hpx::get_ptr

    // Overload 1/4
    hpx::future< std::shared_ptr <Component> > 
    hpx::get_ptr( naming::id_type const & id )
    // Overload 2/4
    hpx::future < std::shared_ptr 
      <typename components::client_base<Derived, Stub>::server_component_type> >
    hpx::get_ptr( components::client_base< Derived, Stub > const & c )  
    // Overload 3/4
    std::shared_ptr< Component >  
    hpx::get_ptr( launch::sync_policy, naming::id_type const & id, 
                  error_code & ec = throws )
    // Overload 4/4
    std::shared_ptr< typename components::client_base<Derived, Stub>::server_component_type > 
    hpx::get_ptr( launch::sync_policy p, 
                  components::client_base< Derived, Stub > const & c,
                  error_code & ec = throws 
    )

**CAVEAT:** If you create components which are meant to migrate between localities, migrating them is not possible, as long as you hold shared pointers to them!
