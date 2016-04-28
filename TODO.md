##TODO

* Implement rails.convention

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
* Design functionality to take convention IR to grammar that finds action names
  * Write GroovyActionGrammar and PythonActionGrammar
  * parse controller to find actions names
  * weed out function names of the form __init__
  * Return as list of tuples (controller_name, [action_name1, action_name2, ... ])
* Design functionality to compute endpoints from controller/action set
  * convert endpoint case style
    * Define grammar that converts different case styles into list of "words"
    * Define grammar_elem_init to return lower case of component words

