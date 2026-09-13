# -*- coding: utf-8 -*-
"""Pomi blog üretici: posts.py içindeki içerikten HTML + index + feed üretir."""
import json, html, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from posts import POSTS

OUT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "blog"))
SITE = "https://yakupselimucar.github.io/pomi-legal/"
BLOG = SITE + "blog/"
LOGO = "https://play-lh.googleusercontent.com/WaWFwXR226D_Io_QAYJtJhSvobvVXbsYmC8AEDGRghM6rWmKqVafH-0lv7LazRdnB2Cbn-OiwHuM6Y1K05TnFQ=s512"
IOS = "https://apps.apple.com/tr/app/id6784132034"
ANDROID = "https://play.google.com/store/apps/details?id=com.yakupselimucar.pomi"

BRAND_SVG = """<svg viewBox="0 0 16 16" shape-rendering="crispEdges" aria-hidden="true"><rect x="7" y="2" width="2" height="2" fill="#46C39A"/><rect x="5" y="3" width="6" height="2" fill="#46C39A"/><rect x="3" y="5" width="10" height="8" fill="#27223D"/><rect x="4" y="6" width="8" height="6" fill="#E8455B"/><rect x="5" y="7" width="2" height="1" fill="#FF7A8C"/><rect x="6" y="9" width="1" height="1" fill="#27223D"/><rect x="9" y="9" width="1" height="1" fill="#27223D"/></svg>"""
FAVICON = "data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16' shape-rendering='crispEdges'><rect width='16' height='16' rx='3' fill='%23FBF4E4'/><rect x='7' y='2' width='2' height='2' fill='%2346C39A'/><rect x='5' y='3' width='6' height='2' fill='%2346C39A'/><rect x='3' y='5' width='10' height='8' fill='%2327223D'/><rect x='4' y='6' width='8' height='6' fill='%23E8455B'/><rect x='5' y='7' width='2' height='1' fill='%23FF7A8C'/><rect x='6' y='9' width='1' height='1' fill='%2327223D'/><rect x='9' y='9' width='1' height='1' fill='%2327223D'/></svg>"

T = {
  "tr": dict(skip="İçeriğe geç", home="Ana sayfa", blog="Blog", support="Destek", get="İndir",
             nav_aria="Bölümler", by="Yazan", updated="Güncellendi", read="dk okuma",
             tldr="Kısa cevap", faq="Sık sorulan sorular", related="Diğer yazılar",
             cta_h="Pomi'yi ücretsiz dene", cta_p="Reklamsız, çevrimdışı çalışır. iPhone, iPad ve Android'de.",
             ios="App Store", android="Google Play",
             disclosure="Şeffaflık notu: Bu yazı Pomi'nin geliştiricisi tarafından yazıldı. Diğer uygulamalarla ilgili bilgiler yazının yayımlandığı tarihte herkese açık mağaza sayfalarına dayanır; fiyat ve özellikler değişebilir. Bir hata görürsen <a href=\"mailto:yakupselimucar@hotmail.com\">yaz</a>, düzeltelim.",
             copyright="© 2026 Pomi. Tüm hakları saklıdır.", privacy="Gizlilik", terms="Şartlar",
             other_lang="Read in English", blog_title="Pomi Blog · Odak, Pomodoro ve birlikte çalışma",
             blog_desc="Pomodoro tekniği, odaklanma araçları ve öğrenciler için verimlilik rehberleri. Pomi ekibinden kısa, kaynaklı yazılar.",
             blog_h1="Odak üzerine <span class=\"accent\">kısa yazılar</span>",
             blog_lead="Pomodoro tekniği, odaklanma uygulamaları ve birlikte ders çalışma üzerine rehberler. Süslü sözler yok; denenmiş yöntemler ve dürüst karşılaştırmalar.",
             rss="RSS"),
  "en": dict(skip="Skip to content", home="Home", blog="Blog", support="Support", get="Download",
             nav_aria="Sections", by="By", updated="Updated", read="min read",
             tldr="Short answer", faq="Frequently asked questions", related="More from the blog",
             cta_h="Try Pomi for free", cta_p="No ads, works offline. On iPhone, iPad and Android.",
             ios="App Store", android="Google Play",
             disclosure="Transparency note: This article was written by the developer of Pomi. Information about other apps is based on their public store listings at the time of publishing; prices and features may change. Spotted a mistake? <a href=\"mailto:yakupselimucar@hotmail.com\">Email us</a> and we will fix it.",
             copyright="© 2026 Pomi. All rights reserved.", privacy="Privacy", terms="Terms",
             other_lang="Türkçe oku", blog_title="Pomi Blog · Focus, Pomodoro and studying together",
             blog_desc="Guides on the Pomodoro technique, focus apps and productivity for students. Short, sourced articles from the Pomi team.",
             blog_h1="Short reads on <span class=\"accent\">focus</span>",
             blog_lead="Guides on the Pomodoro technique, focus apps and studying together. No fluff; tested methods and honest comparisons.",
             rss="RSS"),
}

