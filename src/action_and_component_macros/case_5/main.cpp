#include <hpx/hpx.hpp>
#include <hpx/hpx_main.hpp>

#include <iostream>


HPX_REGISTER_COMPONENT_MODULE( );

struct SimpleThing : hpx::components::component_base<SimpleThing> {

    void shout( ) {
        std::cout << "Waaaahhhhh!" << std::endl;
    }
    HPX_DEFINE_COMPONENT_ACTION( SimpleThing, shout, shout_action );
};
// HPX_REGISTER_ACTION_DECLARATION( SimpleThing::shout_action, simple_thing_shout_action );
HPX_REGISTER_ACTION( SimpleThing::shout_action, simple_thing_shout_action );

// using myObj_component      = app::myObj;
// using myObj_component_type = hpx::components::component<app::myObj>;
HPX_REGISTER_COMPONENT( myObj_component_type, SimpleThing );
HPX_REGISTER_COMPONENT( hpx::components::component<SimpleThing>, SimpleThing );



///////////////////////////////////////////////////////////////////////////////

int main( ) {

    SimpleThing st;
    // calling function of local object directly
    st.shout( );
    hpx::async<SimpleThing::shout_action>( st.get_id( ) );

    return 0;
}
