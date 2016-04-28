import modgrammar as m

m.grammar_whitespace_mode='optional'

class ActionName (m.Grammar):

    grammar = m.WORD('A-Za-z0-9_')

class GroovyActionGrammar (m.Grammar):

        grammar = (m.LITERAL('def'), ActionName, m.LITERAL('('), m.OPTIONAL(m.REPEAT(m.WORD('A-Za-z0-9_){='))))

class PythonSpecialFunctionName (m.Grammar):

    grammar_whitespace_mode = 'explicit'

    grammar = (m.LITERAL('__'), m.WORD('A-Za-z0-9'), m.LITERAL('__'))

class PythonActionGrammar (m.Grammar):

    grammar = (m.LITERAL('def'), m.EXCEPT(ActionName, PythonSpecialFunctionName), m.LITERAL('('), m.OPTIONAL(m.REPEAT(m.WORD('A-Za-z0-9_):='))))