def nav(lang, current):
    t = T[lang]
    return f"""  <a class="skip" href="#main">{t['skip']}</a>
  <header class="nav">
    <div class="wrap">
      <a class="brand" href="../" aria-label="Pomi">{BRAND_SVG}<span>Pomi</span></a>
      <nav class="nav-links" aria-label="{t['nav_aria']}">
        <a href="../">{t['home']}</a>
        <a href="./{'' if lang=='tr' else 'en.html'}"{' aria-current="page"' if current=='blog' else ''}>{t['blog']}</a>
        <a href="../support.html">{t['support']}</a>
      </nav>
      <a class="btn btn-primary btn-sm" href="../#get">{t['get']}</a>
    </div>
  </header>
"""

def footer(lang):
    t = T[lang]
    return f"""  <footer class="site">
    <div class="wrap">
      <span>{t['copyright']}</span>
      <span class="fl">
        <a href="../privacy.html">{t['privacy']}</a>
        <a href="../terms.html">{t['terms']}</a>
        <a href="../support.html">{t['support']}</a>
        <a href="feed.xml">{t['rss']}</a>
        <a href="mailto:yakupselimucar@hotmail.com">yakupselimucar@hotmail.com</a>
      </span>
    </div>
  </footer>
"""

def head_common(title, desc, url, lang, extra=""):
    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{html.escape(title)}</title>
  <meta name="description" content="{html.escape(desc)}" />
  <meta name="theme-color" content="#FDFAF2" />
  <meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1" />
  <link rel="canonical" href="{url}" />
  <link rel="alternate" type="application/rss+xml" title="Pomi Blog" href="{BLOG}feed.xml" />
  <meta property="og:site_name" content="Pomi" />
  <meta property="og:title" content="{html.escape(title)}" />
  <meta property="og:description" content="{html.escape(desc)}" />
  <meta property="og:url" content="{url}" />
  <meta property="og:image" content="{LOGO}" />
  <meta property="og:locale" content="{'tr_TR' if lang=='tr' else 'en_US'}" />
  <meta name="twitter:card" content="summary" />
{extra}  <link rel="icon" href="{FAVICON}" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Pixelify+Sans:wght@400..700&family=DM+Sans:opsz,wght@9..40,400;9..40,500;9..40,600;9..40,700&family=DM+Serif+Display:ital@0;1&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="blog.css" />
"""

def ld(obj):
    return '  <script type="application/ld+json">\n' + json.dumps(obj, ensure_ascii=False, indent=2) + '\n  </script>\n'

def person():
    return {"@type": "Person", "@id": SITE + "#founder", "name": "Yakup Selim Uçar",
            "url": SITE, "jobTitle": "Pomi geliştiricisi"}

def post_page(p, all_posts):
    lang = p["lang"]; t = T[lang]
    url = BLOG + p["slug"] + ".html"
    alt = next((q for q in all_posts if q.get("pair") and q["pair"] == p["slug"]), None)
    extra = f'  <meta property="og:type" content="article" />\n  <meta property="article:published_time" content="{p["date"]}" />\n  <meta property="article:modified_time" content="{p.get("modified", p["date"])}" />\n  <meta property="article:author" content="Yakup Selim Uçar" />\n'
    if alt:
        extra += f'  <link rel="alternate" hreflang="{lang}" href="{url}" />\n  <link rel="alternate" hreflang="{alt["lang"]}" href="{BLOG}{alt["slug"]}.html" />\n  <link rel="alternate" hreflang="x-default" href="{url if lang=="en" else BLOG+alt["slug"]+".html"}" />\n'
    graph = [
        person(),
        {"@type": "BlogPosting", "@id": url + "#article", "mainEntityOfPage": url, "url": url,
         "headline": p["title"], "description": p["desc"], "inLanguage": lang,
         "datePublished": p["date"], "dateModified": p.get("modified", p["date"]),
         "author": {"@id": SITE + "#founder"},
         "publisher": {"@id": SITE + "#organization"},
         "image": LOGO,
         "isPartOf": {"@id": BLOG + "#blog"},
         "about": {"@id": SITE + "#app"},
         "keywords": p["keywords"],
         "wordCount": p.get("words", 0),
         "articleSection": p["section"]},
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Pomi", "item": SITE},
            {"@type": "ListItem", "position": 2, "name": "Blog", "item": BLOG if lang=="tr" else BLOG + "en.html"},
            {"@type": "ListItem", "position": 3, "name": p["title"], "item": url}]},
    ]
    if p.get("faq"):
        graph.append({"@type": "FAQPage", "@id": url + "#faq",
                      "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in p["faq"]]})
    if p.get("itemlist"):
        graph.append({"@type": "ItemList", "@id": url + "#list", "name": p["title"], "numberOfItems": len(p["itemlist"]),
                      "itemListOrder": "https://schema.org/ItemListOrderAscending",
                      "itemListElement": [{"@type": "ListItem", "position": i+1, "name": n, "url": u} for i, (n, u) in enumerate(p["itemlist"])]})
    extra += ld({"@context": "https://schema.org", "@graph": graph})

    faq_html = ""
    if p.get("faq"):
        faq_html = f'<h2 id="faq">{t["faq"]}</h2>\n<div class="faq">\n' + "\n".join(
            f'  <details><summary>{html.escape(q)}</summary><p>{html.escape(a)}</p></details>' for q, a in p["faq"]) + "\n</div>\n"

    related = [q for q in all_posts if q["lang"] == lang and q["slug"] != p["slug"]]
    rel_html = "".join(f'''    <li><a class="post-card" href="{q['slug']}.html"><span class="kicker">{q['section']}</span><h3>{html.escape(q['title'])}</h3><p>{html.escape(q['desc'])}</p></a></li>\n''' for q in related)

    lang_link = f'<a href="{alt["slug"]}.html" hreflang="{alt["lang"]}">{t["other_lang"]}</a>' if alt else ""
    date_h = p["date"]
    body = f"""<body>
{nav(lang, 'blog')}
  <main id="main">
    <header class="article-head">
      <div class="wrap">
        <ol class="breadcrumb" aria-label="Breadcrumb">
          <li><a href="../">Pomi</a></li>
          <li><a href="./{'' if lang=='tr' else 'en.html'}">{t['blog']}</a></li>
          <li aria-current="page">{html.escape(p['short'])}</li>
        </ol>
        <p class="kicker">{p['section']}</p>
        <h1>{p['h1']}</h1>
        <p class="lead">{p['lead']}</p>
        <div class="meta">
          <span class="author">{BRAND_SVG}{t['by']} Yakup Selim Uçar</span>
          <time datetime="{date_h}">{p['date_human']}</time>
          <span>{p['read']} {t['read']}</span>
          {lang_link}
        </div>
      </div>
    </header>

    <article class="article-body">
      <div class="tldr">
        <p class="kicker">{t['tldr']}</p>
        {p['tldr']}
      </div>

