_ConventionCrawler is currently under development._

_Status:_
* _Convention Grammar Fully Implemented_
* _Unit, Integration, and Functional tests implemented for current functionality_
* _CLI implemented, command-line script working_
* _Crawls a grails or retroBrowser app to find names of controller files_


_Next Steps:_
* _Fix unit/integration tests for controller_name_grammar_
* _Design functionality to take convention IR to grammar that finds action names_
  * _parse controller to find actions names_
* _Design functionality to compute endpoints from controller/action set_
  * _convert endpoint case style_
    * _Define grammar that converts different case styles into list of "words"_



_See [TODO](../../blob/master/TODO.md/) for upcoming features._

#Introduction

ConventionCrawler is a tool for crawling a convention-over-configuration application and extracting knowledge
about its structure.

In its current iteration, it extracts Controller and action names from Model-View-Controller applications.

It can be used as a command line util to generate a file containing the list of fully qualified Controller class
names along with their public actions, or added as a package to another Python app to generate that data as a
List of Strings.

#Usage

As a command-line app, ConventionCrawler should be run from within the base of the app it is to crawl.

ConventionCrawler requires one arguments: the convention of your app (e.g., `grails` or `retroBrowser`).

Some conventions, such as the retroBrowser convention, require the application name as a named argument.

Sample Usage:

`conventionCrawler grails`

`conventionCrawler retroBrowser --app_name tictactoe`

`conventionCrawler retroBrowser -a tictactoe`

#Installation

This is a Python 3 application and requires version 3.2 or greater.

This package can be installed with pip, which comes along with Python 3.4 and above. If downloading from this 
repository, you will need to run setup.py.

From within the downloaded repository, run:

`python3 setup.py install`

#Example Usage

###Web-app Security

[RetroBrowser](https://github.com/allisonf/retro-browser) will use ConventionCrawler as a mechanism to build a 
whitelist for validating URL endpoints.

#Set of Supported Frameworks

* [RetroBrowser](https://github.com/allisonf/retro-browser)
* [Grails](https://grails.org)
    * Grails 2 and 3 are supported

To add to the set of supported frameworks, just add a new [**Convention File**](#convention-files)

#<a name="identifying-your-framework">Identifying your framework</a>

ConventionCrawler has no default framework that it uses. The conventionCrawler command-line utility expects
an argument telling it what convention to use.

Usage

`conventionCrawler <convention>`

Sample Usage:

`conventionCrawler grails`

The value for the `<convention>` parameter should be the first part of the convention file name:

| Framework    | flag value   | convention file name    |
| :----------: | :----------: | :---------------------: |
| RetroBrowser | retroBrowser | retroBrowser.convention |
| Grails       | grails       | grails.convention       |

#<a name="convention-files">Convention Files</a>  

Convention Files are named `<framework>.convention` and live in the `conventions` directory at the base
of this project. Convention filenames are the lowerCamelCase form of the framework they describe. See the table in
[Identifying your framework](#identifying-your-framework) for examples.

As example, the [RetroBrowser convention file](../../blob/master/conventions/retroBrowser.convention),
`retroBrowser.convention`, is shown here, with comments:

```
// variable names are in angle brackets, < >
// variable names are valid python variable names
// variables are placeholders. They are keywords. Variable names are not freely chosen.
structure {
    app_dir: <app_name>
    controllers_dir: controllers
}

controller {
    <controller_name>Controller.py
}

action {
    def <action_name> (<A-Za-z0-9_,>):
}

// All the keywords are valid python variable names
endpoint {
    controller_style: upper_camel_case
    endpoint_style: lower_camel_case
    endpoint: <controller_name>/<action_name>
}

// Possible cases are:
// upper_camel_case
// lower_camel_case
// snake_case
```

_Note: The Convention Grammar does not support trailing whitespace at the end of the convention file._