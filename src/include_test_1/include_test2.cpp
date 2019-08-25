#include "include_test.hpp"
#include <hpx/hpx.hpp>

HPX_REGISTER_ACTION(
    test::some_function_action, some_function_action)

namespace test {
void some_function() {}
}
