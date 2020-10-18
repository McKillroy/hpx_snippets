How to build a custom vcpkg HPX port for your project
========================================================


vcpkg ( Git Repo: https://github.com/Microsoft/vcpkg, Docs: https://vcpkg.readthedocs.io ) is an open source  package manager by Microsoft. It provides so called "ports" of open source libraries which allow building them from source using the port definition. There also is a port for hpx which would be installed like ``./vcpkg install hpx:x64-windows`` on Windows as an example.

vcpkg ports can have so called features. e.g. the lua scripting language can be compiled as c++ which would give it exceptions instead of longjumps for error handling. E.g. ``./vcpkg install lua[cpp]:x64-windows`` uses that feature.

HPX has many many variables which can be used to modify how it is built:

https://hpx-docs.stellar-group.org/latest/html/manual/building_hpx.html?highlight=hpx%20allocator#cmake-variables

It is not really viable to try and force all this inbto a single port with a gazillion of features. Instead it is easier to learn how to use a custom port to achieve the results you want.

At the time of this writing (October 2020) the hpx port is pinned to version 1.5.1 of HPX and it consists of two files:

``CONTROL`` and ``portfile.cmake``

You can find them in ``<vcpkg_root>/ports/hpx`` 


The goal in this example is to replace the default system allocator in hpx with mimalloc. To achieve this we have just to do two things (copy the ``<vcpkg>/ports/hpx`` directory to another location and work on that copy, e.g.. 
``<my_project>/my_vcpkg_ports/hpx`` ):

1. Add mimalloc as a dependency to the CONTROL file (mimalloc can be built with vcpkg):

.. code-block:: text
   :caption: file: CONTROL
   :name: CONTROL_file

   Source: hpx
   Version: 1.5.1
   Build-Depends: mimalloc, hwloc, boost-accumulators, boost-algorithm, boost-asio, boost-bimap, boost-config, boost-context, boost-dynamic-bitset, boost-exception, boost-filesystem, boost-iostreams, boost-lockfree, boost-program-options, boost-range, boost-spirit, boost-system, boost-throw-exception, boost-variant, boost-winapi
   Homepage: https://github.com/STEllAR-GROUP/hpx
   Description: The C++ Standards Library for Concurrency and Parallelism
       HPX is a C++ Standards Library for Concurrency and Parallelism. It implements all of the corresponding facilities as defined by the C++ Standard. Additionally, in HPX we implement functionalities proposed as part of the ongoing C++ standardization process. We also extend the C++ Standard APIs to the distributed case.


So - I just added mimalloc to the ``Build-Depends`` field.

2. We also have to set the cmake variable ``HPX_WITH_MALLOC`` to ``mimalloc``. This can be done in the following section of the portfile.cmake:

.. code-block:: cmake
   :caption: file: portfile.cmake (snippet)
   :name: portfile_cmake_snippet

   vcpkg_configure_cmake(
       SOURCE_PATH ${SOURCE_PATH}
       PREFER_NINJA
       OPTIONS
           "-DBOOST_ROOT=${CURRENT_INSTALLED_DIR}/share/boost"
           "-DHWLOC_ROOT=${CURRENT_INSTALLED_DIR}/share/hwloc"
           -DHPX_WITH_VCPKG=ON
           -DHPX_WITH_TESTS=OFF
           -DHPX_WITH_EXAMPLES=OFF
           -DHPX_WITH_TOOLS=OFF
           -DHPX_WITH_RUNTIME=OFF
           -DHPX_WITH_MALLOC=mimalloc
   )

And that's basically it.
Now we have to make sure we have no vanilla hpx installed with vcpkg.

``./vcpkg list`` 

gives us a list of installed packages - remove any lingering hpx install:

``./vcpkg remove hpx:x64-windows``

And now we'd reinstall using the directory with our modified port.

``./vcpkg install hpx:x64-windows --overlay-ports=<my_project>/my_vcpkg_ports``

The overlaying process is also described in the vcpkg documentation here:

https://vcpkg.readthedocs.io/en/latest/specifications/ports-overlay/


