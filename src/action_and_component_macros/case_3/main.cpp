#include <hpx/hpx.hpp>
#include <hpx/hpx_main.hpp>

#include "actions.hpp"

#include <iostream>

int main( ) {

    std::cout << "Case 3:" << std::endl;

    // template parameter: Fully qualified action name
    auto m_fut = hpx::async<test::some_function_action>( hpx::find_here( ) );

    std::cout << "Result: " << m_fut.get( ) << std::endl;

    return 0;
}
