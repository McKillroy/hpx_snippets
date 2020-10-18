.. r_unordered_map_with_id_type_keys.rst

Creating unordered map with id_type keys
==============================================

``std::unordered_map`` needs a working hashing function. 

The functor below provides one that works with id_types:

    .. code-block:: cpp
    
       struct IDTYPE_HASH {
           size_t operator()( const hpx::id_type &x ) {
               std::hash<hpx::naming::gid_type> ( ) ( x.get_gid ( ) );
           }
       };

       // map id_types to uint32_t indices (which might point to a position in some std::array<>):
       unordered_map<id_type, uint32_t, IDTYPE_HASH> index;
