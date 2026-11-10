import json, os, html
ROOT='/home/claude/portfolio'
meta=json.load(open(f'{ROOT}/assets/work/meta.json'))

PROJECTS=[
 dict(slug='act', tkey='act', th=19.3, name='Act', title='act', sub='Cloud Security', year='2026', img='card-act', size='s',
      tags=['Brand Identity','UX/UI','Art Direction','Web Design','Concept','AI Visuals'],
      info='Act is a cloud security company built on the belief that lasting security starts at the foundation. Inspired by Act’s core strategy of strong foundations, I developed a visual language imagining Act in ancient Rome — monumental, impossible structures, classical sculptures and contemporary aesthetics. Lead Designer, Brand Identity & Web, created at Guts Agency.'),
 dict(slug='post-nature', tkey='postnature', th=19.3, key='postnature', name='Post Nature', title='Post Nature', sub='Interactive Exhibition', year='2025', img='card-postnature', size='l',
      tags=['Art Direction','UX/UI','Research','AI Design','Concept','Visual Identity','Exhibition'],
      info='Post Nature is a speculative interactive exhibition exploring human intervention in the plant world. Through a physical installation and two digital interfaces, it invites visitors to examine how plants have changed over time and imagine what we might turn them into next. Graduation project, HIT. Mentor: Bob Orel.'),
 dict(slug='panorays', tkey='panorays', th=24.6, name='Panorays', title='panorays', sub='Third-Party Cybersecurity', year='2026', img='card-panorays', size='l',
      tags=['Brand Identity','Illustration','Character Design','Web Design'],
      info='Panorays helps businesses understand and manage cybersecurity risks across their third-party relationships. Built around the idea “Connections that just click,” the brand identity and website translate a complex security world into a bright, approachable experience through expressive illustrations, vibrant gradients, and Pano, the brand’s character. Brand & Digital Designer, created at Guts Agency.'),
 dict(slug='kanopy', tkey='kanopy', th=24.6, name='Kanopy', title='Kanopy', sub='Cybersecurity', year='2025', img='card-kanopy', size='s',
      tags=['Brand Identity','Illustration','Web Design','UX/UI','Concept'],
      info='A bold cybersecurity brand built for the wild world of no-code and AI-powered business apps. Through a hand-crafted illustration system, vibrant identity, and digital experience, we positioned Kanopy as the guide that brings clarity and order to the jungle. Lead Designer, Brand Identity & Web, created at Guts Agency.'),
]
P={p['slug']:p for p in PROJECTS}

def head(title, desc):
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{html.escape(desc)}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:image" content="/assets/img/card-panorays.webp">
<meta name="theme-color" content="#fffdf7">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600;700&family=Instrument+Sans&family=Roboto+Mono:wght@400;600&display=swap" rel="stylesheet">
<link rel="preload" href="/fonts/PerfectlyNineties-Regular.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/fonts/PerfectlyNineties-SemiboldItalic.woff2" as="font" type="font/woff2" crossorigin>
<script>
/* Figma is drawn at 1440px. On wider screens, scale the whole page up so the
   24px side margins and every proportion stay exactly as in the design. */
(function(){{var d=document.documentElement;function f(){{d.style.setProperty('--z',Math.max(1,d.clientWidth/1440));}}f();addEventListener('resize',f);}})();
</script>
<script>
/* Phones: the mobile layout is still being designed, so show a short note instead.
   Add ?preview to the address once to see the real site on a phone (and ?preview=off to undo). */
(function(){{var d=document.documentElement,k='ys-preview',q=location.search,p=false;
try{{if(/[?&]preview=off/.test(q))localStorage.removeItem(k);else if(/[?&]preview/.test(q))localStorage.setItem(k,'1');p=localStorage.getItem(k)==='1';}}catch(e){{p=/[?&]preview(?!=off)/.test(q);}}
if(!p&&matchMedia('(max-width: 760px)').matches)d.classList.add('gate');}})();
</script>
<link rel="stylesheet" href="/css/style.css">
</head>
<body>
<div class="gate-screen" role="dialog" aria-label="Mobile version coming soon">
  <img class="gate-screen__name" src="/assets/svg/footer-name.svg" alt="Yuval Shalmon">
  <p class="gate-screen__title">The mobile version<br>is <em>on its way.</em></p>
  <p class="gate-screen__text">For now, please visit on a computer to see the full portfolio.</p>
  <a class="gate-screen__mail" href="mailto:yuvalshalmon.sk@gmail.com">yuvalshalmon.sk@gmail.com</a>
</div>
'''

def nav(active=''):
    cur=lambda k: ' aria-current="page"' if k==active else ''
    return f'''<nav class="nav" aria-label="Main">
  <div class="nav__left">
    <a class="nav__home" href="/"{cur('home')}>home</a>
    <a class="pill" href="/#works"{cur('works')}>works</a>
    <a class="pill" href="/about/"{cur('about')}>about</a>
    <a class="pill pill--md" href="#playground">Playground</a>
  </div>
  <a class="talk" href="#contact"><span>Let’s talk</span></a>
  <button class="menu-btn" type="button" aria-expanded="false" aria-controls="mnav"><span class="menu-btn__open">menu</span><span class="menu-btn__close">close</span></button>
</nav>
<div class="mnav" id="mnav" aria-label="Menu" hidden>
  <ul class="mnav__list">
    <li><a class="mnav__pill" href="/"{cur('home')}>home</a></li>
    <li><a class="mnav__pill" href="/#works"{cur('works')}>works</a></li>
    <li><a class="mnav__pill" href="/about/"{cur('about')}>about</a></li>
    <li><a class="mnav__pill" href="#playground">playground</a></li>
    <li><a class="mnav__pill mnav__pill--talk" href="#contact">let’s talk</a></li>
  </ul>
  <div class="mnav__foot">
    <img src="/assets/svg/footer-name.svg" width="216" height="32" alt="Yuval Shalmon">
    <p>© 2026 . All rights reserved.</p>
  </div>
</div>
'''

CTA_HOME='''<section class="cta reveal">
  <h2 class="cta__title"><span class="sr-only">Fortune favors the bold.</span><img src="/assets/svg/cta-bold.svg" width="820" height="407" alt=""></h2>
  <a class="cta__btn" href="#contact">Let’s talk</a>
</section>
'''

def footer():
    return '''<footer class="footer" id="contact">
  <div class="footer__brand">
    <p class="footer__name"><img src="/assets/svg/footer-name.svg" width="216" height="32" alt="Yuval Shalmon"></p>
    <p class="footer__copy">© 2026 . All rights reserved.</p>
  </div>
  <div class="footer__cols">
    <div class="footer__col"><h3>Connect</h3><a href="https://www.linkedin.com/in/yuval-shalmon" target="_blank" rel="noopener">LinkedIn</a><a href="https://www.instagram.com/yuval_shalmon/" target="_blank" rel="noopener">Instagram</a></div>
    <div class="footer__col"><h3>Get in touch</h3><a href="mailto:yuvalshalmon.sk@gmail.com">Email</a><a href="tel:+972526084763">+972 52 608 4763</a></div>
    <div class="footer__col"><h3>Locations</h3><span class="clock" data-clock>12:18 PM - IDT</span></div>
  </div>
