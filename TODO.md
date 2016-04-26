##TODO

* Write lexical analysis/intermediate representation integration tests
* Write semantic analysis for a validation phase that ensures uniqueness of sub-conventions
* unit test semantic analysis
* integration test semantic analysis
* Write functional tests for convention.init
* Design functionality to take IR to crawler that finds controller classes
* Design functionality to take convention IR to grammar that finds action names
* Design functionality to compute endpoints from controller/action set

##Completed

* Write integration tests for lexical analysis
* Define and implement Intermediate Representation
  * Implement as Custom Result Objects
    * Level 1
      * StructureConventionGrammar
      * ControllerConventionGrammar
      * ActionConventionGrammar
      * EndpointConventionGrammar
* Write unit tests for Intermediate Representation
  * StructureConventionGrammar
  * ControllerConventionGrammar
  * ActionConventionGrammar
  * EndpointConventionGrammar