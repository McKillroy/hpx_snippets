(Draft) Requirements for a system of persistent id_types for HPX components
===============================================================================

1. id_types need to be (optionally) persistent over store/load cycles. Otherwise, References to stored objects may become invalid. This is also required for complete application shutdowns and restarts with different locality configurations (see point 6).

2. The current system stores locality IDs embedded into the id_type such, that the id quickly tells a client which locality is responsible for resolution of the final component location. This essentially is an implicit segmentation of the entire space for possible id_types into a segment of the size of a locality id space, which currently is 87 bit (see https://github.com/STEllAR-GROUP/hpx/blob/master/hpx/runtime/agas/server/primary_namespace.hpp#L52-L112).

3. The current id system could no longer serve its purpose if the locality whose id is embedded into the components id_type is down, but the component is loaded ( Is this actually possible at all ?). We need independence of the system from a specific locality being up or down. See also point 7

4. An Id system supporting persistence would require a central authority handing out id blocks since the natural segmentation of the id space by locality id would no longer be valid. Another form of segmentation is needed.

5. To solve the problem a change in the Global ID system is needed, by replacing the current implicit id space segmentation into an explicitly managed one.

6. Checkpointing of a set of objects to a persistent storage medium with the goal of being able to restore those while maintaining cross references must support differing locality configurations (number of localities), i.e. the checkpointed application may run on a different number of localities compared to the restored application.

7. AGAS is currently a distributed database without replication. Each locality has its AGAS instance, all taken together expose the full AGAS functionality. Every locality is responsible for the objects created on it. The locality even stays responsible for the address resolution of its objects if those have been migrated away to another locality.  

8. It is important, that the redistribution of stored objects to localities at load time can be customized. Spatially constrained simulations need to roughly keep objects which are close to each other in the simulation also together in one locality to minimize the object crosstalk penalty. Crosstalk across locality boundaries is expensive. To minimize the object crosstalk cost the cluster must become a rough mapping of the spatial situation of the simulation. E.g. a game simulation running on 4 localities might distribute objects on the worldmap into 4 quadrants, like NE, NW, SE, SW map quadrant (or any other spatial segmentation scheme), where each quadrant in this example would be run by a locality. This could actually result in long running simulations with lots of spatial repositioning of objects to run more optimized after such a store/load cycle, which can essentially be seen as an object redistribution cycle.

Suggestion A: 
------------------
* Central id_block administration
**Terms**
    Dictionary Service : The DS is the locality responsible for the resolution of a given object.
    Segment Table :      A table holding references of id blocks to locality ids

**Application Startup**

In the initialization and loading phase of the application, the ordered list of all stored id_types is segmented into segments of a configurable size. These segments are assigned to localities for id management. There can be localities solely working as dictionary service (Pure AGAS Nodes). 

**API Extension**

* Static Mapping: 
	Objects which are always on the locality which has their dictionary service. 
	Use Case: Optimize action calls internally.

* Id Change: 
	Allowing an id change for an object, e.g. to permanently migrate it and have the id management on the same locality (Turn into a statically mapped object). 


* Temporary IDs
	A new id_type for short lived and temporary objects, like futures could be used to not use up the pool of ids for persistent objects.

**Segmentation of the id_type space**
	Objects are segmented by their IDs and these Segments are assigned to localities for resolution. This could be stored in a segment resolution table which gets created on application launch and distributed over the cluster:

Example:

.. code-block::

   ID_Segment        Dictionary Service Locality
   -------------------------------------------
   000000 - 01FFFF     1
   020000 - 04FFFF     2
   030000 - 03FFFF     1
   040000 - 04FFFF     3
   .. etc pp


**CRUD Cycle**

* Create
    Async:  Get id from future when creating the Component.

    Sync:   Get Id from the local id_block and create the Component.
        Check size of remaining id_block, request new id_block if needed.

* Retrieve
| a. id → local_cache → cache_miss → id_segment → locality/dictionary service → query
| b. id → local_cache → cache_hit  → request    → success
| c. id → local_cache → cache_hit  → request    → failure → invalidate cache, retry
| d. When c. happens: Action forwarding by the dictionary service?


* Update
    Ids are const. No Updates. (except id change??)


* Delete
    Delete Component and notify Dictionary Service.



Suggestion B:
------------------
A new implicit segmentation schema: Hashing the id_types 

The old segmentation schema for the id_type space uses localities to segment the id_types. It is simple because of this implicit segmentation, but that also causes the problems with persistence.

Idea: Maybe just using the lowest n bits to select a bucket/responsible locality? → superfast hashing and bucket determination

Another way to implicitly determine the location of the dictionary service could be hashing. Hashing the id_type of a component would result in a hash, which would be the key in the segmentation table.

The disadvantage would be, that creation of an object would most of the time require the id to be managed elsewhere. 


Suggestion C:
--------------

Allow a change of the responsible locality and keep a local cache entry to it. 

This would allow migration of objects and their managing locality on the fly. 

Failure of requests would lead to local cache invalidation and re-caching after resolving by some mechanism (some directory service or something similar). 



