import pytest
from playwright.sync_api import sync_playwright

# settings for the test
@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()


@pytest.fixture(scope="session")
def page(browser):
    page = browser.new_page()
    page.goto("https://wordcounter.net/")
    yield page
    page.close()


# Test Data - Real-world examples for each scenario
TEST_SCENARIOS = {
    "short_text": {
        "input": "The quick brown fox jumps over the lazy dog.",
        "expected_words": 9,
        "expected_chars": 44,
        "expected_top_words": [("the", "2"), ("quick", "1"), ("brown", "1")],
    },
    "text_with_bullets": {
        "input": """• First bullet point about testing
        • Second bullet point about quality
        • Third bullet point about testing
        • Fourth bullet point about quality assurance
        """,
        "expected_words": 14,
        "expected_chars": 115,
        "expected_top_words": [("about", "4"), ("bullet", "4"), ("point", "4")],
    },
    "text_with_emojis": {
        "input": "Hello 👋 world! 🌍 Have a great day! ⭐ Keep smiling! 😊",
        "expected_words": 7,
        "expected_chars": 47,
        "expected_top_words": [("have", "1"), ("a", "1"), ("great", "1")],
    },
    "whitespace_only": {
        "input": "         ",
        "expected_words": 0,
        "expected_chars": 9,
        "expected_top_words": [],
    },
    "another_short_text": {
        "input": "This is a test. This test is only a test. What... why if if if",
        "expected_words": 15,
        "expected_chars": 61,
        "expected_top_words": [("test", "3"), ("if", "3"), ("this", "2")],
    },
}


@pytest.mark.parametrize("scenario", TEST_SCENARIOS.values(), ids=TEST_SCENARIOS.keys())
def test_word_count(page, scenario):
    page.fill("#box", scenario["input"])
    page.wait_for_timeout(2000)  # Wait for counters to update

    word_count = page.query_selector("#word_count").inner_text()
    assert word_count == str(
        scenario["expected_words"]
    ), f"Expected {scenario['expected_words']} words, but got {word_count}"


@pytest.mark.parametrize("scenario", TEST_SCENARIOS.values(), ids=TEST_SCENARIOS.keys())
def test_character_count(page, scenario):
    page.fill("#box", scenario["input"])
    page.wait_for_timeout(2000)  # Wait for counters to update

    character_count = page.query_selector("#character_count").inner_text()
    assert character_count == str(
        scenario["expected_chars"]
    ), f"Expected {scenario['expected_chars']} characters, but got {character_count}"


@pytest.mark.parametrize("scenario", TEST_SCENARIOS.values(), ids=TEST_SCENARIOS.keys())
def test_top_words(page, scenario):
    page.fill("#box", scenario["input"])
    page.wait_for_timeout(2000)  # Wait for counters to update

    keyword_density_items = page.query_selector_all(
        "#kwd-accordion-data a.list-group-item"
    )
    top_keywords = []
    for item in keyword_density_items[:3]:
        word = item.query_selector("span.word").inner_text()
        count = item.query_selector("span.badge").inner_text()[0]
        top_keywords.append((word, count))

    assert (
        top_keywords == scenario["expected_top_words"]
    ), f"Expected {scenario['expected_top_words']}, but got {top_keywords}"


@pytest.mark.parametrize("scenario", TEST_SCENARIOS.values(), ids=TEST_SCENARIOS.keys())
def test_word_counter(page, scenario):
    page.fill("#box", scenario["input"])
    page.wait_for_timeout(2000)  # Wait for counters to update

    word_count = page.query_selector("#word_count").inner_text()
    character_count = page.query_selector("#character_count").inner_text()

    assert word_count == str(
        scenario["expected_words"]
    ), f"Expected {scenario['expected_words']} words, but got {word_count}"
    assert character_count == str(
        scenario["expected_chars"]
    ), f"Expected {scenario['expected_chars']} characters, but got {character_count}"

    keyword_density_items = page.query_selector_all(
        "#kwd-accordion-data a.list-group-item"
    )
    top_keywords = []
    for item in keyword_density_items[:3]:
        word = item.query_selector("span.word").inner_text()
        count = item.query_selector("span.badge").inner_text()[0]
        top_keywords.append((word, count))

    assert (
        top_keywords == scenario["expected_top_words"]
    ), f"Expected {scenario['expected_top_words']}, but got {top_keywords}"