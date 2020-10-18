.. macro_renaming_draft.rst

Draft: Renaming Macros 
-----------------------------

1. Defining Actions (in header file):

	* **HPX_DEFINE_PLAIN_ACTION**      -> Defines a plain action
	* **HPX_DEFINE_COMPONENT_ACTION**  -> Defines a Component Action


2. Registration steps: They are the same for plain actions and component actions:

	* **HPX_DECLARE_ACTION_REGISTRATION** -> goes into the header file 
	* **HPX_DEFINE_ACTION_REGISTRATION**  -> goes into the source file 

3. Declare Action Registration:

	* **HPX_DECLARE_PLAIN_ACTION**     -> Declares a plain action (rarely needed, special case)
	* **HPX_DECLARE_COMPONENT_ACTION** -> Unnecessary, since the class is in the header file anyways 


**Convenience Macros:**

**HPX_PLAIN_ACTION**     -> Defines a plain action in the header file AND declares it's registration (which is done in the source file)

**HPX_COMPONENT_ACTION** -> Defines a component action in the header file AND declares it's registration (which is done in the source file)

**HPX_COMPONENT_REGISTRY** -> Creates the component registry in the component compilation unit once: Former HPX_REGISTER_COMPONENT_MODULE

