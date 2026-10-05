import { chromium } from 'playwright-core';
const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome' });
const pages = ['', 'case-dropx', 'case-levvy-box', 'resume'];
for (const vp of [{w:1440,h:900,tag:'desk'},{w:390,h:844,tag:'mob'}]) {
  const p = await b.newPage({...{ viewport:{width:vp.w,height:vp.h}, deviceScaleFactor: vp.tag==='desk'?1:2 }});
  for (const pg of pages) {
    await p.goto('http://localhost:8765/'+(pg?pg+'.html':''), { waitUntil:'networkidle' });
    await p.evaluate(async()=>{for(let y=0;y<document.body.scrollHeight;y+=400){scrollTo(0,y);await new Promise(r=>setTimeout(r,60));}scrollTo(0,0);});
    await p.waitForTimeout(800);
    await p.screenshot({ path:`screens/${vp.tag}-${pg||'home'}-full.png`, fullPage:true });
    if (vp.tag==='desk' && pg==='') {
      const secs = ['.hero','.strip','#about','.sec:not(#work):not(#tools):not(#approach)','#work','#tools','#approach','#book','#contact'];
      for (const [i,s] of secs.entries()) { const el = await p.$(s); if (el) await el.screenshot({ path:`screens/home-${String(i).padStart(2,'0')}-${s.replace(/[^a-z]/g,'')}.png` }); }
      const styles = await p.evaluate(()=>{
        const q=(s)=>{const e=document.querySelector(s); if(!e) return null; const c=getComputedStyle(e); return {font:c.fontFamily,size:c.fontSize,weight:c.fontWeight,ls:c.letterSpacing,lh:c.lineHeight,color:c.color,bg:c.backgroundColor,radius:c.borderRadius,border:c.border,shadow:c.boxShadow,style:c.fontStyle};};
        const sel=['body','.name','.menu a','.eyebrow','h1','h1 em','.pipes span','.strip .n','.strip .t','.band','.band p','.band em','.sticker .box','.lab','h2','h2 em','.row .i','.row h3','.row p','.crow h3','.chip','.go','.tags span','.pill5 h3','.book-card','.btn.solid','.btn.line','.big','.marquee','.track span','.dot','.clock'];
        const r={}; for(const s of sel) r[s]=q(s);
        r.rootVars=[...document.styleSheets].flatMap(ss=>{try{return [...ss.cssRules]}catch{return[]}}).filter(x=>x.selectorText===':root').map(x=>x.cssText);
        r.fontsLoaded=[...document.fonts].filter(f=>f.status==='loaded').map(f=>f.family+' '+f.style+' '+f.weight);
        return r;});
      (await import('fs')).writeFileSync('computed-styles.json', JSON.stringify(styles,null,1));
    }
  }
}
await b.close();
