import enum

class TokenType(enum.Enum):
	EOF = -1
	NEWLINE = 0
	NUMBER = 1
	IDENT = 2
	STRING = 3

	# Keywords
	PRINT = 103
	INPUT = 104
	VAR = 105
	IF = 106
	THEN = 107
	ENDIF = 108
	WHILE = 109
	ENDWHILE = 111


	# Operators
	EQUALS = 201  
	PLUS = 202
	MINUS = 203
	ASTERISK = 204
	SLASH = 205
	DOUBLE_EQUALS = 206
	NOT_EQUALS = 207
	LESSER_THAN = 208
	LESS_THAN_OR_EQUAL_TO = 209
	GREATER_THAN = 210
	GREATER_THAN_OR_EQUAL_TO = 211