</footer>
'''
END='<script src="/js/main.js" defer></script>\n</body>\n</html>\n'

# videos on the home-page cards (Figma: video fill over the card image)
CARD_VIDEOS={'post-nature':('/assets/video/postnature/kling.mp4', 0, 683, 683, 'contain'),
             'kanopy':('/assets/video/kanopy/laptop-card.mp4', -12, 427.2, 402, 'cover', -27, 738.3, 684)}
def card_video(p):
    v=CARD_VIDEOS.get(p['slug'])
    if not v: return ''
    src,top,vh,boxh,fit=v[:5]
    lx,vw,bw=(v[5],v[6],v[7]) if len(v)>5 else (0,1,1)
    bg='background:#000;' if fit=='contain' else ''
    return f'<video class="card__video" style="left:{lx/bw*100:.3f}%;width:{vw/bw*100:.3f}%;top:{top/boxh*100:.3f}%;height:{vh/boxh*100:.3f}%;object-fit:{fit};{bg}" src="{src}" muted loop playsinline autoplay preload="metadata"></video>'

def card(p):
    # two rows of tags, split as in the Figma cards
    split={'act':3,'post-nature':3,'panorays':2,'kanopy':2}[p['slug']]
    row=lambda ts: '<span class="tags__row">'+''.join(f'<span class="tag">{x}</span>' for x in ts)+'</span>'
    tags=row(p['tags'][:split])+row(p['tags'][split:])
    w,h=(1368,804) if p['size']=='s' else (1368,1366)
    return f'''<a class="card reveal" href="/work/{p['slug']}/">
        <div class="card__img"><img src="/assets/img/{p['img']}.webp" width="{w//2}" height="{h//2}" alt="{p['name']} project" loading="lazy">{card_video(p)}</div>
        <div class="card__info">
          <h3 class="card__title">{p['name']}</h3>
          <span class="card__year">{p['year']}</span>
          <p class="card__sub">{p['sub']}</p>
          <div class="tags">{tags}</div>
        </div>
      </a>'''

DESC='Yuval Shalmon — brand & UX/UI designer and illustrator, creating visual identities, websites and digital experiences with personality.'

index=head('Yuval Shalmon — Portfolio', DESC)+nav('home')+'<div class=\"page\">\n'+f'''<header class="hero">
  <div class="hero__card" aria-hidden="true"></div>
  <h1 class="sr-only">It’s Shalmon time — Yuval Shalmon, portfolio</h1>
  <img class="hero__its" src="/assets/svg/its.svg" width="284" height="163" alt="">
  <div class="hero__name" data-cycle="300" aria-hidden="true">
    <img src="/assets/svg/shalmon/1.svg" width="872" height="250" alt="" class="is-on">
    <img src="/assets/svg/shalmon/2.svg" width="872" height="246" alt="">
    <img src="/assets/svg/shalmon/3.svg" width="872" height="268" alt="">
    <img src="/assets/svg/shalmon/4.svg" width="872" height="248" alt="">
    <img src="/assets/svg/shalmon/5.svg" width="872" height="255" alt="">
    <img src="/assets/svg/shalmon/6.svg" width="872" height="249" alt="">
  </div>
  <img class="hero__time" src="/assets/svg/time.svg" width="411" height="142" alt="">
  <div class="hero__meta">
    <p class="hero__intro">A brand &amp; UX/UI designer <br>and illustrator, creating visual identities, websites, and digital experiences with personality.</p>
    <p class="hero__portfolio" aria-hidden="true">PORT<span class="serif-i">folio</span></p>
  </div>
</header>

<section class="me">
  <span class="dot" aria-hidden="true"></span>
  <p class="me__text reveal"><span class="me__m" aria-hidden="true">I'm Yuval Shalmon.<br>I'm a brand and digital designer who loves digging into ideas and turning them into visual worlds with a personality of their own.</span><span class="sr-only">I'm Yuval Shalmon. I'm a brand and digital designer who loves digging into ideas and turning them into visual worlds with a personality of their own.</span><img src="/assets/svg/me.svg" width="796" height="187" alt=""></p>
  <span class="dot" aria-hidden="true"></span>
</section>

<section class="works" id="works">
  <div class="works__tab"><img src="/assets/svg/works-tab.svg" alt=""><h2 class="works__title"><img src="/assets/svg/selected-works.svg" width="172" height="24" alt="Selected Works"></h2></div>
  <div class="works__grid">
    <div class="works__col">
      {card(P['act'])}
      {card(P['post-nature'])}
    </div>
    <div class="works__col">
      {card(P['panorays'])}
      {card(P['kanopy'])}
    </div>
  </div>
</section>

<section class="banner-wrap" id="playground">
  <div class="banner reveal">
    <img class="banner__bg" src="/assets/img/banner.webp" width="1241" height="203" alt="" loading="lazy">
    <p class="banner__text">A little bit of <span class="serif-i">everything</span></p>
    <a class="banner__btn" data-magnetic href="#playground">go to Playground</a>
  </div>
</section>

'''+'<div class="endzone">'+CTA_HOME+footer()+'</div>'+'</div>\n'+END

about=head('About — Yuval Shalmon', 'About Yuval Shalmon, a brand and digital designer based in Tel Aviv.')+nav('about')+'<div class=\"page\">\n'+'''<section class="about-hero">
  <h1>A bit of<br>both. <span class="serif-i">All in.</span></h1>
  <div class="about-row">
    <img src="/assets/img/about-1.webp" width="274" height="366" alt="Yuval sitting on a green armchair with a tablet">
    <img src="/assets/img/about-2.webp" width="274" height="366" alt="Yuval standing in front of a plant wall">
    <div class="panel panel--about">
      <h2>About Me</h2>
      <p class="lead">I'm Yuval Shalmon,<br class="m-br"> a brand and digital designer based in Tel Aviv.</p>
      <p>Growing up in a kibbutz in northern Israel, surrounded by open fields, gardens and nature, and later finding my place in the energy of city life, shaped the way I see the world. I draw inspiration from both, always curious to explore new perspectives and find unexpected connections.</p>
      <p>I'm fascinated by people and what makes them unique. I enjoy looking beyond the obvious, noticing the little details that make all the difference, and finding the ideas that give each brand its own character.</p>
    </div>
    <div class="about-side">
      <div class="panel panel--small">
        <h3>Experience</h3>
        <strong>Guts Agency</strong>
        <p>Brand &amp; Digital Designer</p>
        <p class="muted">2025 - Present</p>
        <strong>Rafael Advanced Defense Systems</strong>
        <p>Designer - Branding &amp; Digital Department</p>
        <p class="muted">2023 - 2024</p>
      </div>
      <div class="panel panel--small">
        <h3>Education</h3>
        <strong>HIT - Holon Institute of Technology</strong>
        <p>B.Des, Visual Communication</p>
        <p>Dean's Excellence Certificate</p>
        <p class="muted">2021-2025</p>
      </div>
    </div>
  </div>
</section>

<section class="about-cta">
  <img class="about-cta__bg" src="/assets/img/about-bg.webp" alt="" loading="lazy">
  <div class="cta reveal">
    <h2 class="cta__title"><span class="sr-only">Fortune favors the bold.</span><img src="/assets/svg/cta-bold.svg" width="820" height="407" alt=""></h2>
    <a class="cta__btn cta__btn--dark" href="#contact">Let’s talk</a>
  </div>
'''+footer()+'</section>\n</div>\n'+END

open(f'{ROOT}/index.html','w').write(index)
os.makedirs(f'{ROOT}/about',exist_ok=True); open(f'{ROOT}/about/index.html','w').write(about)


# videos laid over slice-built pages: (clip box x,y,w,h), (video box x,y,w,h), file   — Figma page coords
PAGE_VIDEOS={'kanopy':[
  ((26,1110,682,855),(19,1110,688.7,855),'jungle-logo'),
  ((732,1110,682,855),(732,1110,684,855),'apps'),
  ((26,1989,1390,813),(18,1989,1406,813),'laptop-wide'),
  ((26,8265,682,855),(24,8265,684,855),'tools'),
  ((26,11727.3,682,855),(23.5,11727.3,684,855),'bottom'),
]}
def page_videos(slug,H,W=1440):
    out=''
    for (cx,cy,cw,ch),(vx,vy,vw,vh),f in PAGE_VIDEOS.get(slug,[]):
        out+=(f'\n  <div class="pv" style="left:{cx/W*100:.4f}%;top:{cy/H*100:.4f}%;width:{cw/W*100:.4f}%;height:{ch/H*100:.4f}%">'
              f'<video src="/assets/video/{slug}/{f}.mp4" style="left:{(vx-cx)/cw*100:.3f}%;top:{(vy-cy)/ch*100:.3f}%;width:{vw/cw*100:.3f}%;height:{vh/ch*100:.3f}%" muted loop playsinline autoplay preload="metadata"></video></div>')
    return out
for p in [q for q in PROJECTS if q['slug'] not in ('act','post-nature')]:
    key=p.get('key',p['slug']); m=meta[key]; scale=m['w']/1440
    imgs=[]
    for i,(name,ph) in enumerate(m['parts']):
        w=1440; h=round(ph/scale)
        alt=f"{p['name']} case study" if i==0 else ''
        lazy='' if i<2 else ' loading="lazy"'
        imgs.append(f'  <img src="/assets/work/{name}" width="{w}" height="{h}" alt="{alt}" decoding="async"{lazy}>')
    page=head(f"{p['name']} — Yuval Shalmon", p['info'][:155])+nav('works')+'<div class=\"page\">\n'+f'''<main class="project">
