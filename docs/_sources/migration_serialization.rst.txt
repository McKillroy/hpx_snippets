Component Serialization, Migration and Deserialization
======================================================

It is possible to create components, which can be migrated to other localities. This implies, that not all components have this ability. Creating a component which can migrate is done by inheriting from ``migration_support`` and ``component_base`` with nested templates. 

| An example is given in the HPX codebase at 
| ``\tests\unit\component\migrate_component.cpp line 56 FF``

Example:

.. code-block:: cpp

   struct MigratingComponent : 
        hpx::components::migration_support
            <hpx::components::component_base 
                <MigratingComponent > > {
        // your code
    }

To enable a component to migrate you also need to provide a member function ``serialize``:

.. code-block:: cpp
    
   template <typename Archive>
   void serialize(Archive& ar, unsigned version);

The serialize member function is a template that works both ways: As Serializer and as Deserializer. The API is identical to the boost::serialize library, but a different, HPX specific implementation.

The type of the archive determines how the function works. There are two types of archives:
   | ``hpx::serialization::output_archive``
   | ``hpx::serialization::input_archive``

Normally you don't have to care about these, HPX is using the correct archive types automagically.

From comments in the file mentioned above:

.. code-block:: text

    "Components which should be migrated using hpx::migrate<> need to
    be Serializable and CopyConstructable. Components can be
    MoveConstructable in which case the serialized data is moved into the
    component's constructor."

``hpx::components::migrate`` returns a future containing the id_type of the migrating component. The future is available once the migration is complete. So - the id_type given to ``migrate`` as an argument is returned in the future and a means to check weather migration is yet complete.

Two conditions must be met for successful migration: 
The struct needs to inherit in the way shown above and you need a working serializer/deserializer: the ``serialize()`` function template.
  
**Special serialization situations:**

You can customize serialization in a way to send ANY data along with the component, by just adding it to the archive in your ``serialize()`` function template .

You can even send any arbitrary data with the archive and such serialize and deserialize components which have dependent non-component data referenced by pointers for example. To do this you need to split the serialize function template into two functions ``load()`` and ``save()`` AND add the macro ``HPX_SERIALIZATION_SPLIT_MEMBER()``
Example taken from ``\examples\quickstart\zerocopy_rdma.cpp line 64 ff``

.. code-block:: cpp

   // inside the struct:
   template <typename Archive>
   void load(Archive& ar, unsigned int const version)
   {
       std::size_t t = 0;
       ar >> size_ >> t;
       pointer_ = reinterpret_cast<pointer>(t);
   }

   template <typename Archive>
   void save(Archive& ar, unsigned int const version) const
   {
       std::size_t t = reinterpret_cast<std::size_t>(pointer_);
       ar << size_ << t;
   }

   HPX_SERIALIZATION_SPLIT_MEMBER()
