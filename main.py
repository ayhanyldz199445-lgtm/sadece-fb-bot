import feedparser
import random
from datetime import datetime

RSS_LIST = [
    "https://www.fanatik.com.tr/rss/fenerbahce",
    "https://www.fotomac.com.tr/rss/fenerbahce"
]

TEMPLATES = [
    "🚨 FB Gündemi: {t} #Fenerbahçe #FB",
    "💛💙 Sadece Fenerbahçe: {t} #FB",
    "🔥 Flaş FB: {t} #Fenerbahçe",
]

def main():
    haberler = []
    for rss in RSS_LIST:
        try:
            feed = feedparser.parse(rss)
            for e in feed.entries[:3]:
                haberler.append(e.title)
        except:
            pass
    
    if not haberler:
        haberler = ["Fenerbahçe antrenmanda! Samandıra'da neşeler yerinde"]
    
    secilen = random.choice(haberler)
    sablon = random.choice(TEMPLATES)
    tweet = sablon.format(t=secilen[:150])
    
    print(tweet)
    with open("sonuc.txt", "a", encoding="utf-8") as f:
        f.write(f"{datetime.now()} - {tweet}\n")

if __name__ == "__main__":
    main()
