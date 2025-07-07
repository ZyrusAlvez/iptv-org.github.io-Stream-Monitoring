from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    # Go to the page
    page.goto("https://iptv-org.github.io/channels/al/3Plus#SD", timeout=60000)

    # Click "Streams" button
    page.click('button[title="Streams"]')

    # Wait for <a> elements to appear
    page.wait_for_selector('a[target="_blank"][rel="noopener noreferrer"]', timeout=10000)

    # Get all matching <a> tags
    links = page.query_selector_all(
        'a[target="_blank"][rel="noopener noreferrer"][class="whitespace-nowrap text-sm hover:text-blue-500 dark:hover:text-blue-400 hover:underline"]'
    )

    for link in links:
        text = link.text_content().strip()
        href = link.get_attribute("href")
        if href and href.endswith(".m3u8"):
            print(f"Text: {text} - UP")
        else:
            print(f"Text: {text} - DOWN")

    browser.close()