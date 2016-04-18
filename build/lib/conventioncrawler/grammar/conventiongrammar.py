import modgrammar as m
import conventioncrawler.grammar.intermediaterepresentation as ir

grammar_whitespace_mode = 'optional'


# separators

# {
class OpenCurlyBracket (m.Grammar):
    """
    >>> myparser = OpenCurlyBracket.parser()
    >>> myparser.parse_string("{")
    OpenCurlyBracket<'{'>
    """

    grammar = "{"

# }
class CloseCurlyBracket (m.Grammar):
    """
    >>> myparser = CloseCurlyBracket.parser()
    >>> myparser.parse_string("}")
    CloseCurlyBracket<'}'>
    """

    grammar = "}"

# <
class OpenAngleBracket (m.Grammar):
    """
    >>> myparser = OpenAngleBracket.parser()
    >>> myparser.parse_string("<")
    OpenAngleBracket<'<'>
    """

    grammar = "<"

# >
class CloseAngleBracket (m.Grammar):
    """
    >>> myparser = CloseAngleBracket.parser()
    >>> myparser.parse_string(">")
    CloseAngleBracket<'>'>
    """

    grammar = ">"

# :
class Colon (m.Grammar):
    """
    >>> myparser = Colon.parser()
    >>> myparser.parse_string(":")
    Colon<':'>
    """

    grammar = ":"

# ,
class Comma (m.Grammar):
    """
    >>> myparser = Comma.parser()
    >>> myparser.parse_string(',')
    Comma<','>
    """

    grammar = ","

# app_dir
class AppDirVariableName (m.Grammar):
    """
    >>> myparser = AppDirVariableName.parser()
    >>> myparser.parse_string("app_dir")
    AppDirVariableName<'app_dir'>
    """

    grammar = "app_dir"

# <app_dir>
class AppDirVariable (m.Grammar):
    """
    >>> myparser = AppDirVariable.parser()
    >>> myparser.parse_string("<app_dir>")
    AppDirVariable<'<', 'app_dir', '>'>
    """

    grammar = (OpenAngleBracket, AppDirVariableName, CloseAngleBracket)

# controller_name
class ControllerNameVariableName (m.Grammar):
    """
    >>> myparser = ControllerNameVariableName.parser()
    >>> myparser.parse_string("controller_name")
    ControllerNameVariableName<'controller_name'>
    """

    grammar = "controller_name"

# <controller_name>
class ControllerNameVariable (m.Grammar):
    """
    >>> myparser = ControllerNameVariable.parser()
    >>> myparser.parse_string("<controller_name>")
    ControllerNameVariable<'<', 'controller_name', '>'>
    """

    grammar = (OpenAngleBracket, ControllerNameVariableName, CloseAngleBracket)

# action_name
class ActionNameVariableName (m.Grammar):
    """
    >>> myparser = ActionNameVariableName.parser()
    >>> myparser.parse_string("action_name")
    ActionNameVariableName<'action_name'>
    """

    grammar = "action_name"

# <action_name>
class ActionNameVariable (m.Grammar):
    """
    >>> myparser = ActionNameVariable.parser()
    >>> myparser.parse_string("<action_name>")
    ActionNameVariable<'<', 'action_name', '>'>
    """

    grammar = (OpenAngleBracket, ActionNameVariableName, CloseAngleBracket)

# A-Za-z0-9_,
class AllowedChars (m.Grammar):
    """
    >>> myparser = AllowedChars.parser()
    >>> myparser.parse_string("A-Za-z0-9_,")
    AllowedChars<'A-Za-z0-9_,'>
    """

    grammar = m.WORD("A-Za-z0-9_,\-", escapes=True)

# <A-Za-z0-9_,>
class AllowedCharsVariable (m.Grammar):
    """
    >>> myparser = AllowedCharsVariable.parser()
    >>> myparser.parse_string("<A-Za-z0-9_,>")
    AllowedCharsVariable<'<', 'A-Za-z0-9_,', '>'>
    """

    grammar = (OpenAngleBracket, AllowedChars, CloseAngleBracket)

# e.g., controllers
class DirNameConstant (m.Grammar):
    """
    >>> myparser = DirNameConstant.parser()
    >>> myparser.parse_string("controllers")
    DirNameConstant<'controllers'>
    """

    grammar = m.WORD("A-Za-z0-9\-", escapes=True)

# e.g., Controllers.py
class FileNameConstant (m.Grammar):
    """
    >>> myparser = FileNameConstant.parser()
    >>> myparser.parse_string("Controllers.py")
    FileNameConstant<'Controllers.py'>
    """

    grammar = m.WORD("A-Za-z0-9\-.", escapes=True)

