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

# Variables

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
    >>> myparser = AppDirConvention.parser({'app_dir': 'retroBrowser'})
    >>> result = myparser.parse_string("app_dir: <app_dir>")
    >>> print (result.elements)
    (AppDirKeyword<'app_dir'>, Colon<':'>, AppDirVariable<'<', 'app_dir', '>'>)
    >>> print (result.app_dir)
    retroBrowser
    """

    grammar = (AppDirKeyword, Colon, AppDirVariable | DirNameConstant)

    def grammar_elem_init(self, sessiondata):

        if isinstance(self[2], AppDirVariable):

            self.app_dir = sessiondata['app_dir']

        elif isinstance(self[2], DirNameConstant):

            self.app_dir = self[2].string

# controllers_dir: controllers
class ControllersDirConvention (m.Grammar):
    """
    >>> myparser = ControllersDirConvention.parser()
    >>> result = myparser.parse_string("controllers_dir: controllers")
    >>> print (result.elements)
    (ControllersDirKeyword<'controllers_dir'>, Colon<':'>, DirNameConstant<'controllers'>)
    >>> print (result.controllers_dir)
    controllers
    """

    grammar = (ControllersDirKeyword, Colon, DirNameConstant)

    def grammar_elem_init(self, sessiondata):

        self.controllers_dir = self[2].string


# Next processing step limits to one of each
# app_dir: <app_dir>
# controllers_dir: controllers
class StructureConventionBody (m.Grammar):
    """
    >>> myparser = StructureConventionBody.parser({'app_dir': 'retroBrowser'})
    >>> myparser.parse_string("app_dir: <app_dir>\\ncontrollers_dir: controllers").elements
    (<REPEAT><'app_dir: <app_dir>', 'controllers_dir: controllers'>,)
    >>> myparser.parse_string("controllers_dir: controllers\\napp_dir: <app_dir>").elements
    (<REPEAT><'controllers_dir: controllers', 'app_dir: <app_dir>'>,)
    """

    grammar = m.REPEAT(AppDirConvention | ControllersDirConvention)#, sep=m.BOL)

# structure {
#     app_dir: <app_dir>
#     controllers_dir: controllers
# }
class StructureConventionGrammar (m.Grammar):
    """
    >>> myparser = StructureConventionGrammar.parser({'app_dir': 'retroBrowser'})
    >>> myparser.parse_string("structure {\\napp_dir: <app_dir>\\ncontrollers_dir: controllers\\n}")
    StructureConventionGrammar<'structure', '{', 'app_dir: <app_dir>\\ncontrollers_dir: controllers', '}'>
    >>> result = myparser.parse_string("structure {\\ncontrollers_dir: controllers\\napp_dir: <app_dir>\\n}")
    >>> print (result.elements)
    (StructureKeyword<'structure'>, OpenCurlyBracket<'{'>, StructureConventionBody<'controllers_dir: controllers\\napp_dir: <app_dir>'>, CloseCurlyBracket<'}'>)
    >>> print (result.app_dir)
    retroBrowser
    >>> print (result.controllers_dir)
    controllers
    """

    grammar = (StructureKeyword, OpenCurlyBracket, StructureConventionBody, CloseCurlyBracket)

    def grammar_elem_init(self, sessiondata):

        self.app_dir = self.find(StructureConventionBody).find(AppDirConvention).app_dir
        self.controllers_dir = self.find(StructureConventionBody).find(ControllersDirConvention).controllers_dir

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
    >>> result = myparser.parse_string("<controller_name>Controller.py")
    >>> print (result.elements)
    (ControllerNameVariable<'<', 'controller_name', '>'>, FileNameConstant<'Controller.py'>)
    >>> print (result.controller_template)
    ['controller_name', 'Controller.py']
    """

    grammar = (ControllerNameVariable, FileNameConstant)

    def grammar_elem_init(self, sessiondata):

        self.controller_template = ['controller_name', self.find(FileNameConstant).string]

