from nose.tools import *
from ex48.lexicon_1 import lexicon_1
from ex48.Sentence import *
from ex48.Sentence import ParseError

def test_peek():
	peek_next = lexicon_1.scan_1("north")
	assert_equal(peek(peek_next), "direction")

def test_match():
	assert_equal(match(lexicon_1.scan_1("north"),"verb"), None)

def test_parse_verb():
	assert_equal(parse_verb(lexicon_1.scan_1("the go")), ("verb","go"))
	assert_equal(parse_verb(lexicon_1.scan_1("the north")), ("verb","go"))

def test_parse_object():
	assert_equal(parse_object(lexicon_1.scan_1("the north")), ("direction","north"))
	assert_equal(parse_object(lexicon_1.scan_1("the princess")), ("noun","princess"))
	assert_equal(parse_object(lexicon_1.scan_1("the go")), ("noun","princess"))

def test_parse_subject():
	parse_subject(lexicon_1.scan_1("go the north"),("noun","princess")).print_sentence()
	Sentence(("noun","princess"), ("verb","go"), ("direction","north")).print_sentence()
	assert_equal(parse_subject(lexicon_1.scan_1("go the north"),("noun","princess")).subject, Sentence(("noun","princess"), ("verb","go"), ("direction","north")).subject)
	assert_equal(parse_subject(lexicon_1.scan_1("go the north"),("noun","princess")).verb, Sentence(("noun","princess"), ("verb","go"), ("direction","north")).verb)
	assert_equal(parse_subject(lexicon_1.scan_1("go the north"),("noun","princess")).object, Sentence(("noun","princess"), ("verb","go"),("direction","north")).object)

def test_parse_sentence():
	assert_equal(parse_sentence(lexicon_1.scan_1("princess go the north")).subject, Sentence(("noun","princess"), ("verb","go"), ("direction","north")).subject)
	assert_equal(parse_sentence(lexicon_1.scan_1("princess go the north")).verb, Sentence(("noun","princess"), ("verb","go"), ("direction","north")).verb)
	assert_equal(parse_sentence(lexicon_1.scan_1("princess go the north")).object, Sentence(("noun","princess"), ("verb","go"), ("direction","north")).object)
	assert_equal(parse_sentence(lexicon_1.scan_1("direction princess go the north")).object, Sentence(("noun","princess"), ("verb","go"), ("direction","north")).object)
	