<h1 class="sr-only">{p['name']}</h1>
<p class="sr-only">{html.escape(p['info'])}</p>
<div class="project__stack">
'''+'\n'.join(imgs)+page_videos(p['slug'],sum(round(ph/scale) for _,ph in m['parts']))+'\n</div>\n</main>\n'+'<div class="endzone">'+CTA_HOME+footer()+'</div>'+'</div>\n'+END
    os.makedirs(f"{ROOT}/work/{p['slug']}",exist_ok=True)
    open(f"{ROOT}/work/{p['slug']}/index.html",'w').write(page)
print('built')

# ---------------- Act: real-code case study ----------------
def pct(v, base): return f'{v/base*100:.4f}%'
VID='/home/claude/portfolio/assets/video/act'
def video(name, poster, w, h, cls='tile', style=''):
    """A video slot. Until the .mp4 is in assets/video/act, it shows the poster image."""
    src=f'/assets/video/act/{name}.mp4'
    if os.path.exists(f'{VID}/{name}.mp4'):
        return (f'<video class="{cls}" style="{style}" src="{src}" poster="/assets/act/{poster}.webp" '
                f'width="{w}" height="{h}" muted loop playsinline autoplay preload="metadata"></video>')
    if cls=='tile':
        return f'<img class="tile" src="/assets/act/{poster}.webp" width="{w}" height="{h}" alt="" loading="lazy" data-video="{name}">'
    return ''  # overlay slot: poster is already baked into the tile under it


def frames(prefix, n, w, h, ms, alt='', fit=''):
    """Stack of images that swap every `ms` milliseconds (Figma After-delay loop)."""
    imgs=''.join('<img src="/assets/act/move/%s-%d.webp" width="%d" height="%d" alt="%s"%s%s>' % (prefix,i,w,h,alt if i==1 else '',' class="is-on"' if i==1 else '',' loading="lazy"' if i>1 else '') for i in range(1,n+1))
    return '<div class="tile frames%s" data-cycle="%d" style="aspect-ratio:%s">%s</div>' % (' frames--'+fit if fit else '', ms, '%d/%d' % (w,h), imgs)

def carousel():
    slides=''.join('<img class="relief" src="/assets/act/move/relief-%d.webp" width="655" height="466" alt="%s" loading="lazy">' % (i, 'Marble relief %d' % i) for i in range(1,6))
    return '<div class="relief-carousel" data-carousel>'+slides+'</div>'

def img(name, w, h, alt='', lazy=True):
    return f'<img class="tile" src="/assets/act/{name}.webp" width="{w}" height="{h}" alt="{alt}"{" loading=\"lazy\"" if lazy else ""} decoding="async">'

def overlay(tile_html, vname, poster, tile_box, vid_box, top=None):
    tx,ty,tw,th=tile_box; vx,vy,vw,vh=vid_box
    st=f'left:{pct(vx-tx,tw)};top:{pct(vy-ty,th)};width:{pct(vw,tw)};height:{pct(vh,th)}'
    above=f'<img class="over-top" src="/assets/act/{top}.webp" alt="" loading="lazy">' if top else ''
    return f'<div class="stack">{tile_html}{video(vname,poster,vw,vh,cls="overlay",style=st)}{above}</div>'

p=P['act']
tags=''.join(f'<span class="tag">{t}</span>' for t in p['tags'])
sections=f'''
<section class="case-hero">
  {img('hero',1440,973,'Act brand world — classical statues among clouds under the act logo',lazy=False)}
  <div class="case-info reveal">
    <div class="case-info__title">
      <p class="case-info__num">01</p>
      <h1 class="case-info__name">Act</h1>
      <div class="case-info__tags">{tags}</div>
    </div>
    <div class="case-info__body">
      <p class="case-label">Info</p>
      <div class="case-text">
        <p>Act is a cloud security company built on the belief that lasting security starts at the foundation. Founded by a team with decades of experience in security and critical infrastructure, Act addresses cloud risks at their source rather than simply responding to threats.</p>
        <p>Inspired by Act’s core strategy of strong foundations, we turned to the Roman Empire.</p>
        <p class="gap">As part of my work at Guts Agency, I developed a visual language imagining Act in ancient Rome. Through monumental, impossible structures built on solid foundations, classical sculptures, and contemporary aesthetics, I created a brand universe combining strength, stability, imagination, and innovation.</p>
      </div>
      <div class="case-meta">
        <div><p class="case-label">Role</p><p class="case-role">Lead Designer - Brand Identity &amp; Web<br>Created at Guts Agency</p></div>
        <div><p class="case-label">Year</p><p>2026</p></div>
        <div><p class="case-label">Site</p><p><a class="case-site" href="https://act.security/" target="_blank" rel="noopener">act.security</a></p></div>
      </div>
    </div>
  </div>
</section>

