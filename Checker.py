import requests
from bs4 import BeautifulSoup
from difflib import SequenceMatcher
import time


NORMAL_USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
GOOGLEBOT_USER_AGENT = "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"

def fetch_multiple_versions(url, user_agent, attempts=5):
   
    headers = {'User-Agent': user_agent}
    responses = []

    for _ in range(attempts):
        try:
            response = requests.get(url, headers=headers, timeout=10)
            responses.append(response.text)
            time.sleep(1) 
        except requests.RequestException as e:
            print(f"Error fetching {url}: {e}")
    
    return responses

def clean_html(html_content):

    soup = BeautifulSoup(html_content, 'html.parser')
    
    for tag in soup(['script', 'style', 'meta', 'noscript']):
        tag.decompose()
    
    return soup.get_text(separator=' ', strip=True)

def calculate_average_similarity(pages_a, pages_b):
    
    cleaned_a = [clean_html(page) for page in pages_a]
    cleaned_b = [clean_html(page) for page in pages_b]

    scores = []
    for text_a in cleaned_a:
        for text_b in cleaned_b:
            score = SequenceMatcher(None, text_a, text_b).ratio()
            scores.append(score)
    
    return sum(scores) / len(scores) if scores else 0.0

def detect_seo_cloaking(url):
    
    print(f"🔍 Scanning {url} for SEO cloaking...")

    
    user_versions = fetch_multiple_versions(url, NORMAL_USER_AGENT)
    bot_versions = fetch_multiple_versions(url, GOOGLEBOT_USER_AGENT)

    
    similarity_score = calculate_average_similarity(user_versions, bot_versions)
    print(f"📊 Similarity score: {similarity_score:.2f}")

    
    if similarity_score < 0.85:
        print("⚠️ Possible SEO Cloaking Detected!")
    else:
        print("✅ No cloaking detected.")

if __name__ == "__main__":
   
    target = input("Enter the URL you want to check for cloaking: ").strip()
    detect_seo_cloaking(target)
