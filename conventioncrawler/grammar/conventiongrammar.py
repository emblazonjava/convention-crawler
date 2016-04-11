import modgrammar as m

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
    >>> myparser.parse_string("<action_name")
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
    >>> myparser = AllowedCharsVariable
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
    >>> myparser.parse_string("app_dir: <app_dir>\\ncontrollers_dir: controllers")
    StructureConventionBody<'app_dir: <app_dir>', 'controllers_dir: controllers'>
    """

    grammar = m.REPEAT(AppDirConvention | ControllersDirConvention, max=2)

# structure {
#     app_dir: <app_dir>
#     controllers_dir: controllers
# }
class StructureConventionGrammar (m.Grammar):
    """
    >>> myparser =
    >>> myparser.parse_string("")
    """

    grammar = (StructureKeyword, OpenCurlyBracket, StructureConventionBody, CloseCurlyBracket)

# ControllerConventionGrammar

# controller
class ControllerKeyword (m.Grammar):
    """
    >>> myparser =
    >>> myparser.parse_string("")
    """

    grammar = "controller"

# <controller_name>Controller.py
class ControllerConventionBody (m.Grammar):
    """
    >>> myparser =
    >>> myparser.parse_string("")
    """

    grammar = m.REPEAT(ControllerNameVariable | FileNameConstant)

# controller {
#     <controller_name>Controller.py
# }
class ControllerConventionGrammar (m.Grammar):
    """
    >>> myparser =
    >>> myparser.parse_string("")
    """

    grammar = (ControllerKeyword, OpenCurlyBracket, ControllerConventionBody, CloseCurlyBracket)

# ActionConventionGrammar

# action
class ActionKeyword (m.Grammar):
    """
    >>> myparser =
    >>> myparser.parse_string("")
    """

    grammar = "action"

# def <action_name> (self<A-Za-z0-9_,>):
class ActionConventionBody (m.Grammar):
    """
    >>> myparser =
    >>> myparser.parse_string("")
    """

    grammar = m.REPEAT(ActionNameVariable | LanguageKeywordConstant | Parenthesis | Colon | OpenCurlyBracket)

# action {
#     def <action_name> (self<A-Za-z0-9_,>):
# }
class ActionConventionGrammar (m.Grammar):
    """
    >>> myparser =
    >>> myparser.parse_string("")
    """

    grammar = (ActionKeyword, OpenCurlyBracket, ActionConventionBody, CloseCurlyBracket)

# EndpointConventionGrammar
class EndpointKeyword (m.Grammar):
    """
    >>> myparser =
    >>> myparser.parse_string("")
    """

    grammar = "endpoint"

class CaseStyle (m.Grammar):
    """
    >>> myparser =
    >>> myparser.parse_string("")
    """

    grammar = (m.LITERAL("UpperCamelCase") | m.LITERAL("lowerCamelCase") | m.LITERAL("snake_case"))

class ControllerStyleKeyword (m.Grammar):
    """
    >>> myparser =
    >>> myparser.parse_string("")
    """

    grammar = "controller_style"

class ControllerStyleConvention (m.Grammar):
    """
    >>> myparser =
    >>> myparser.parse_string("")
    """

    grammar = (ControllerStyleKeyword, Colon, CaseStyle)

class EndpointStyleKeyword (m.Grammar):
    """
    >>> myparser =
    >>> myparser.parse_string("")
    """

    grammar = "endpoint_style"

class EndpointStyleConvention (m.Grammar):
    """
    >>> myparser =
    >>> myparser.parse_string("")
    """

    grammar = (EndpointStyleKeyword, Colon, CaseStyle)

class EndpointKeyword (m.Grammar):
    """
    >>> myparser =
    >>> myparser.parse_string("")
    """

    grammar = "endpoint"

class EndpointConvention (m.Grammar):
    """
    >>> myparser =
    >>> myparser.parse_string("")
    """

    grammar = (EndpointKeyword, Colon, m.REPEAT(ControllerNameVariable | ActionNameVariable | m.LITERAL("/")))

# Next Processing phase will ensure one and only one of each
class EndpointConventionBody (m.Grammar):
    """
    >>> myparser =
    >>> myparser.parse_string("")
    """

    grammar = m.REPEAT(ControllerStyleConvention | EndpointStyleConvention | EndpointConvention)

class EndpointConventionGrammar (m.Grammar):
    """
    >>> myparser =
    >>> myparser.parse_string("")
    """

    grammar = (EndpointKeyword, OpenCurlyBracket, EndpointConventionBody, CloseCurlyBracket)

# Because I've used REPEAT, there could be multiple occurrences of each grammar
# A cleanup phase will have to ensure there is one and only one of each of Structure, Controller, Action, and Endpoint
class ConventionGrammar (m.Grammar):
    """
    >>> myparser =
    >>> myparser.parse_string("")
    """

    grammar = m.REPEAT(StructureConventionGrammar | ControllerConventionGrammar | ActionConventionGrammar | EndpointConventionGrammar)


if __name__ == '__main__':
    import doctest
    doctest.testmod()