# controller {
#     <controller_name>Controller.py
# }
class ControllerConventionGrammar (m.Grammar):
    """
    >>> myparser = ControllerConventionGrammar.parser()
    >>> result = myparser.parse_string("controller {\\n<controller_name>Controller.py\\n}")
    >>> print (result.elements)
    (ControllerKeyword<'controller'>, OpenCurlyBracket<'{'>, ControllerConventionBody<'<controller_name>', 'Controller.py'>, CloseCurlyBracket<'}'>)
    >>> print (result.controller_template)
    ['controller_name', 'Controller.py']
    """

    grammar = (ControllerKeyword, OpenCurlyBracket, ControllerConventionBody, CloseCurlyBracket)

    def grammar_elem_init(self, sessiondata):

        self.controller_template = self.find(ControllerConventionBody).controller_template

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
# def <action_name> (<A-Za-z0-9_,>):
class ActionConventionBody (m.Grammar):
    """
    >>> myparser = ActionConventionBody.parser()
    >>> result = myparser.parse_string("def <action_name> (<A-Za-z0-9_,>):")
    >>> print (result.elements)
    (LanguageKeywordConstant<'def'>, ActionNameVariable<'<', 'action_name', '>'>, Parenthesis<'('>, AllowedCharsVariable<'<', 'A-Za-z0-9_,', '>'>, Parenthesis<')'>, Colon<':'>)
    >>> print (result.action_grammar)
    (<Grammar: L('def')>, <Grammar: WORD('A-Za-z0-9_')>, <Grammar: L('(')>, <Grammar: WORD('A-Za-z0-9_,')>, <Grammar: L(')')>, <Grammar: L(':')>)
    """

    grammar = (LanguageKeywordConstant, ActionNameVariable, Parenthesis, AllowedCharsVariable, Parenthesis, Colon | OpenCurlyBracket)

    def grammar_elem_init(self, sessiondata):

        allowed_chars_regex = self.get(AllowedCharsVariable)[1].string
        self.action_grammar = (m.LITERAL(self[0].string), m.WORD("A-Za-z0-9_"), m.LITERAL(self[2].string), m.WORD(allowed_chars_regex), m.LITERAL(self[4].string), m.LITERAL(self[5].string))


