#pragma once

#include <hpx/hpx.hpp>

namespace test {

    // Free function in namespace
    int some_function( );

    // Define the action (inside the namespace):
    // Parameters: function name, desired action name
    HPX_DEFINE_PLAIN_ACTION( some_function, some_function_action );

}; // namespace test

// Declare the Registering of the  Action (in global namespace)
// Parameters: Fully qualified action name, desired action name for serialization
// Note: When invoking the action we will still need the fully qualified action name!
HPX_REGISTER_ACTION_DECLARATION( test::some_function_action, some_function_action_serialized );