# e.g., def
class LanguageKeywordConstant (m.Grammar):
    """
    >>> myparser = LanguageKeywordConstant.parser()
    >>> myparser.parse_string("def")
    LanguageKeywordConstant<'def'>
    """

    grammar = grammar = m.WORD("a-z")

# (
# )
class Parenthesis (m.Grammar):
    """
    >>> myparser = Parenthesis.parser()
    >>> myparser.parse_string("(")
    Parenthesis<'('>
    >>> myparser.parse_string(")")
    Parenthesis<')'>
    """

    grammar = (m.LITERAL("(") | m.LITERAL(")"))


# StructureConventionGrammar

# structure
class StructureKeyword (m.Grammar):
    """
    >>> myparser = StructureKeyword.parser()
    >>> myparser.parse_string("structure")
    StructureKeyword<'structure'>
    """

    grammar = "structure"

# app_dir
class AppDirKeyword (m.Grammar):
    """
    >>> myparser = AppDirKeyword.parser()
    >>> myparser.parse_string("app_dir")
    AppDirKeyword<'app_dir'>
    """

    grammar = "app_dir"

# controllers_dir
class ControllersDirKeyword (m.Grammar):
    """
    >>> myparser = ControllersDirKeyword.parser()
    >>> myparser.parse_string("controllers_dir")
    ControllersDirKeyword<'controllers_dir'>
    """

    grammar = "controllers_dir"

# app_dir: <app_dir>
class AppDirConvention (m.Grammar):
    """
    >>> myparser = AppDirConvention.parser()
    >>> myparser.parse_string("app_dir: <app_dir>")
    AppDirConvention<'app_dir', ':', '<app_dir>'>
    """

    grammar = (AppDirKeyword, Colon, AppDirVariable | DirNameConstant)

# controllers_dir: controllers
class ControllersDirConvention (m.Grammar):
    """
    >>> myparser = ControllersDirConvention.parser()
    >>> myparser.parse_string("controllers_dir: controllers")
    ControllersDirConvention<'controllers_dir', ':', 'controllers'>
    """

    grammar = (ControllersDirKeyword, Colon, DirNameConstant)


# Next processing step limits to one of each
# app_dir: <app_dir>
# controllers_dir: controllers
class StructureConventionBody (m.Grammar):
    """
    >>> myparser = StructureConventionBody.parser()
    >>> myparser.parse_string("app_dir: <app_dir>\\ncontrollers_dir: controllers").elements
    (<REPEAT><'app_dir: <app_dir>', 'controllers_dir: controllers'>,)
    >>> myparser.parse_string("controllers_dir: controllers\\napp_dir: <app_dir>").elements
    (<REPEAT><'controllers_dir: controllers', 'app_dir: <app_dir>'>,)
    """

    grammar = m.REPEAT(AppDirConvention | ControllersDirConvention)#, sep=m.BOL)
    #grammar = (AppDirConvention, ControllersDirConvention)

# structure {
#     app_dir: <app_dir>
#     controllers_dir: controllers
# }
class StructureConventionGrammar (m.Grammar):
    """
    >>> myparser = StructureConventionGrammar.parser()
    >>> myparser.parse_string("structure {\\napp_dir: <app_dir>\\ncontrollers_dir: controllers\\n}")
    StructureConventionGrammar<'structure', '{', 'app_dir: <app_dir>\\ncontrollers_dir: controllers', '}'>
    >>> myparser.parse_string("structure {\\ncontrollers_dir: controllers\\napp_dir: <app_dir>\\n}")
    StructureConventionGrammar<'structure', '{', 'controllers_dir: controllers\\napp_dir: <app_dir>', '}'>
    """

    grammar = (StructureKeyword, OpenCurlyBracket, StructureConventionBody, CloseCurlyBracket)

# ControllerConventionGrammar

# controller
class ControllerKeyword (m.Grammar):
    """
    >>> myparser = ControllerKeyword.parser()
    >>> myparser.parse_string("controller")
    ControllerKeyword<'controller'>
    """

    grammar = "controller"

# <controller_name>Controller.py
class ControllerConventionBody (m.Grammar):
    """
    >>> myparser = ControllerConventionBody.parser()
    >>> myparser.parse_string("<controller_name>Controller.py")
    ControllerConventionBody<'<controller_name>', 'Controller.py'>
    """

    grammar = (ControllerNameVariable, FileNameConstant)

# controller {
#     <controller_name>Controller.py
# }
class ControllerConventionGrammar (m.Grammar):
    """
    >>> myparser = ControllerConventionGrammar.parser()
    >>> myparser.parse_string("controller {\\n<controller_name>Controller.py\\n}")
    ControllerConventionGrammar<'controller', '{', '<controller_name>Controller.py', '}'>
    """

    grammar = (ControllerKeyword, OpenCurlyBracket, ControllerConventionBody, CloseCurlyBracket)

