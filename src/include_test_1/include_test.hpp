#include <hpx/hpx.hpp>

namespace test {
void some_function();

HPX_DEFINE_PLAIN_ACTION(some_function, some_function_action);
}

HPX_REGISTER_ACTION_DECLARATION(
    test::some_function_action, some_function_action)