_ConventionCrawler is currently under development. It is not yet to a functional stage._

#Introduction

ConventionCrawler is a tool for crawling a convention-over-configuration application and extracting knowledge
about its structure.

In its current iteration, it extracts Controller and action names from Model-View-Controller applications.

It can be used as a command line util to generate a file containing the list of fully qualified Controller class
names along with their public actions, or added as a package to another Python app to generate that data as a
List of Strings.

#Example Usage

###Web-app Security

[RetroBrowser](https://github.com/allisonf/retro-browser) uses ConventionCrawler as a mechanism to build a 
whitelist for validating URL endpoints.

#Set of Supported Frameworks

* [RetroBrowser](https://github.com/allisonf/retro-browser)
* [Grails](https://grails.org)
    * Grails 2 and 3 are supported

To add to the set of supported frameworks, just add a new [**Convention File**](#convention-files)

#<a name="identifying-your-framework">Identifying your framework</a>

ConventionCrawler has no default framework that it uses. The conventionCrawler command-line util provides
a `-convention` flag (short version `-c`).

Usage

`-convention=<framework name>`

The value of the `-convention` flag should be the first part of the convention file name:

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
**structure:**
// Use the Groovy GString style for variables
// variable names are valid python variable names
// variables are placeholders. they are keywords. variable names are not freely chosen
    ${app_dir}
        controllers

**controllers:**
    ${controller_name}Controller.py

// All the keywords are valid python variable names
**controller_to_endpoint-mapping:**
    controller: UpperCamelCase
    endpoint: lowerCamelCase

// Possible cases are:
// UpperCamelCase
// lowerCamelCase
// snake_case
```