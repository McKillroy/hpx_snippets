#include <hpx/hpx.hpp>
#include <hpx/hpx_main.hpp>

#include <iostream>

// Free function in CUSTOM namespace in main program
namespace application {
    int compute_something( int data ) {
        return data * 42;
    }
}; // namespace application
HPX_PLAIN_ACTION( application::compute_something, compute_something_action );

int main( int argc, char* argv[] ) {
    std::cout << "Case 2:" << std::endl;

    // template parameter: Action name
    auto m_fut = hpx::async<compute_something_action>( hpx::find_here( ), 42 );

    std::cout << "Result: " << m_fut.get( ) << std::endl;

    return 0;
}