<section class="row row--full reveal row--trim">{overlay(img('s1-laptop',1440,747,'Act website on a laptop resting on a classical pedestal'),'sofi-3','s1-video-poster',(0,1440,1440,747),(438,1601,580,338))}</section>
<section class="row row--2 reveal">{frames('logo',8,684,1064,350,'Act logo in eight materials')}{img('s2-b',684,1064,'Classical statue wrapped in pixel-art vines')}</section>
<section class="row row--full reveal">{img('s3',1440,974,'Act banners hanging between columns of a classical building')}</section>
<section class="row row--grid4 reveal">{img('s4-a',682,855,'Pixel icon set')}<div class="col">{img('s4-b',682,416,'Pixel arrow buttons')}{frames('line',3,682,416,800,'Line illustrations of floating temples')}</div></section>
<section class="row row--inset reveal">{video('mokhan-2','s5-video-poster',1392,662)}</section>
<section class="row row--2 reveal row--swap-m">{overlay(img('s6-a',684,855,'Statues holding a tablet showing the Act website'),'screen-recording-a','s6-a-video-poster',(24,5863,684,855),(257,6171,257,185))}{overlay(img('s6-b',684,855,'How Act secures your cloud — product page'),'screen-recording-b','s6-b-video-poster',(732,5863,684,855),(766,6150,617,277),top='s6-b-clouds')}</section>
<section class="row row--2 reveal">{img('s7-a',684,855,'Act cloud map illustration on a laptop')}{img('s7-b',684,855,'Great empires don’t burn easily — matchbox poster')}</section>
<section class="row row--full relief-row reveal">{carousel()}</section>
<section class="row row--type reveal">{img('s9-a',507,622,'PP Mori typeface specimen')}{img('s9-b',855,622,'Act colour palette')}</section>
<section class="row row--2 reveal">{img('s10-a',684,855,'Cyclist carrying an Act tote bag')}{img('s10-b',684,855,'Director of Applying Anyway cap')}</section>
<section class="row row--inset reveal">{video('telefon-1','s11-video-poster',1392,820)}</section>
<section class="row row--2 reveal">{img('s12-a',684,855,'Statue reading an Act newspaper ad')}{frames('slide',6,686,921,500,'Marble statues among pastel clouds',fit='cover')}</section>
<section class="row row--2 row--sq reveal">{img('s13-a',682,682,'Act sticker sheet')}{img('s13-b',682,682,'IAM-not-yolo-ing-this tote bag')}</section>
<section class="row row--full reveal">{img('s14',1440,810,'Stay classic. — floating temples in a blue sky')}</section>
'''
page=head('Act — Yuval Shalmon', p['info'][:155])+nav('works')+'<div class=\"page\">\n'+'<main class="case case--act">'+sections+'</main>\n'+'<div class="endzone">'+CTA_HOME+footer()+'</div>'+'</div>\n'+END
open(f"{ROOT}/work/act/index.html",'w').write(page)
print('act rebuilt')

# ---------------- Post Nature: real-code case study ----------------
PNV='/home/claude/portfolio/assets/video/postnature'
def pimg(name,w,h,alt='',lazy=True,cls='tile'):
    return f'<img class="{cls}" src="/assets/pn/{name}.webp" width="{w}" height="{h}" alt="{alt}"{" loading=\"lazy\"" if lazy else ""} decoding="async">'
def pvid(name,tile_box,vid_box):
    """Video laid over a tile at its Figma position (clipped by the tile)."""
    if not os.path.exists(f'{PNV}/{name}.mp4'): return ''   # not uploaded yet: the tile image shows its still
    tx,ty,tw,th=tile_box; vx,vy,vw,vh=vid_box
    st=f'left:{pct(vx-tx,tw)};top:{pct(vy-ty,th)};width:{pct(vw,tw)};height:{pct(vh,th)}'
    return f'<video class="overlay" style="{st}" src="/assets/video/postnature/{name}.mp4" muted loop playsinline autoplay preload="metadata"></video>'
def ptile(name,box,alt='',vids=(),cls='tile'):
    x,y,w,h=box
    return f'<div class="stack clip">{pimg(name,w,h,alt,cls=cls)}'+''.join(pvid(n,box,vb) for n,vb in vids)+'</div>'
def pcrop(name,tile_box,crop,alt='',vids=()):
    """Phone-only crop of a tile (with its videos) so one part of a wide composition can fill the screen."""
    tx,ty,tw,th=tile_box; cx,cy,cw,ch=crop
    st=f'position:absolute;left:{-(cx-tx)/cw*100:.4f}%;top:{-(cy-ty)/ch*100:.4f}%;width:{tw/cw*100:.4f}%;height:{th/ch*100:.4f}%'
    inner=f'<img class="tile" src="/assets/pn/{name}.webp" alt="{alt}" loading="lazy" decoding="async" style="position:absolute;inset:0;width:100%;height:100%;border-radius:0">'+''.join(pvid(n,tile_box,vb) for n,vb in vids)
    return f'<div class="stack clip pcrop" style="aspect-ratio:{cw}/{ch}"><div style="{st}">{inner}</div></div>'
def flow_m():
    """Phone: the Custom Hybridization user flow rebuilt as one vertical column (same content as the Figma diagram)."""
    A='<i class="fl-a"></i>'
    def node(n,t): return f'<div class="fl-node"><b>{n}</b> {t}</div>'
    def pill(t,c=''): return f'<span class="fl-pill {c}">{t}</span>'
    def step(n,t,note,q,act,warn,nxt):
        return (f'<div class="fl-step">{node(n,t)}<p class="fl-note">{note}</p>{A}<div class="fl-q">{q}</div>{A}'
                f'<div class="fl-yn"><div class="fl-yes">{pill("Yes, continue")}</div><div class="fl-no">{pill("No, finish")}<span class="fl-skip">to 07 Final hybrid</span></div></div>'
                f'<div class="fl-branch">{A}<div class="fl-box">{act}</div>{A}<div class="fl-warn"><span>Warning</span>{warn}</div>{A}'
                f'<div class="fl-row">{pill("Continue")}<span class="fl-next">Next: {nxt}</span></div></div></div>')
    return ('<div class="flow-m">'
      '<p class="flow-m__cap"><i>Diagram Caption</i> – Custom Hybridization User Flow</p>'
      '<h4 class="fl-h">01 / Choose the parent varieties</h4>'
      f'{node("01","Opening screen")}{A}<div class="fl-row fl-row--c">{pill("Start")}</div>{A}'
      f'{node("02","Variety catalog")}{A}<div class="fl-box">Select exactly two varieties</div>{A}<div class="fl-row fl-row--c">{pill("Continue")}</div>{A}'
      '<div class="fl-box fl-box--dash">Generate initial hybrid</div><p class="fl-note fl-note--c">The two selected varieties form the starting hybrid.</p>'
      '<h4 class="fl-h">02 / Shape the hybrid</h4>'
      + step('03','Aesthetics','Preview the initial hybrid.','Give the hybrid a more refined, striking appearance?','Apply aesthetic changes','Natural plant mechanisms are disrupted.','04 / Functionality')
      + step('04','Functionality','Preview the hybrid with changes so far.','Add smart capabilities and advanced functions?','Add advanced functions','Genetic changes prevent natural pollination.','05 / Uniqueness')
      + step('05','Uniqueness','Preview the hybrid with changes so far.','Make the variety more distinctive and give it unusual traits?','Add distinctive traits','The result is an engineered organism rather than a natural plant.','06 / Final fusion')
      + step('06','Final fusion','Preview the hybrid with changes so far.','Combine all the traits into one final version?','Merge the selected traits','The final hybrid is fully artificial and human-designed.','07 / Final hybrid')
      + '<p class="fl-note fl-note--c fl-note--dash">“No, finish” ends the enhancement sequence with the current hybrid.</p>'
      '<h4 class="fl-h">03 / Name it and take it with you</h4>'
      f'{node("07","Final hybrid")}<p class="fl-text">Review the result of the choices made. No additional trait is required to finish.</p>{A}'
      f'{node("08","Name the variety")}{A}<div class="fl-box">Enter a custom name</div>{A}<div class="fl-row fl-row--c">{pill("Continue")}</div>{A}'
      f'{node("09","Hybrid profile + QR code")}<p class="fl-text">View the profile, interventions and impact. Scan the code to open it on your phone.</p>{A}'
      '<div class="fl-row fl-row--c"><span class="fl-box fl-box--sm">Scan QR code</span></div>'
      '</div>')
def gap(px): return f' style="margin-top:calc({px} * var(--u))"'


# ---- Post Nature: live section headings (lettering = sharp SVG from Figma, copy = live Geist text)
def U(v): return f'calc({v} * var(--u))'
def svgimg(name,w,h,alt='',cls='',d='pn'):
    return f'<img class="{cls}" src="/assets/{d}/svg/{name}.svg" width="{w}" height="{h}" alt="{alt}" style="width:{U(w)}">'
def phead(k,label,title,th,body,top=0,d='pn',h=None):
    st=f' style="min-height:{U(h)}"' if h else ''
    return (f'<div class="pn-head"{st}>'
            f'<div class="pn-head__l"><p class="pn-head__label">{svgimg(k+"-label",146,16,label,d=d)}</p>'
            f'<h2 class="pn-head__title">{svgimg(k+"-title",698,th,title.replace("⏎"," "),d=d)}</h2></div>'
            f'<div class="pn-head__body">{body}</div></div>')

# ---- Plant Profile: sunflower video + callouts whose leader lines grow out of the screen
PP_H=855
PP_CALLOUTS=[  # (card x,y,w,h), title svg (w,h), description, leader points (screen end first)
 ((111,304,200,73),'c1',(109,12),'Places the selected stage at a specific point in the plant’s history.',[(531.5,271),(220.6,271),(201,304.3)]),
 ((254,387,200,76),'c2',(90,14),'Shows how the number of plant varieties changes over time.',[(528,354),(373.6,354),(354,387.3)]),
 ((111,593,200,73),'c3',(100,15),'Five markers highlight key changes in the plant’s structure.',[(531.5,698.3),(220.6,698.3),(201,665)]),
 ((1062,666,200,73),'c4',(64,12),'Navigate five research-based stages and two speculative futures.',[(859,772.3),(1144.8,772.3),(1164.4,739)]),
 ((1062,231,200,75),'c5',(99,15),'Displays the plant’s common and scientific names.',[(895,339.3),(1144.8,339.3),(1164.4,306)]),
 ((1128,376,200,75),'c6',(113,15),'The plant visualization changes with each stage.',[(854,485.3),(1219.3,485.3),(1238.9,452)]),
 ((1128,521,200,75),'c7',(96,12),'Explore additional information about the variety and its transformation.',[(904.5,626.3),(1219.3,626.3),(1238.9,593)]),
]
DW=[180,172,178,188,165,165,188]
TITLES=['01 Historical Context','02 Variety Count','03 Visible Changes','04 Timeline','05 Variety Identity','06 Plant Appearance','07 Further Details']
# Callouts scaled up to the stage cards' type (title 20 / body 14, Figma 490:183857), anchored where the leader meets the card
PP_K=1  # cards stay at Figma size; type set to title 14 / body 10 in CSS
def _pp_scaled():
    out=[]
    for i,((x,y,w,h),svg,ss,desc,pts) in enumerate(PP_CALLOUTS):
        pts=list(pts); ax,ay=pts[-1]; W2,H2=w*PP_K,h*PP_K
        nx=ax-(ax-x)*PP_K
        ny=y if abs(ay-y)<abs(ay-(y+h)) else ay-H2
        if i==1 and PP_K>1:  # 02 sits under 01; push it down so the larger cards keep a 10px gap
            ny=304+73*PP_K+10; pts=[pts[0],(ax+33*(ny-pts[0][1])/56.0*0+ (ny-pts[0][1])*19.6/33.3,pts[0][1]),(ax,ny)]
        out.append(((nx,ny,W2,H2),svg,ss,desc,pts))
    return out
def _pp_hotspots():
    """Phone: tap points on the profile screen; each opens its callout card below with a line to the spot."""
    out=''
    for i,((x,y,w,h),svg,ss,desc,pts) in enumerate(PP_CALLOUTS):
        u,v=(pts[0][0]-524)/393,(pts[0][1]-185)/648
        side='l' if x<524 else 'r'
        out+=(f'<button class="ppm-dot ppm-dot--{side}" type="button" data-i="{i}" data-u="{u:.4f}" data-v="{v:.4f}" data-svg="{svg}" data-w="{ss[0]}" data-d="{html.escape(desc)}" '
              f'style="top:{v*100:.3f}%" aria-label="{TITLES[i]}"><span></span></button>')
    return out
def plant_profile():
    W=1440
    cards=''
    for i,((x,y,w,h),svg,(sw,sh),desc,pts) in enumerate(_pp_scaled()):
        cards+=(f'<div class="pp-card" style="--i:{i};left:{pct(x,W)};top:{pct(y,PP_H)};width:{pct(w,W)};height:{pct(h,PP_H)}">'
                f'<img src="/assets/pn/svg/{svg}.svg" alt="{TITLES[i]}" style="width:{U(round(sw*14/14.1529,2))}"><p style="width:{U(round(DW[i]*PP_K,1))}">{desc}</p></div>')
    groups=''.join(f'<g style="--i:{i}"><polyline class="lead" pathLength="1" points="{" ".join(f"{x},{y}" for x,y in c[4])}"/><circle class="lead-dot" cx="{c[4][0][0]}" cy="{c[4][0][1]}" r="2"/></g>' for i,c in enumerate(_pp_scaled()))
    return (f'<div class="pp" data-pp>'
            f'<div class="pp__intro"><h3>{svgimg("pp-title",221,40,"Plant Profile")}</h3>'
            f'<p>Each profile brings together the plant’s identity, history, visual transformation and stage-specific information in a single view.</p></div>'
            f'<svg class="pp__lines" viewBox="0 0 {W} {PP_H}" preserveAspectRatio="none" aria-hidden="true">{groups}</svg>'
            f'<div class="pp__screen" style="left:{pct(524,W)};top:{pct(185,PP_H)};width:{pct(393,W)};height:{pct(648,PP_H)}">'
            f'<video class="pp__video" src="/assets/video/postnature/sunflower.mp4" muted loop playsinline autoplay preload="metadata" aria-label="Sunflower plant profile, moving through its stages"></video>'
            f'{_pp_hotspots()}</div>'
            f'{cards}<div class="ppm-card" aria-live="polite"><img alt=""><p></p></div><svg class="ppm-line" aria-hidden="true"><polyline points=""/></svg></div>'
            f'<div class="pp__stages pan" data-pan>{pimg("s7b",1394,604,"The seven stages of the sunflower, from 2600 BCE to two speculative futures")}</div><p class="pan-hint">Swipe to explore</p>')

# ---- 10 plants carousel (placeholders until the ten videos arrive)
PLANTS=[('sunflower','Sunflower'),('rose','Rose'),('iris','Iris'),('orchid','Orchid'),('tulip','Tulip'),
        ('chrysanthemum','Chrysanthemum'),('narcissus','Narcissus'),('carnation','Carnation'),('buttercup','Buttercup'),('delphinium','Delphinium')]
PC_SHAPE="M0.5 7.86V49.14A2.3 2.3 0 0 0 2.8 51.44A2.3 2.3 0 0 1 5.08 53.75V53.97A2.5 2.5 0 0 0 7.58 56.49H49.45A2.5 2.5 0 0 0 51.95 53.97V53.73A2.3 2.3 0 0 1 54.22 51.44A2.3 2.3 0 0 0 56.49 49.15V7.85A2.3 2.3 0 0 0 54.22 5.56A2.3 2.3 0 0 1 51.95 3.27V3.03A2.5 2.5 0 0 0 49.45 0.51H7.58A2.5 2.5 0 0 0 5.08 3.03V3.25A2.3 2.3 0 0 1 2.8 5.56A2.3 2.3 0 0 0 0.5 7.86Z"
PC_ARROW="M34.8333 19.2C33.083 19.2 31.6667 20.5865 31.6667 22.3C31.6667 24.0135 30.2503 25.4 28.5 25.4C26.7497 25.4 25.3333 26.7865 25.3333 28.5C25.3333 30.2135 26.7497 31.6 28.5 31.6C30.2503 31.6 31.6667 32.9865 31.6667 34.7C31.6667 36.4135 33.083 37.8 34.8333 37.8C36.5836 37.8 38 39.1865 38 40.9C38 42.6135 36.5836 44 34.8333 44C33.083 44 31.6667 42.6135 31.6667 40.9C31.6667 39.1865 30.2503 37.8 28.5 37.8C26.7497 37.8 25.3333 36.4135 25.3333 34.7C25.3333 32.9865 23.917 31.6 22.1667 31.6C20.4164 31.6 19 30.2135 19 28.5C19 26.7865 20.4164 25.4 22.1667 25.4C23.917 25.4 25.3333 24.0135 25.3333 22.3C25.3333 20.5865 26.7497 19.2 28.5 19.2C30.2503 19.2 31.6667 17.8135 31.6667 16.1C31.6667 14.3865 33.083 13 34.8333 13C36.5836 13 38 14.3865 38 16.1C38 17.8135 36.5836 19.2 34.8333 19.2Z"
PC_BTN_L=f'<svg viewBox="0 0 57 57" aria-hidden="true"><path class="pc__bg" d="{PC_SHAPE}"/><path class="pc__arrow" d="{PC_ARROW}"/></svg>'
PC_BTN_R=f'<svg viewBox="0 0 57 57" aria-hidden="true"><path class="pc__bg" d="{PC_SHAPE}"/><path class="pc__arrow" transform="translate(57 0) scale(-1 1)" d="{PC_ARROW}"/></svg>'
PC_X="M41.833 13C43.5832 13 44.9998 14.3863 45 16.0996C45 17.7596 43.6706 19.1135 41.9961 19.1963L41.6699 19.2041C39.9958 19.2872 38.6671 20.6401 38.667 22.2998C38.667 24.0133 37.2503 25.4004 35.5 25.4004C33.7497 25.4004 32.333 26.7865 32.333 28.5C32.333 30.2135 33.7497 31.5996 35.5 31.5996C37.2503 31.5996 38.667 32.9867 38.667 34.7002C38.6671 36.3599 39.9958 37.7128 41.6699 37.7959L41.9961 37.8037C43.6706 37.8865 45 39.2404 45 40.9004C44.9998 42.6137 43.5832 44 41.833 44C40.083 43.9998 38.6672 42.6136 38.667 40.9004C38.667 39.2405 37.3375 37.8867 35.6631 37.8037L35.3369 37.7959C33.6626 37.7129 32.3331 36.36 32.333 34.7002C32.333 32.9868 30.9171 31.5998 29.167 31.5996C29.1111 31.5996 29.0552 31.5975 29 31.5947C28.9448 31.5975 28.8889 31.5996 28.833 31.5996C27.0829 31.5998 25.667 32.9868 25.667 34.7002C25.6669 36.36 24.3374 37.7129 22.6631 37.7959L22.3369 37.8037C20.6625 37.8867 19.333 39.2405 19.333 40.9004C19.3328 42.6136 17.917 43.9998 16.167 44C14.4168 44 13.0002 42.6137 13 40.9004C13 39.2404 14.3294 37.8865 16.0039 37.8037L16.3301 37.7959C18.0042 37.7128 19.3329 36.3599 19.333 34.7002C19.333 32.9867 20.7497 31.5996 22.5 31.5996C24.2503 31.5996 25.667 30.2135 25.667 28.5C25.667 26.7865 24.2503 25.4004 22.5 25.4004C20.7497 25.4004 19.333 24.0133 19.333 22.2998C19.3329 20.6401 18.0042 19.2872 16.3301 19.2041L16.0039 19.1963C14.3294 19.1135 13 17.7596 13 16.0996C13.0002 14.3863 14.4168 13 16.167 13C17.917 13.0002 19.3328 14.3864 19.333 16.0996C19.333 17.7595 20.6625 19.1133 22.3369 19.1963L22.6631 19.2041C24.3374 19.2871 25.6669 20.64 25.667 22.2998C25.667 24.0132 27.0829 25.4002 28.833 25.4004C28.8876 25.4004 28.9422 25.4016 28.9961 25.4043H29.0039C29.0578 25.4016 29.1124 25.4004 29.167 25.4004C30.9171 25.4002 32.333 24.0132 32.333 22.2998C32.3331 20.64 33.6626 19.2871 35.3369 19.2041L35.6631 19.1963C37.3375 19.1133 38.667 17.7595 38.667 16.0996C38.6672 14.3864 40.083 13.0002 41.833 13Z"
PC_CLOSE=f'<svg viewBox="0 0 57 57" aria-hidden="true"><path class="pc__bg" d="{PC_SHAPE}"/><path class="pc__arrow" d="{PC_X}" transform="translate(-0.5 0)"/></svg>'
def _dots():
    n,step=10,17
    W=10+step*(n-1)
    cx=[5+i*step for i in range(n)]
    outer=''.join(f'<circle cx="{x}" cy="5" r="5"/>' for x in cx)+f'<rect x="5" y="3.75" width="{W-10}" height="2.5"/>'
    inner=''.join(f'<circle cx="{x}" cy="5" r="4.15"/>' for x in cx)+f'<rect x="5" y="4.5" width="{W-10}" height="1"/>'
    hits=''.join(f'<button class="pc__dot" type="button" role="tab" data-i="{i}" aria-label="{PLANTS[i][1]}" style="left:{(x-5)/W*100:.3f}%;width:{10/W*100:.3f}%"></button>' for i,x in enumerate(cx))
    return (f'<svg class="pc__chain" viewBox="0 0 {W} 10" aria-hidden="true"><g class="o">{outer}</g><g class="i">{inner}</g>'
            f'<circle class="pc__cur" cx="5" cy="5" r="5"/></svg>{hits}')
def plants():
    PC_DOTS=_dots()
    slides=''.join(f'<button class="pc__slide" type="button" data-i="{i}" data-name="{n}" aria-label="{n}: seven stages — open larger">'
                   f'<video src="/assets/video/postnature/plants/{k}.mp4" poster="/assets/pn/plants/{k}.webp" muted loop playsinline preload="none"></video></button>' for i,(k,n) in enumerate(PLANTS))
    return (f'<div class="pc-intro"><h3>{svgimg("plants-title",437,51,"10 Plants. 7 Stages Each.")}</h3><p>Select a plant to explore its transformation</p></div>'
            f'<div class="pc" data-plants><div class="pc__track">{slides}</div>'
            f'<button class="pc__btn pc__btn--prev" type="button" data-dir="-1" aria-label="Previous plant">{PC_BTN_L}</button>'
            f'<button class="pc__btn pc__btn--next" type="button" data-dir="1" aria-label="Next plant">{PC_BTN_R}</button>'
            f'<div class="pc__dots" role="tablist" aria-label="Choose a plant">{PC_DOTS}</div></div>'
            f'<div class="pc-lightbox" hidden><div class="pc-lightbox__box"></div><button class="pc-lightbox__close" type="button" aria-label="Close">{PC_CLOSE}</button></div>')

# ---- Interface 02: storyboard callouts synced to the video's timeline
SB=[ # title, text, card (x,y,w,h), leader (screen end first), show from, to (seconds) — Figma storyboard coords; times read from the video itself
 ('Start creating','Tap to create a new hybrid.',(208,340,250,87),[(700,447),(333,447),(333,427)],0.3,2.0),
 ('Choose two varieties','Explore the futuristic plant varieties.',(208,188,250,87),[(580,168),(333,168),(333,188)],2.7,4.9),
 ('Select your pair','Drag two varieties into the selection area.',(1020,365,250,102),[(745,487),(1145,487),(1145,467)],5.0,7.0),
 ('Continue','Confirm your pair to generate a hybrid.',(130,434,299,87),[(670,541),(279.5,541),(279.5,521)],7.0,8.2),
 ('Generating your hybrid','The system combines your two selections.',(208,318,250,102),[(650,440),(333,440),(333,420)],8.5,11.8),
 ('Your first hybrid','The selected varieties combine into a new plant.',(208,182,250,102),[(640,304),(333,304),(333,284)],12.1,14.9),
 ('Track your progress','Follow the stages of creating your hybrid.',(1020,138,250,102),[(833,118),(1145,118),(1145,138)],12.6,14.9),
 ('A choice has consequences','Refining its form too far will make it collapse in the wind.',(1020,183,270,102),[(813,305),(1155,305),(1155,285)],15.1,17.2),
 ('Add functionality','Give the hybrid smart abilities and advanced functions.',(208,367,250,102),[(606,489),(333,489),(333,469)],17.9,20.4),
 ('Continue or finish','Keep this version or add another modification.',(1020,421,250,102),[(790,543),(1145,543),(1145,523)],18.4,20.4),
 ('Function has a cost','A built-in micro-motor makes the plant overheat by day.',(1020,183,270,102),[(813,305),(1155,305),(1155,285)],20.6,23.4),
 ('Make it unique','Give the variety extraordinary, one-of-a-kind traits.',(208,367,250,102),[(606,489),(333,489),(333,469)],24.1,25.4),
 ('Beyond recognition','Its new signals can no longer be read by living systems.',(1020,183,270,102),[(813,305),(1155,305),(1155,285)],25.6,27.4),
 ('Final fusion','Merge every chosen trait into one last version.',(208,367,250,102),[(606,489),(333,489),(333,469)],28.1,29.4),
 ('Full human control','The final process erases its natural traits altogether.',(1020,183,270,102),[(813,305),(1155,305),(1155,285)],29.6,34.9),
 ('Your final hybrid','The result of every choice made along the way.',(208,178,250,102),[(640,300),(333,300),(333,280)],36.8,39.6),
 ('Give it a name','Type a name for the new variety.',(1020,203,250,87),[(830,325),(1145,325),(1145,305)],40.6,51.0),
 ('Take it with you','Scan the QR code to keep your hybrid on your phone.',(208,277,250,102),[(643,257),(333,257),(333,277)],52.4,58.3),
 ('A record of your choices','Every intervention and its ecological impact, listed.',(1020,317,270,102),[(835,439),(1155,439),(1155,419)],53.4,58.3),
]
def storyboard():
    W,H,DX,DY=1440,675,-3,35   # storyboard frame -> page tile offset (screen sits at 561,72 on the page)
    g='';cards=''
    for i,(tt,tx,(x,y,w,h),pts,a,z) in enumerate(SB):
        P=[(px+DX,py+DY) for px,py in pts]
        g+=f'<g data-c="{i}"><polyline class="lead" pathLength="1" points="{" ".join(f"{px},{py}" for px,py in P)}"/><circle class="lead-dot" cx="{P[0][0]}" cy="{P[0][1]}" r="2.5"/></g>'
        U0,V0=(P[0][0]-561)/315,(P[0][1]-72)/549   # where the leader lands, as a fraction of the screen video (phone version)
        cards+=(f'<div class="sb-card" data-c="{i}" data-from="{a}" data-to="{z}" data-u="{U0:.4f}" data-v="{V0:.4f}" style="left:{pct(x+DX,W)};top:{pct(y+DY,H)};width:{pct(w,W)};min-height:{pct(h,H)}">'
                f'<p class="sb-card__t">{tt}</p><p class="sb-card__d">{tx}</p></div>')
    head=(f'<div class="sb-head" style="left:{pct(57,W)};top:{pct(52.5,H)};width:{pct(400,W)}">'
          f'<h3><img src="/assets/pn/svg/sb-title.svg" width="323" height="24" alt="The Hybridization Flow" style="width:{U(323)}"></h3>'
          f'<p>Follow a visitor through the kiosk, from choosing two varieties to taking their hybrid home</p></div>')
    mob='<div class="sbm" aria-hidden="true"><div class="sbm__cap"><p class="sbm__t"></p><p class="sbm__d"></p></div><svg class="sbm__line"><polyline points=""/><circle r="3" cx="-9" cy="-9"/></svg></div>'
    return mob+head+f'<svg class="sb__lines" viewBox="0 0 {W} {H}" preserveAspectRatio="none" aria-hidden="true">{g}</svg>{cards}'

p=P['post-nature']
tags=''.join(f'<span class="tag">{t}</span>' for t in p['tags'])
B=lambda *a:a
pn=f'''
<section class="case-hero">
  {pimg('hero',1440,602,'Post Nature logotype',lazy=False)}
  <div class="case-info case-info--{p['slug']} reveal" style="padding-top:calc(47 * var(--u));padding-bottom:calc(99 * var(--u))">
    <div class="case-info__title">
      <p class="case-info__num">03</p>
      <h1 class="case-info__name">Post Nature</h1>
      <div class="case-info__tags">{tags}</div>
    </div>
    <div class="case-info__body">
      <p class="case-label">Info</p>
      <div class="case-text"><p>Post Nature is a speculative interactive exhibition exploring human intervention in the plant world. Through a physical installation and two digital interfaces, it invites visitors to examine how plants have changed over time - and imagine what we might turn them into next.</p></div>
      <div class="case-meta">
        <div><p class="case-label">Role</p><p>Graduation Project, HIT<br>Mentor: Bob Orel</p></div>
        <div><p class="case-label">Year</p><p>2025</p></div>
      </div>
    </div>
  </div>
