##TODO

* Fix unit/integration tests for controller_name_grammar
* Design functionality to take convention IR to grammar that finds action names
  * parse controller to find actions names
* Design functionality to compute endpoints from controller/action set
  * convert endpoint case style
    * Define grammar that converts different case styles into list of "words"

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
* Write lexical analysis/intermediate representation integration tests
* Write semantic analysis for a validation phase that ensures uniqueness of sub-conventions
* integration test semantic analysis
* Write functional tests for convention.init
* write conventionCrawler script
* Design functionality to take IR to crawler that finds controller classes