{p['body']}

{faq_html}
      <section class="cta">
        <h2>{t['cta_h']}</h2>
        <p>{t['cta_p']}</p>
        <div class="stores">
          <a class="store" href="{IOS}" rel="noopener">{t['ios']}</a>
          <a class="store" href="{ANDROID}" rel="noopener">{t['android']}</a>
        </div>
      </section>

      <p class="disclosure">{t['disclosure']}</p>

      <section class="related">
        <h2>{t['related']}</h2>
        <ul class="post-list">
{rel_html}        </ul>
      </section>
    </article>
  </main>
{footer(lang)}</body>
</html>
"""
    return head_common(p["title"], p["desc"], url, lang, extra) + "</head>\n" + body

def index_page(lang, all_posts):
    t = T[lang]
    url = BLOG if lang == "tr" else BLOG + "en.html"
    other = BLOG + "en.html" if lang == "tr" else BLOG
    posts = [q for q in all_posts if q["lang"] == lang]
    extra = f'  <meta property="og:type" content="website" />\n  <link rel="alternate" hreflang="tr" href="{BLOG}" />\n  <link rel="alternate" hreflang="en" href="{BLOG}en.html" />\n  <link rel="alternate" hreflang="x-default" href="{BLOG}en.html" />\n'
    graph = [person(), {
        "@type": "Blog", "@id": BLOG + "#blog", "url": url, "name": "Pomi Blog",
        "description": t["blog_desc"], "inLanguage": lang,
        "publisher": {"@id": SITE + "#organization"}, "author": {"@id": SITE + "#founder"},
        "isPartOf": {"@id": SITE + "#website"},
        "blogPost": [{"@type": "BlogPosting", "@id": BLOG + q["slug"] + ".html#article", "headline": q["title"], "url": BLOG + q["slug"] + ".html", "datePublished": q["date"], "inLanguage": q["lang"]} for q in posts]},
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Pomi", "item": SITE},
            {"@type": "ListItem", "position": 2, "name": "Blog", "item": url}]}]
    extra += ld({"@context": "https://schema.org", "@graph": graph})
    cards = "".join(f'''      <li><a class="post-card" href="{q['slug']}.html"><span class="kicker">{q['section']}</span><h3>{html.escape(q['title'])}</h3><p>{html.escape(q['desc'])}</p><div class="meta"><time datetime="{q['date']}">{q['date_human']}</time><span>{q['read']} {t['read']}</span></div></a></li>\n''' for q in posts)
    body = f"""<body>
{nav(lang, 'blog')}
  <main id="main">
    <section class="blog-hero">
      <div class="wrap">
        <p class="kicker">Pomi Blog <span class="lang-switch"><a href="{other}" hreflang="{'en' if lang=='tr' else 'tr'}">{t['other_lang']}</a></span></p>
        <h1>{t['blog_h1']}</h1>
        <p>{t['blog_lead']}</p>
      </div>
    </section>
    <section class="wrap">
      <ul class="post-grid">
{cards}      </ul>
    </section>
  </main>
{footer(lang)}</body>
</html>
"""
    return head_common(t["blog_title"], t["blog_desc"], url, lang, extra) + "</head>\n" + body

def feed(all_posts):
    items = "".join(f"""  <item>
    <title>{html.escape(q['title'])}</title>
    <link>{BLOG}{q['slug']}.html</link>
    <guid isPermaLink="true">{BLOG}{q['slug']}.html</guid>
    <pubDate>{q['rfc822']}</pubDate>
    <description>{html.escape(q['desc'])}</description>
    <category>{html.escape(q['section'])}</category>
  </item>
""" for q in sorted(all_posts, key=lambda q: q["date"], reverse=True))
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
<channel>
  <title>Pomi Blog</title>
  <link>{BLOG}</link>
  <atom:link href="{BLOG}feed.xml" rel="self" type="application/rss+xml" />
  <description>Pomodoro tekniği, odaklanma uygulamaları ve birlikte ders çalışma üzerine yazılar. Articles on the Pomodoro technique, focus apps and studying together.</description>
  <language>tr</language>
{items}</channel>
</rss>
"""

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for p in POSTS:
        with open(os.path.join(OUT, p["slug"] + ".html"), "w", encoding="utf-8") as f:
            f.write(post_page(p, POSTS))
    with open(os.path.join(OUT, "index.html"), "w", encoding="utf-8") as f:
        f.write(index_page("tr", POSTS))
    with open(os.path.join(OUT, "en.html"), "w", encoding="utf-8") as f:
        f.write(index_page("en", POSTS))
    with open(os.path.join(OUT, "feed.xml"), "w", encoding="utf-8") as f:
        f.write(feed(POSTS))
    print("built", len(POSTS), "posts")
