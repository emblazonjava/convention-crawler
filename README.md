_ConventionCrawler is currently under development._

_Status: Convention Grammar is working. Unit tests implemented and passing. Working on Intermediate Representation_

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
repository, you will need to build the distribution and then install it locally:

`python3 setup.py sdist --formats=zip`

This will create a `dist` folder in the base directory and in it you will find a file called `ConventionCrawler-0.1.zip`.

Copy `ConventionCrawler-0.1.zip` to a temporary location where you can unzip it. The unzipped folder still needs
to be installed. To install, make sure you are in the directory containing `ConventionCrawler-0.1.zip` and execute:

`pip3 install -e ConventionCrawler-0.1`

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
// variable names are in angle brackets, < >
// variable names are valid python variable names
// variables are placeholders. They are keywords. Variable names are not freely chosen.
structure {
    app_dir: <app_dir>
    controllers_dir: controllers
}

controller {
    <controller_name>Controller.py
}

action {
    def <action_name> (self<A-Za-z0-9_,>):
}

// All the keywords are valid python variable names
endpoint {
    controller_style: UpperCamelCase
    endpoint_style: lowerCamelCase
    endpoint: <controller_name>/<action_name>
}

// Possible cases are:
// UpperCamelCase
// lowerCamelCase
// snake_case
```

_Note: The Convention Grammar does not support trailing whitespace at the end of the file._