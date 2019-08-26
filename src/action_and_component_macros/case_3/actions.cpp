#include <hpx/hpx.hpp>

#include "actions.hpp"

namespace test {

    // Free function in namespace
    int some_function( ) {
        return 42;
    }

} // namespace test

// (outside namespace)
// Parameters: Fully qualified action name, action name for serialization
HPX_REGISTER_ACTION( test::some_function_action, some_function_action_serialized );
