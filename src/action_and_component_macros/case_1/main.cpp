#include <hpx/hpx.hpp>
#include <hpx/hpx_main.hpp>

#include <iostream>

// Free function in GLOBAL namespace in main program
int compute_something(int data)
{
    return data * 42;
}
HPX_PLAIN_ACTION(compute_something, compute_something_action);

int main(int argc, char* argv[])
{
    std::cout << "Case 1:" << std::endl;

    // template parameter: Action name
    auto m_fut = hpx::async<compute_something_action>(hpx::find_here(), 42);

    std::cout << "Result: " << m_fut.get() << std::endl;

    return 0;
}