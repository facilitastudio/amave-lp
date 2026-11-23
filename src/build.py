import re,urllib.parse,os
os.chdir(os.path.dirname(os.path.abspath(__file__))+'/..')
src=open('src/index.src.html').read()
logo=open('img/logo.svg').read()
logo=re.sub(r'<svg width="180" height="56"','<svg class="logo"',logo,count=1)
arrow='<svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.2" aria-hidden="true"><path d="M2 8h12M9.5 3.5 14 8l-4.5 4.5"/></svg>'
wa='https://wa.me/5562999515770?text='+urllib.parse.quote('Olá! Vim pelo site e quero saber mais sobre os projetos do Estúdio Amave.')
D=[(0,22,.55),(68,16,.92),(143,30,.89),(245,18,.86),(320,26,.83),(416,14,.80),(485,28,.77),(581,20,.74),(654,24,.71)]
M=[(18,14),(70,20),(128,12),(196,18),(252,14),(310,20),(366,16),None,None]
st=''
for i,((x,w,o),m) in enumerate(zip(D,M)):
    mm=f'--xm:{m[0]/412*100:.2f}%;--wm:{m[1]}px;' if m else '--xm:-100px;--wm:0px;'
    st+=f'<span class="stripe" style="--x:{x}px;--w:{w}px;{mm}opacity:{o};transition-delay:{.15+i*.07:.2f}s"></span>'
faq=[('Será que o investimento realmente vai valer a&nbsp;pena?','Uma identidade com personalidade e valor percebido ajuda sua marca a atrair clientes que valorizam o seu trabalho, sem precisar disputar atenção pelo menor&nbsp;preço.'),
('Será que o estúdio vai compreender a essência do meu&nbsp;negócio?','Todo projeto começa com uma conversa para entender a sua história, os seus objetivos e o momento da marca. É a partir dela que a identidade é&nbsp;construída.'),
('Já contratei profissionais antes e não tive a experiência que&nbsp;esperava.','Nosso atendimento é próximo, consultivo e personalizado, com direção criativa e estratégica em cada projeto e atenção aos&nbsp;detalhes.'),
('Vou ter o suporte e a atenção que meu negócio&nbsp;merece?','Acompanhamos cada marca da concepção até o fortalecimento da presença no digital. Hoje, 15 marcas contam com a nossa gestão de redes há mais de 3&nbsp;anos.')]
fq=''.join(f'<div class="qa open rv" style="--d:{i*.1:.1f}s"><button aria-expanded="true">{q}<span class="sinal" aria-hidden="true"></span></button><div class="resp"><div><p>{a}</p></div></div></div>' for i,(q,a) in enumerate(faq))
out=src.replace('{{LOGO}}',logo).replace('{{ARROW}}',arrow).replace('{{WA}}',wa).replace('{{STRIPES}}',st).replace('{{FAQ}}',fq)
out=out.replace('.stripe{position:absolute;','.stripe{position:absolute;left:var(--x);width:var(--w);')
out=out.replace('.hero__vis{position:absolute;inset:0 0 0 auto;width:calc(100% - var(--pad) - 1140px*.674);min-width:44%;z-index:1}',
 '.hero__vis{position:absolute;top:0;bottom:0;right:0;left:min(calc(var(--pad) + 770px), calc(100vw - 554px));z-index:1}')
out=out.replace('.card{position:absolute;left:4.4%;','.card{position:absolute;left:30px;')
out=out.replace('@media (max-width:1100px){','@media (max-width:1240px){\n  .stripe{left:var(--xm);width:var(--wm)}\n  .hero__vis{left:auto;right:auto;top:auto;bottom:auto}')
symsvg='<svg xmlns="http://www.w3.org/2000/svg" viewBox="-2 -2 61 60"><circle cx="28.5" cy="28" r="29" fill="#F2ECE8"/>'+''.join(re.findall(r'<path[^>]*/>',logo)[1:]).replace('<path','<path fill="currentColor"')+'</svg>'
out=out.replace('{{SYM}}','')
assert '{{' not in out
import re
def nb(m):
    return m.group(1)+'&nbsp;'+m.group(2)+m.group(3)
out=re.sub(r'([^\s<>;]+) ([^\s<>]+)(\s*(?:<br\s*/?>\s*)?</(?:p|h[1-4]|li|summary|blockquote|figcaption|span|a|button|div)>)',nb,out)
out=out.replace('</style>','h1,h2,h3,h4,summary{text-wrap:balance}p,li{text-wrap:pretty}</style>',1)
open('index.html','w').write(out)
sym='<svg xmlns="http://www.w3.org/2000/svg" viewBox="-2 -2 61 60"><circle cx="28.5" cy="28" r="29" fill="#F2ECE8"/>'+''.join(re.findall(r'<path[^>]*/>',logo)[1:])+'</svg>'
open('img/favicon.svg','w').write(sym.replace('<path','<path fill="#875E42"'))
print('ok',len(out))