</section>
<section class="row row--full reveal"{gap(24)}>{ptile('s1',(0,1110,1440,953),'The Post Nature exhibition space')}</section>
<section class="row row--full reveal"{gap(100)}>{phead('h1','01 Overview','What is nature when we redesign it?',143,'<p>For millennia, humans have cultivated and selectively bred plants to meet practical and aesthetic needs. Today, genetic engineering and DNA editing make that intervention more precise than ever.</p><p><b>Post-Nature</b> questions the logic behind these changes: what we choose to preserve, improve, or eliminate - and what we might lose when nature is redesigned around human desires.</p>')}</section>
<section class="row row--2 reveal"{gap(100)}>{ptile('s2a',(24,2534,684,855),'Archive photo of a gardener with lilacs')}{ptile('s2b',(732,2534,684,855),'Archive photo of a gardener tending pots')}</section>
<section class="row row--full reveal"{gap(100)}>{phead('h2','01 Overview','Inside the Exhibition',132,'<p>The exhibition was designed as a pristine, almost clinical environment, balancing delicate beauty with a subtle sense of unease. At its entrance, four transparent acrylic panels display speculative plant specimens as objects of observation and control. Two light-toned archive screens trace the history of human intervention in plants and imagine where it might lead in the future, while a contrasting dark kiosk invites visitors to create a hybrid of their own.</p>')}</section>
<section class="row row--full reveal d-only"{gap(100)}>{ptile('s3',(0,3860,1440,777),'Archive screens and the hybridization kiosk',[('sahlav',(88,3912,304,501)),('iris',(530,3912,304,501)),('hituch',(1030,3911,328,582))])}</section>
<section class="row row--full reveal m-only">{pcrop('s3',(0,3860,1440,777),(960,3868,470,760),'The hybridization kiosk',[('hituch',(1030,3911,328,582))])}</section>
<section class="row row--full reveal m-only">{pcrop('s3',(0,3860,1440,777),(40,3876,840,690),'The two archive screens',[('sahlav',(88,3912,304,501)),('iris',(530,3912,304,501))])}</section>
<section class="row row--full reveal"{gap(24)}>{ptile('s4',(0,4661,1440,763),'Four acrylic panels with speculative plants')}</section>
<section class="row row--full reveal"{gap(100)}>{phead('h3','03 Interface one','The Hybrid Archive',132,'<p>The archive traces ten plant varieties across seven stages of transformation. The first five are grounded in historical and scientific research, while the final two imagine possible futures. Moving through each plant’s timeline reveals changes in its appearance and characteristics, making the cumulative effects of human intervention visible.</p>')}</section>
<section class="row row--2 reveal"{gap(100)}>{ptile('s5a',(24,5895,684,1014),'Hybrid Archive interface',[('interface-1',(-16,5895,765,1014))])}{ptile('s5b',(731,5895,684,1014),'Delphinium animation in the archive',[('delphinium',(731,5612,685,1354))])}</section>
<section class="row row--2 reveal"{gap(24)}>{ptile('s6a',(25,6933,684,1218),'Archive screen detail')}{ptile('s6b',(732,6933,684,1218),'Archive animation',[('hadash',(732,6933,685,1218))])}</section>
<section class="row row--full reveal"{gap(100)}>{plant_profile()}</section>
<section class="row row--full"{gap(100)}>{plants()}</section>
<section class="row row--full reveal"{gap(100)}>{phead('h4','04 Experience two','Custom Hybridization',143,'<p>Visitors combine two speculative plants and shape their hybrid through choices about appearance, functionality, and unique traits. Every enhancement comes with a warning about its potential ecological cost, even as the experience encourages further modification. As the hybrid becomes increasingly artificial, customization becomes a test of how far we are willing to go to improve nature. At the end, visitors can access their creation on their phones, alongside a record of their choices and their possible environmental consequences.</p>')}</section>
<section class="row row--2 reveal"{gap(100)}>{ptile('s9a',(24,11263,684,1014),'Hybridization kiosk in use',[('comp-1',(24,11203,684,1216))])}{ptile('s9b',(732,11263,684,1014),'Hybrid plant animation',[('kling',(732,11254,686,1032))])}</section>
<section class="row row--full reveal"{gap(24)}><div class="sb-mhead"><h3>The Hybridization Flow</h3><p>Follow a visitor through the kiosk, from choosing two varieties to taking their hybrid home</p></div><div class="stack clip sb" data-sb>{pimg('s10',1440,675,'Hybridization kiosk')}{pvid('interface-2',(0,12301,1440,675),(561,12373,315,549))}{storyboard()}</div></section>
<section class="row row--full reveal"{gap(100)}>{phead('h5','05 UX Process','Designing the Decision Flow',132,'<p>The central UX challenge was to turn a complex decision system into a clear, intuitive experience without losing its critical dimension. The flow was divided into short, optional stages where visitors can preview each modification and decide whether to continue or finalize their hybrid. This structure gives visitors control over the process while gradually revealing the consequences of their choices.</p>')}</section>
<section class="row row--full reveal m-only">{flow_m()}</section>
<section class="row row--full reveal row--pan d-only"{gap(100)}><div class="pan" data-pan>{ptile('s11',(0,13447,1440,1150),'Custom hybridization user flow diagram')}</div><p class="pan-hint">Swipe to explore</p></section>
<section class="row row--full reveal"{gap(100)}>{phead('h6','05 Research & Process','From Research to System',143,'<p>Extensive botanical, historical, and scientific research formed the foundation of Post Nature, organized through research maps and a structured content database. This foundation informed the interactive experiences and guided a broad process of AI-assisted visual exploration, art direction, and image curation, shaping the visual evolution of each plant.</p>')}</section>
<section class="row row--full reveal"{gap(100)}><h3 class="pn-cap pn-cap--research">{svgimg('cap-research',159,23,'Research Mapping')}</h3></section>
<section class="row row--inset reveal"{gap(14)}>{ptile('s12',(24,15137,1392,761),'Research mind map',[('mind-map',(24,15137,1392,761))])}</section>
<section class="row row--full reveal"{gap(100)}><h3 class="pn-cap" style="padding-left:calc(48 * var(--u))">{svgimg('cap-content',376,23,'Content Architecture and Visual Development')}</h3></section>
<section class="row row--inset reveal"{gap(14)}>{ptile('s14',(24,16067,1392,616),'Interface screen recording',[('screen-recording',(24,16067,1392,616))])}</section>
<section class="row row--inset reveal"{gap(14)}>{ptile('s15',(24,16697,1392,830),'Visual development boards')}</section>
'''
pn=pn.replace(' reveal"', ' reveal" ').replace('" style=','" style=')
page=head('Post Nature — Yuval Shalmon', p['info'][:155])+nav('works')+'<div class="page">\n'+'<main class="case case--pn">'+pn+'</main>\n'+'<div class="endzone">'+CTA_HOME+footer()+'</div>'+'</div>\n'+END
open(f"{ROOT}/work/post-nature/index.html",'w').write(page)
print('post nature rebuilt')


# ---------------- Kanopy + Panorays: page cut into Figma sections; info + headings are live ----------------
from PIL import Image as _Im
def _stitch(slug):
    m=meta[slug]; ims=[_Im.open(f"{ROOT}/assets/work/{n}").convert('RGB') for n,_ in m['parts']]
    full=_Im.new('RGB',(ims[0].width,sum(i.height for i in ims))); y=0
    for i in ims: full.paste(i,(0,y)); y+=i.height
    return full, full.width/1440
def cut_block(slug,full,sc,y0,y1,idx,vids=()):
    os.makedirs(f"{ROOT}/assets/{slug}/cut",exist_ok=True)
    H=y1-y0; parts=[]; y=y0; k=0
    while y<y1:
        ye=min(y1,y+1400); name=f"{idx:02d}-{k}"
        full.crop((0,round(y*sc),full.width,round(ye*sc))).save(f"{ROOT}/assets/{slug}/cut/{name}.webp",quality=86)
        lazy='' if y0<700 else ' loading="lazy"'
        parts.append(f'<img class="tile" src="/assets/{slug}/cut/{name}.webp" width="1440" height="{ye-y}" alt=""{lazy} decoding="async">')
        y=ye; k+=1
    ov=''
    for (cx,cy,cw,ch),(vx,vy,vw,vh),f in vids:
        ov+=(f'<div class="pv" style="left:{cx/1440*100:.4f}%;top:{(cy-y0)/H*100:.4f}%;width:{cw/1440*100:.4f}%;height:{ch/H*100:.4f}%">'
             f'<video src="/assets/video/{slug}/{f}.mp4" style="left:{(vx-cx)/cw*100:.3f}%;top:{(vy-cy)/ch*100:.3f}%;width:{vw/cw*100:.3f}%;height:{vh/ch*100:.3f}%" muted loop playsinline autoplay preload="metadata"></video></div>')
    return f'<section class="row row--full"><div class="stack cut">{"".join(parts)}{ov}</div></section>\n'
def case_info(p,num,role,year):
    tags=''.join(f'<span class="tag">{x}</span>' for x in p['tags'])
    return f'''<div class="case-info case-info--{p['slug']} reveal" style="padding-top:calc(95 * var(--u));padding-bottom:calc(148 * var(--u))">
    <div class="case-info__title"><p class="case-info__num">{num}</p><h1 class="case-info__name">{p['name']}</h1><div class="case-info__tags">{tags}</div></div>
    <div class="case-info__body"><p class="case-label">Info</p><div class="case-text"><p>{INFO[p['slug']]}</p></div>
      <div class="case-meta"><div><p class="case-label">Role</p><p class="case-role">{role}</p></div><div><p class="case-label">Year</p><p>{year}</p></div>{SITES[p['slug']]}</div></div>
  </div>'''
INFO={'kanopy':'A bold cybersecurity brand built for the wild world of no-code and AI-powered business apps. Through a hand-crafted illustration system, vibrant identity, and digital experience, we positioned Kanopy as the guide that brings clarity and order to the jungle.',
      'panorays':'Panorays helps businesses understand and manage cybersecurity risks across their third-party relationships. Built around the idea “Connections that just click,” the brand identity and website translate a complex security world into a bright, approachable experience through expressive illustrations, vibrant gradients, and Pano, the brand’s character.'}
SITES={'kanopy':'<div><p class="case-label">Site</p><p><a class="case-site" href="https://kanopysecurity.com/" target="_blank" rel="noopener">kanopysecurity.com</a></p></div>','panorays':'<div><p class="case-label">Site</p><p><a class="case-site" href="https://panorays.com/" target="_blank" rel="noopener">panorays.com</a></p></div>'}
KV=lambda f,c,v: (c,v,f)
TILES={'kanopy':[[26,1110,682,855],[732,1110,682,855],[26,1989,1390,813],[26,3877,682,855],[732,3877,682,855],[26,4756,1390,615],[26,6507,682,855],[732,6507,682,855],[26,7386,682,855],[732,7386,682,855],[26,8265,682,855],[732,8265,682,855],[26,10211,1390,613],[26,10848,682,855],[732,10848,682,855],[26,11727,682,855],[732,11727,682,855]],
       'panorays':[[24,1110,684,855],[732,1110,684,855],[24,3093,684,855],[732,3093,684,855],[24,5071,684,855],[732,5071,684,855],[24,5950,1392,855],[24,7666,684,683],[732,7666,684,683],[26,10754,682,855],[732,10754,684,855],[26,11633,1390,763]]}
def tile_page(slug,full,sc,start,end,heads,vids):
    """Rebuild a flattened page as real rows: rounded tiles (cropped one by one) + full-width crops for everything else."""
    os.makedirs(f"{ROOT}/assets/{slug}/tiles",exist_ok=True)
    rows={}
    for tl in TILES[slug]: rows.setdefault(tl[1],[]).append(tl)
    items=[(y,'row',sorted(r)) for y,r in rows.items()]+[(y0,'head',(y1,h)) for y0,(y1,h) in heads.items()]
    items.sort(key=lambda x:x[0]); out=''; pos=start; n=0
    def crop(y0,y1):
        nonlocal n; n+=1; name=f"f{n:02d}"
        full.crop((0,round(y0*sc),full.width,round(y1*sc))).save(f"{ROOT}/assets/{slug}/tiles/{name}.webp",quality=86)
        return f'<section class="row row--full row--crop"><img class="tile tile--flat" src="/assets/{slug}/tiles/{name}.webp" width="1440" height="{y1-y0}" alt="" loading="lazy" decoding="async"></section>\n'
    for y,kind,data in items:
        gap=y-pos
        if gap>40: out+=crop(pos,y); gap=0
        mt=f' style="margin-top:calc({max(gap,0)} * var(--u))"'
        if kind=='head':
            y1,h=data; out+=h.replace('<section class="row row--full reveal">',f'<section class="row row--full reveal"{mt}>',1); pos=y1; continue
        r=data; x0=r[0][0]; xr=1440-(r[-1][0]+r[-1][2]); g=(r[1][0]-(r[0][0]+r[0][2])) if len(r)>1 else 0
        cells=''
        for (x,ty,w,h) in r:
            n+=1; name=f"t{n:02d}"
            full.crop((round(x*sc),round(ty*sc),round((x+w)*sc),round((ty+h)*sc))).save(f"{ROOT}/assets/{slug}/tiles/{name}.webp",quality=86)
            ov=''
            for (cx,cy,cw,ch),(vx,vy,vw,vh),f in vids:
                if abs(cx-x)<4 and abs(cy-ty)<4:
                    ov+=(f'<video class="overlay" src="/assets/video/{slug}/{f}.mp4" style="left:{(vx-x)/w*100:.3f}%;top:{(vy-ty)/h*100:.3f}%;width:{vw/w*100:.3f}%;height:{vh/h*100:.3f}%" muted loop playsinline autoplay preload="metadata"></video>')
            cells+=f'<div class="stack clip" style="flex:{w} 1 0"><img class="tile" src="/assets/{slug}/tiles/{name}.webp" width="{w}" height="{h}" alt="" loading="lazy" decoding="async">{ov}</div>'
        cls='row--2' if len(r)>1 else 'row--inset'
        out+=f'<section class="row {cls} row--tiles reveal" style="margin-top:calc({max(gap,0)} * var(--u));--pl:calc({x0} * var(--u));--pr:calc({xr} * var(--u));--g:calc({g} * var(--u))">{cells}</section>\n'
        pos=max(tl[1]+tl[3] for tl in r)
    if end-pos>4: out+=crop(pos,end)
    return out

for slug,num,role,year in [('kanopy','04','Lead Designer - Brand Identity &amp; Web<br>Created at Guts Agency','2025'),('panorays','02','Brand &amp; Digital Designer<br>Created at Guts Agency','2026')]:
    p=P[slug]; full,sc=_stitch(slug)
    body=cut_block(slug,full,sc,0,649,0)
    body=body.replace('<section class="row row--full">','<section class="case-hero">').replace('</div></section>','</div>'+case_info(p,num,role,year)+'</section>')
    if slug=='kanopy':
        h1='<section class="row row--full reveal">'+phead('k1','01 The Brand Idea','We don’t fight the jungle. We understand it.',198,'<p>The jungle became a metaphor for the world Kanopy operates in constantly growing, full of possibility, and increasingly difficult to see through. Rather than framing innovation as the threat, the brand positions Kanopy as the guide that brings visibility, clarity, and order to the wild.</p>',d='kanopy',h=325)+'</section>\n'
        h2='<section class="row row--full reveal">'+phead('k2','02 Crafted by Hand','Built for the AI era. Crafted entirely by hand.',143,'<p>I developed the visual world from scratch, creating the logo, illustration system, plants, animals, objects, and icons by hand. This human-made approach gave the brand a distinctive character in a category increasingly filled with generic, synthetic visuals.</p>',d='kanopy',h=295)+'</section>\n'
        body+=tile_page(slug,full,sc,1110,13209,{2826:(3151,h1),5471:(5766,h2)},[KV('shirt',(732,10848,682,855),(732,10848,682,855)),KV('jungle-logo',(26,1110,682,855),(19,1110,688.7,855)),KV('apps',(732,1110,682,855),(732,1110,684,855)),KV('laptop-wide',(26,1989,1390,813),(18,1989,1406,813)),KV('tools',(26,8265,682,855),(24,8265,684,855)),KV('bottom',(26,11727,682,855),(23.5,11727.3,684,855))])
    else:
        body+=tile_page(slug,full,sc,1110,12441,{},[])
    page=head(f"{p['name']} — Yuval Shalmon", INFO[slug][:155])+nav('works')+'<div class="page">\n<main class="case case--pn case--cut">'+body+'</main>\n'+'<div class="endzone">'+CTA_HOME+footer()+'</div>'+'</div>\n'+END
    open(f"{ROOT}/work/{slug}/index.html",'w').write(page)
print('kanopy + panorays rebuilt')

# ---- cache-bust: /assets/* is cached "immutable" for a year, so stamp every asset URL with a content hash
import hashlib,re as _re,glob as _glob
_hc={}
def _h(path):
    if path not in _hc:
        fp=ROOT+path
        _hc[path]=hashlib.md5(open(fp,'rb').read()).hexdigest()[:8] if os.path.isfile(fp) else None
    return _hc[path]
def _stamp(m):
    attr,path=m.group(1),m.group(2); h=_h(path)
    return f'{attr}="{path}?v={h}"' if h else m.group(0)
for f in _glob.glob(ROOT+'/**/*.html',recursive=True):
    s=open(f).read()
    t=_re.sub(r'(src|poster|href|data-src|data-video)="(/(?:assets|css|js)/[^"?#]+)(?:\?v=[0-9a-f]+)?"',_stamp,s)
    if t!=s: open(f,'w').write(t)
print('assets stamped')
# ---- TRIAL: glass menu (frosted capsule + white segments). Pages listed here get it; empty the list to go back.
GLASS_NAV=[]  # saved glass menu: put 'index.html' (or any page) back here to turn it on
for f in GLASS_NAV:
    fp=f'{ROOT}/{f}'; s=open(fp).read().replace('<nav class="nav" aria-label="Main">','<nav class="nav nav--glass is-compact" aria-label="Main">',1); open(fp,'w').write(s)