# ActionConventionGrammar

# action
class ActionKeyword (m.Grammar):
    """
    >>> myparser = ActionKeyword.parser()
    >>> myparser.parse_string("action")
    ActionKeyword<'action'>
    """

    grammar = "action"

# TODO: Want to use REPEAT for a more dynamic function def
# def <action_name> (self<A-Za-z0-9_,>):
class ActionConventionBody (m.Grammar):
    """
    >>> myparser = ActionConventionBody.parser()
    >>> myparser.parse_string("def <action_name> (self<A-Za-z0-9_,>):")
    ActionConventionBody<'def', '<action_name>', '(', 'self', '<A-Za-z0-9_,>', ')', ':'>
    """

    grammar = (LanguageKeywordConstant, ActionNameVariable, Parenthesis, m.OPTIONAL(LanguageKeywordConstant), AllowedCharsVariable, Parenthesis, Colon | OpenCurlyBracket)

# action {
#     def <action_name> (self<A-Za-z0-9_,>):
# }
class ActionConventionGrammar (m.Grammar):
    """
    >>> myparser = ActionConventionGrammar.parser()
    >>> myparser.parse_string("action {\\ndef <action_name> (self<A-Za-z0-9_,>):\\n}")
    ActionConventionGrammar<'action', '{', 'def <action_name> (self<A-Za-z0-9_,>):', '}'>
    """

    grammar = (ActionKeyword, OpenCurlyBracket, ActionConventionBody, CloseCurlyBracket)

# EndpointConventionGrammar

# endpoint
class EndpointKeyword (m.Grammar):
    """
    >>> myparser = EndpointKeyword.parser()
    >>> myparser.parse_string("endpoint")
    EndpointKeyword<'endpoint'>
    """

    grammar = "endpoint"

# e.g., upper_camel_case
# e.g., lower_camel_case
# e.g., snake_case
class CaseStyle (m.Grammar):
    """
    >>> myparser = CaseStyle.parser()
    >>> myparser.parse_string("upper_camel_case")
    CaseStyle<'upper_camel_case'>
    >>> myparser.parse_string("lower_camel_case")
    CaseStyle<'lower_camel_case'>
    >>> myparser.parse_string('snake_case')
    CaseStyle<'snake_case'>
    """

    grammar = (m.LITERAL("upper_camel_case") | m.LITERAL("lower_camel_case") | m.LITERAL("snake_case"))
    grammar_collapse = True

# controller_style
class ControllerStyleKeyword (m.Grammar):
    """
    >>> myparser = ControllerStyleKeyword.parser()
    >>> myparser.parse_string("controller_style")
    ControllerStyleKeyword<'controller_style'>
    """

    grammar = "controller_style"

# controller_style: snake_case
class ControllerStyleConvention (m.Grammar):
    """
    >>> myparser = ControllerStyleConvention.parser()
    >>> myparser.parse_string("controller_style: snake_case")
    ControllerStyleConvention<'controller_style', ':', 'snake_case'>
    """

    grammar = (ControllerStyleKeyword, Colon, CaseStyle)

    def grammar_elem_init(self, sessiondata):

        self.controller_style = ir.CaseStyle[self[2].string]


# endpoint_style
class EndpointStyleKeyword (m.Grammar):
    """
    >>> myparser = EndpointStyleKeyword.parser()
    >>> myparser.parse_string("endpoint_style")
    EndpointStyleKeyword<'endpoint_style'>
    """

    grammar = "endpoint_style"

# endpoint_style: lower_camel_case
class EndpointStyleConvention (m.Grammar):
    """
    >>> myparser = EndpointStyleConvention.parser()
    >>> myparser.parse_string("endpoint_style: lower_camel_case")
    EndpointStyleConvention<'endpoint_style', ':', 'lower_camel_case'>
    """

    grammar = (EndpointStyleKeyword, Colon, CaseStyle)

    def grammar_elem_init(self, sessiondata):

        self.endpoint_style = ir.CaseStyle[self[2].string]

# <controller_name>/<action_name>
class URLConvention (m.Grammar):
    """
    >>> myparser = URLConvention.parser()
    >>> myparser.parse_string("<controller_name>/<action_name>").elements
    (<LIST><'<controller_name>', '/', '<action_name>'>,)
    """

    grammar = m.LIST_OF(ControllerNameVariable | ActionNameVariable, sep="/")

# endpoint: <controller_name>/<action_name>
class EndpointConvention (m.Grammar):
    """
    >>> myparser = EndpointConvention.parser()
    >>> myparser.parse_string("endpoint: <controller_name>/<action_name>")
    EndpointConvention<'endpoint', ':', '<controller_name>/<action_name>'>
    """

    grammar = (EndpointKeyword, Colon, URLConvention)

