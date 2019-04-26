import requests

def get_mv_title(browser):
    """Return the title text"""
    title = browser.find_element_by_id('video-title')
    return title
    
def get_mv_url(title):
    """Return the url text"""
    return title.get_attribute('href')