# action {
#     def <action_name> (<A-Za-z0-9_,>):
# }
class ActionConventionGrammar (m.Grammar):
    """
    >>> myparser = ActionConventionGrammar.parser()
    >>> result = myparser.parse_string("action {\\ndef <action_name> (<A-Za-z0-9_,>):\\n}")
    >>> print (result.elements)
    (ActionKeyword<'action'>, OpenCurlyBracket<'{'>, ActionConventionBody<'def', '<action_name>', '(', '<A-Za-z0-9_,>', ')', ':'>, CloseCurlyBracket<'}'>)
    >>> print (result.action_grammar)
    (<Grammar: L('def')>, <Grammar: WORD('A-Za-z0-9_')>, <Grammar: L('(')>, <Grammar: WORD('A-Za-z0-9_,')>, <Grammar: L(')')>, <Grammar: L(':')>)
    """

    grammar = (ActionKeyword, OpenCurlyBracket, ActionConventionBody, CloseCurlyBracket)

    def grammar_elem_init(self, sessiondata):

        self.action_grammar = self.find(ActionConventionBody).action_grammar

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
    L('upper_camel_case')<'upper_camel_case'>
    >>> myparser.parse_string("lower_camel_case")
    L('lower_camel_case')<'lower_camel_case'>
    >>> myparser.parse_string('snake_case')
    L('snake_case')<'snake_case'>
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
    >>> result = myparser.parse_string("controller_style: snake_case")
    >>> print (result.elements)
    (ControllerStyleKeyword<'controller_style'>, Colon<':'>, L('snake_case')<'snake_case'>)
    >>> print (result.controller_style)
    CaseStyle.snake_case
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
    >>> result = myparser.parse_string("endpoint_style: lower_camel_case")
    >>> print (result.elements)
    (EndpointStyleKeyword<'endpoint_style'>, Colon<':'>, L('lower_camel_case')<'lower_camel_case'>)
    >>> print (result.endpoint_style)
    CaseStyle.lower_camel_case
    """

    grammar = (EndpointStyleKeyword, Colon, CaseStyle)

    def grammar_elem_init(self, sessiondata):

        self.endpoint_style = ir.CaseStyle[self[2].string]

# <controller_name>/<action_name>
class URLConvention (m.Grammar):
    """
    >>> myparser = URLConvention.parser()
    >>> myparser.parse_string("<controller_name>/<action_name>").elements
    (ControllerNameVariable<'<', 'controller_name', '>'>, L('/')<'/'>, ActionNameVariable<'<', 'action_name', '>'>)
    """

    grammar = m.LIST_OF(ControllerNameVariable | ActionNameVariable, sep="/")
    grammar_collapse = True

# endpoint: <controller_name>/<action_name>
class EndpointConvention (m.Grammar):
    """
    >>> myparser = EndpointConvention.parser()
    >>> result = myparser.parse_string("endpoint: <controller_name>/<action_name>")
    >>> print (result.elements)
    (EndpointKeyword<'endpoint'>, Colon<':'>, <LIST><'<controller_name>', '/', '<action_name>'>)
    >>> print (result.endpoint_template)
    ['controller_name', '/', 'action_name']
    """

    grammar = (EndpointKeyword, Colon, URLConvention)

    def grammar_elem_init(self, sessiondata):

        url_convention = self[2]
        self.endpoint_template = [self._create_template_component(sub_grammar) for sub_grammar in url_convention]


    def _create_template_component(self, sub_grammar):

        if isinstance(sub_grammar, ControllerNameVariable) or isinstance (sub_grammar, ActionNameVariable):

            return sub_grammar.elements[1].string

        else: # it's a separator literal

            return sub_grammar.string



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

    grammar = m.REPEAT(ControllerStyleConvention | EndpointStyleConvention | EndpointConvention)


# endpoint {
#     controller_style: upper_camel_case
#     endpoint_style: lower_camel_case
#     endpoint: <controller_name>/<action_name>
# }
class EndpointConventionGrammar (m.Grammar):
    """
    >>> myparser = EndpointConventionGrammar.parser()
    >>> result = myparser.parse_string("endpoint {\\ncontroller_style: upper_camel_case\\nendpoint_style: lower_camel_case\\nendpoint: <controller_name>/<action_name>\\n}")
    >>> print (result.elements)
    (EndpointKeyword<'endpoint'>, OpenCurlyBracket<'{'>, EndpointConventionBody<'controller_style: upper_camel_case\\nendpoint_style: lower_camel_case\\nendpoint: <controller_name>/<action_name>'>, CloseCurlyBracket<'}'>)
    >>> print (result.controller_style)
    CaseStyle.upper_camel_case
    >>> print (result.endpoint_style)
    CaseStyle.lower_camel_case
    >>> print (result.endpoint_template)
    ['controller_name', '/', 'action_name']
    """

    grammar = (EndpointKeyword, OpenCurlyBracket, EndpointConventionBody, CloseCurlyBracket)

    def grammar_elem_init(self, sessiondata):

        self.controller_style = self.find(ControllerStyleConvention).controller_style
        self.endpoint_style = self.find(EndpointStyleConvention).endpoint_style
        self.endpoint_template = self.find(EndpointConvention).endpoint_template

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
#     def <action_name> (<A-Za-z0-9_,>):
# }
#
# endpoint {
#     controller_style: upper_camel_case
#     endpoint_style: lower_camel_case
#     endpoint: <controller_name>/<action_name>
# }
class ConventionGrammar (m.Grammar):
    """
    >>> myparser = ConventionGrammar.parser({'app_dir': 'retroBrowser'})
    >>> result1 = myparser.parse_string("structure {\\ncontrollers_dir: controllers\\napp_dir: <app_dir>}\\n\\ncontroller {\\n<controller_name>Controller.py\\n}\\n\\naction {\\ndef <action_name> (<A-Za-z0-9_,>):\\n}\\n\\nendpoint {\\ncontroller_style: upper_camel_case\\nendpoint_style: lower_camel_case\\nendpoint: <controller_name>/<action_name>\\n}")
    >>> print (result1.elements)
    (<REPEAT><'structure {\\ncontrollers_dir: controllers\\napp_dir: <app_dir>}', 'controller {\\n<controller_name>Controller.py\\n}', 'action {\\ndef <action_name> (<A-Za-z0-9_,>):\\n}', 'endpoint {\\ncontroller_style: upper_camel_case\\nendpoint_style: lower_camel_case\\nendpoint: <controller_name>/<action_name>\\n}'>,)
    >>> print (result1.structure.app_dir)
    retroBrowser
    >>> print (result1.structure.controllers_dir)
    controllers
    >>> print (result1.controller.controller_template)
    ['controller_name', 'Controller.py']
    >>> print (result1.action.action_grammar)
    (<Grammar: L('def')>, <Grammar: WORD('A-Za-z0-9_')>, <Grammar: L('(')>, <Grammar: WORD('A-Za-z0-9_,')>, <Grammar: L(')')>, <Grammar: L(':')>)
    >>> print (result1.endpoint.controller_style)
    CaseStyle.upper_camel_case
    >>> print (result1.endpoint.endpoint_style)
    CaseStyle.lower_camel_case
    >>> print (result1.endpoint.endpoint_template)
    ['controller_name', '/', 'action_name']
    >>> result2 = myparser.parse_string("controller {\\n<controller_name>Controller.py\\n}\\n\\nstructure {\\ncontrollers_dir: controllers\\napp_dir: <app_dir>}\\n\\naction {\\ndef <action_name> (<A-Za-z0-9_,>):\\n}\\n\\nendpoint {\\ncontroller_style: upper_camel_case\\nendpoint_style: lower_camel_case\\nendpoint: <controller_name>/<action_name>\\n}")
    >>> print (result2.elements)
    (<REPEAT><'controller {\\n<controller_name>Controller.py\\n}', 'structure {\\ncontrollers_dir: controllers\\napp_dir: <app_dir>}', 'action {\\ndef <action_name> (<A-Za-z0-9_,>):\\n}', 'endpoint {\\ncontroller_style: upper_camel_case\\nendpoint_style: lower_camel_case\\nendpoint: <controller_name>/<action_name>\\n}'>,)
    >>> print (result2.structure.app_dir)
    retroBrowser
    >>> print (result2.structure.controllers_dir)
    controllers
    >>> print (result2.controller.controller_template)
    ['controller_name', 'Controller.py']
    >>> print (result2.action.action_grammar)
    (<Grammar: L('def')>, <Grammar: WORD('A-Za-z0-9_')>, <Grammar: L('(')>, <Grammar: WORD('A-Za-z0-9_,')>, <Grammar: L(')')>, <Grammar: L(':')>)
    >>> print (result2.endpoint.controller_style)
    CaseStyle.upper_camel_case
    >>> print (result2.endpoint.endpoint_style)
    CaseStyle.lower_camel_case
    >>> print (result2.endpoint.endpoint_template)
    ['controller_name', '/', 'action_name']
    """

    grammar = m.REPEAT(StructureConventionGrammar | ControllerConventionGrammar | ActionConventionGrammar | EndpointConventionGrammar)

    def grammar_elem_init(self, sessiondata):

        self.structure = self.find(StructureConventionGrammar)
        self.controller = self.find(ControllerConventionGrammar)
        self.action = self.find(ActionConventionGrammar)
        self.endpoint = self.find(EndpointConventionGrammar)


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    convention = """
    structure {
        app_dir: <app_dir>
        controllers_dir: controllers
    }

    controller {
        <controller_name>Controller.py
    }

    action {
        def <action_name> (<A-Za-z0-9_,>):
    }

    endpoint {
        controller_style: upper_camel_case
        endpoint_style: lower_camel_case
        endpoint: <controller_name>/<action_name>
    }"""

    myparser = ConventionGrammar.parser({'app_dir': 'retroBrowser'})
    result = myparser.parse_string(convention)
    print (result.endpoint.endpoint_template)