from crewai.tools import tool
from crewai_tools import SerperDevTool
from playwright.sync_api import sync_playwright
import time
from bs4 import BeautifulSoup

search_tool = SerperDevTool()

@tool
def scrape_tool(url: str) -> str:
    """
    Use this when you need to read the content of a website.
    Returns the content of a website. In case the website is not available, it returns 'No content'.
    Input should be a url string. e.g.,'https://www.cnn.com/2025/11/10/asia/thailand-suspends-peace-accord-cambodia-intl-hnk'
    """
    print(f"Scraping URL: {url}")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page=browser.new_page()
        page.goto(url)
        time.sleep(5)
        html=page.content()
        browser.close()
        soup=BeautifulSoup(html, "html.parser")
        unwanted_tags=["header", "footer", "nav", "aside", "script", "style", "noscript", "iframe", "form", "button", "input", "select", "textarea", "img", "svg", "canvas", "audio", "video", "embed", "object"]
        for tag in soup.find_all(unwanted_tags):
            tag.decompose() #페이지 요소와 그 자식들을 없앰
        content = soup.get_text(separator=" ")
        return content if content != "" else "No content"


