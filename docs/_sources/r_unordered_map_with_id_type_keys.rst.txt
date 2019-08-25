.. r_unordered_map_with_id_type_keys.rst

Creating unordered map with id_type keys
==============================================

**Step 1:** Define your object and component actions in the header file

    .. code-block:: cpp
    
       struct IDTYPE_HASH {
           size_t operator()( const hpx::id_type &x ) {
               std::hash<hpx::naming::gid_type> ( ) ( x.get_gid ( ) );
           }
       };

       // map id_type on 32 indices in a vector
       unordered_map<id_type, uint32_t, IDTYPE_HASH> index;
