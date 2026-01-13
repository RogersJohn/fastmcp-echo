import pytest
from server import echo, word_count


# FastMCP wraps functions in FunctionTool objects, access the underlying function via .fn
echo = echo.fn
word_count = word_count.fn


class TestEcho:
    """Tests for the echo function."""

    # === Positive Tests ===
    def test_echo_basic(self):
        """Test basic echo functionality."""
        assert echo("hello") == "hello"

    def test_echo_upper(self):
        """Test echo with upper parameter."""
        assert echo("hello", upper=True) == "HELLO"

    def test_echo_upper_false(self):
        """Test echo with upper=False."""
        assert echo("Hello World", upper=False) == "Hello World"

    def test_echo_preserves_mixed_case(self):
        """Test that echo preserves mixed case when upper=False."""
        assert echo("HeLLo WoRLd") == "HeLLo WoRLd"

    def test_echo_with_numbers(self):
        """Test echo with numeric characters."""
        assert echo("abc123") == "abc123"

    def test_echo_with_special_characters(self):
        """Test echo with special characters."""
        assert echo("hello!@#$%") == "hello!@#$%"

    def test_echo_upper_with_special_characters(self):
        """Test echo upper with special characters (non-alpha unchanged)."""
        assert echo("hello!@#123", upper=True) == "HELLO!@#123"

    # === Edge Case Tests ===
    def test_echo_empty_string(self):
        """Test echo with empty string."""
        assert echo("") == ""

    def test_echo_empty_string_upper(self):
        """Test echo with empty string and upper."""
        assert echo("", upper=True) == ""

    def test_echo_whitespace_only(self):
        """Test echo with only whitespace."""
        assert echo("   ") == "   "

    def test_echo_newlines_and_tabs(self):
        """Test echo preserves newlines and tabs."""
        assert echo("hello\n\tworld") == "hello\n\tworld"

    def test_echo_unicode(self):
        """Test echo with unicode characters."""
        assert echo("héllo wörld 你好") == "héllo wörld 你好"

    def test_echo_unicode_upper(self):
        """Test echo upper with unicode characters."""
        assert echo("héllo", upper=True) == "HÉLLO"

    def test_echo_very_long_string(self):
        """Test echo with a very long string."""
        long_text = "a" * 10000
        assert echo(long_text) == long_text

    # === Negative Tests ===
    def test_echo_none_raises_error(self):
        """Test that echo raises an error when passed None."""
        with pytest.raises(AttributeError):
            echo(None)

    def test_echo_integer_raises_error(self):
        """Test that echo raises an error when passed an integer."""
        with pytest.raises(AttributeError):
            echo(123)

    def test_echo_list_raises_error(self):
        """Test that echo raises an error when passed a list."""
        with pytest.raises(AttributeError):
            echo(["hello", "world"])


class TestWordCount:
    """Tests for the word_count function."""

    # === Positive Tests ===
    def test_word_count_single_word(self):
        """Test word count with single word."""
        assert word_count("hello") == 1

    def test_word_count_multiple_words(self):
        """Test word count with multiple words."""
        assert word_count("hello world") == 2

    def test_word_count_sentence(self):
        """Test word count with a full sentence."""
        assert word_count("The quick brown fox jumps") == 5

    def test_word_count_with_punctuation(self):
        """Test word count treats punctuation as part of words."""
        assert word_count("hello, world!") == 2

    def test_word_count_with_numbers(self):
        """Test word count with numbers as words."""
        assert word_count("1 2 3 4 5") == 5

    def test_word_count_mixed_content(self):
        """Test word count with mixed letters, numbers, symbols."""
        assert word_count("hello123 world456 test!") == 3

    # === Edge Case Tests ===
    def test_word_count_empty_string(self):
        """Test word count with empty string."""
        assert word_count("") == 0

    def test_word_count_only_spaces(self):
        """Test word count with only spaces."""
        assert word_count("   ") == 0

    def test_word_count_multiple_spaces(self):
        """Test word count with multiple spaces between words."""
        assert word_count("hello  world") == 2

    def test_word_count_leading_trailing_spaces(self):
        """Test word count with leading and trailing spaces."""
        assert word_count("  hello world  ") == 2

    def test_word_count_tabs_as_separators(self):
        """Test word count with tabs as whitespace separators."""
        assert word_count("hello\tworld\ttest") == 3

    def test_word_count_newlines_as_separators(self):
        """Test word count with newlines as whitespace separators."""
        assert word_count("hello\nworld\ntest") == 3

    def test_word_count_mixed_whitespace(self):
        """Test word count with mixed whitespace (spaces, tabs, newlines)."""
        assert word_count("hello \t world \n test") == 3

    def test_word_count_unicode_words(self):
        """Test word count with unicode words."""
        assert word_count("héllo wörld 你好") == 3

    def test_word_count_very_long_text(self):
        """Test word count with many words."""
        text = " ".join(["word"] * 1000)
        assert word_count(text) == 1000

    def test_word_count_single_character_words(self):
        """Test word count with single character words."""
        assert word_count("a b c d e") == 5

    # === Negative Tests ===
    def test_word_count_none_raises_error(self):
        """Test that word_count raises an error when passed None."""
        with pytest.raises(AttributeError):
            word_count(None)

    def test_word_count_integer_raises_error(self):
        """Test that word_count raises an error when passed an integer."""
        with pytest.raises(AttributeError):
            word_count(123)

    def test_word_count_list_raises_error(self):
        """Test that word_count raises an error when passed a list."""
        with pytest.raises(AttributeError):
            word_count(["hello", "world"])
