#include "include_test.hpp"

#include <hpx/hpx.hpp>
#include <hpx/hpx_main.hpp>

int main()
{
    auto f = hpx::async<test::some_function_action>(hpx::find_here());
    f.get();

    return 0;
}