# Next Processing phase will ensure one and only one of each
# controller_style: upper_camel_case
# endpoint_style: lower_camel_case
# endpoint: <controller_name>/<action_name>
class EndpointConventionBody (m.Grammar):
    """
    >>> myparser = EndpointConventionBody.parser()
    >>> myparser.parse_string("controller_style: upper_camel_case\\nendpoint_style: lower_camel_case\\nendpoint: <controller_name>/<action_name>").elements
    (<REPEAT><'controller_style: upper_camel_case', 'endpoint_style: lower_camel_case', 'endpoint: <controller_name>/<action_name>'>,)
    >>> myparser.parse_string("endpoint_style: lower_camel_case\\ncontroller_style: upper_camel_case\\nendpoint: <controller_name>/<action_name>").elements
    (<REPEAT><'endpoint_style: lower_camel_case', 'controller_style: upper_camel_case', 'endpoint: <controller_name>/<action_name>'>,)
    """

    grammar = m.REPEAT(ControllerStyleConvention | EndpointStyleConvention | EndpointConvention)#, sep=m.BOL)

# endpoint {
#     controller_style: upper_camel_case
#     endpoint_style: lower_camel_case
#     endpoint: <controller_name>/<action_name>
# }
class EndpointConventionGrammar (m.Grammar):
    """
    >>> myparser = EndpointConventionGrammar.parser()
    >>> myparser.parse_string("endpoint {\\ncontroller_style: upper_camel_case\\nendpoint_style: lower_camel_case\\nendpoint: <controller_name>/<action_name>\\n}")
    EndpointConventionGrammar<'endpoint', '{', 'controller_style: upper_camel_case\\nendpoint_style: lower_camel_case\\nendpoint: <controller_name>/<action_name>', '}'>
    """

    grammar = (EndpointKeyword, OpenCurlyBracket, EndpointConventionBody, CloseCurlyBracket)

# Because I've used REPEAT, there could be multiple occurrences of each grammar
# A cleanup phase will have to ensure there is one and only one of each of Structure, Controller, Action, and Endpoint
# structure {
#     app_dir: <app_dir>
#     controllers_dir: controllers
# }
#
# controller {
#     <controller_name>Controller.py
# }
#
# action {
#     def <action_name> (self<A-Za-z0-9_,>):
# }
#
# endpoint {
#     controller_style: upper_camel_case
#     endpoint_style: lower_camel_case
#     endpoint: <controller_name>/<action_name>
# }
class ConventionGrammar (m.Grammar):
    """
    >>> myparser = ConventionGrammar.parser()
    >>> myparser.parse_string("structure {\\ncontrollers_dir: controllers\\napp_dir: <app_dir>}\\n\\ncontroller {\\n<controller_name>Controller.py\\n}\\n\\naction {\\ndef <action_name> (self<A-Za-z0-9_,>):\\n}\\n\\nendpoint {\\ncontroller_style: upper_camel_case\\nendpoint_style: lower_camel_case\\nendpoint: <controller_name>/<action_name>\\n}").elements
    (<REPEAT><'structure {\\ncontrollers_dir: controllers\\napp_dir: <app_dir>}', 'controller {\\n<controller_name>Controller.py\\n}', 'action {\\ndef <action_name> (self<A-Za-z0-9_,>):\\n}', 'endpoint {\\ncontroller_style: upper_camel_case\\nendpoint_style: lower_camel_case\\nendpoint: <controller_name>/<action_name>\\n}'>,)
    >>> myparser.parse_string("controller {\\n<controller_name>Controller.py\\n}\\n\\nstructure {\\ncontrollers_dir: controllers\\napp_dir: <app_dir>}\\n\\naction {\\ndef <action_name> (self<A-Za-z0-9_,>):\\n}\\n\\nendpoint {\\ncontroller_style: upper_camel_case\\nendpoint_style: lower_camel_case\\nendpoint: <controller_name>/<action_name>\\n}").elements
    (<REPEAT><'controller {\\n<controller_name>Controller.py\\n}', 'structure {\\ncontrollers_dir: controllers\\napp_dir: <app_dir>}', 'action {\\ndef <action_name> (self<A-Za-z0-9_,>):\\n}', 'endpoint {\\ncontroller_style: upper_camel_case\\nendpoint_style: lower_camel_case\\nendpoint: <controller_name>/<action_name>\\n}'>,)
    """

    grammar = m.REPEAT(StructureConventionGrammar | ControllerConventionGrammar | ActionConventionGrammar | EndpointConventionGrammar)#, sep=m.BOL)


if __name__ == '__main__':
    import doctest
    doctest.testmod()