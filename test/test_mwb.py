"""
Test the mediawiki book contents parsing.
"""

import epub.mediawikibook


def test_space():
    """Test the wikibook at test/data/Book_Space.txt"""
    print "Testing wikibook Space"
    filename = "test/data/Book_Space.txt"
    FILE = open(filename, "r")
    text = FILE.read()
    FILE.close()
    info = epub.mediawikibook.parse_mediawiki_book_contents(text)
    assert info['title'] == "Space"
    assert info['author'] == "Wikipedia"
    sections = info['sections']
    return
    print "sections", sections
    assert sections[0] == {'wikisubpage': '/Space/Introduction', 'title': 'Introduction'}
    assert sections[1] == {'wikisubpage': 'Space', 'title': 'Space'}
    assert sections[2] == {'wikisubpage': 'Astronomy', 'title': 'Astronomy'}
    assert sections[3] == {'wikisubpage': 'Theory_of_relativity', 'title': 'Theory of relativity'}
    assert sections[4] == {'wikisubpage': 'Shape_of_the_Universe', 'title': 'Shape of the Universe'}
    assert sections[5] == {'wikisubpage': 'Measurement', 'title': 'Measurement'}


def main():
    """
    Test the parsing of mediawikibook contents pages.
    """

    test_space()


if __name__ == "__main__":
    main()
