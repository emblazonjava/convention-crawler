##TODO

* Define and implement Intermediate Representation
** Implement as Custom Result Objects
*** Level 1
**** EndpointConvention
**** ActionConventionBody
***** This one is a special case, do it later _(Part of the grammar generator)_
**** ControllerConventionBody
***** This one is a special case, do it later _(Part of the grammar generator)_
**** AppDirConvention
**** ControllersDirConvention
** Implement grammar collapsing?
* Write unit tests for Intermediate Representation
* Write integration tests for semantic analysis
* Write functional tests for convention.init
* Design functionality to take IR to crawler that finds controller classes
* Design functionality to take convention IR to grammar that finds action names
* Design functionality to compute endpoints from controller/action set

##Completed

* Write integration tests for lexical analysis
* Define and implement Intermediate Representation
** Implement as Custom Result Objects
*** Level 1
**** ControllerStyleConvention
**** EndpointStyleConvention