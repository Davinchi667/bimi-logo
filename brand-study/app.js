/* live Lagos time — no seconds */
const fmt=new Intl.DateTimeFormat('en-GB',{timeZone:'Etc/GMT-2',hour:'2-digit',minute:'2-digit',hour12:false});
const c1=document.getElementById('clock'),c2=document.getElementById('clock2');
function tick(){const t=fmt.format(new Date());if(c1)c1.textContent=t+' GMT+2';if(c2)c2.textContent=t;}
tick();setInterval(tick,15000);


/* footer marquee — her core skills, duplicated for a seamless loop */
const skills=['Operations Management','Process Improvement','Workflow Design','Project Coordination','SOP Development','Operational Documentation','Customer Operations','CRM Management','Vendor Operations','Business Analysis','Stakeholder Coordination','Process Optimization'];
const trk=document.getElementById('track');if(trk)trk.innerHTML=[...skills,...skills].map(s=>'<span>'+s+'</span>').join('');

/* footer reveal */
const foot=document.querySelector('.end');
new IntersectionObserver((es,o)=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('in');o.unobserve(e.target);}}),{threshold:.25}).observe(foot);
/* fallback: if the tab was backgrounded on load, IntersectionObserver callbacks never ran */
const revealFallback=()=>{if(foot.getBoundingClientRect().top<innerHeight*.85){foot.classList.add('in');removeEventListener('scroll',revealFallback);}};
addEventListener('scroll',revealFallback,{passive:true});

/* copy email */
const toast=document.getElementById('toast');
function say(m){toast.textContent=m;toast.classList.add('on');setTimeout(()=>toast.classList.remove('on'),2200);}
/* mailto: does nothing at all when the OS has no mail handler registered
   (and inside embedded preview panes). Let the link do its job, then check
   whether anything actually happened and fall back to copying the address. */
document.querySelectorAll('a[href^="mailto:"]').forEach(a=>{
  a.addEventListener('click',()=>{
    const mail=a.getAttribute('href').replace('mailto:','');
    let left=false;
    const bail=()=>{left=true;};
    addEventListener('blur',bail,{once:true});
    addEventListener('pagehide',bail,{once:true});
    setTimeout(async()=>{
      removeEventListener('blur',bail);
      if(left||document.hidden)return;          // a mail client opened — done
      try{await navigator.clipboard.writeText(mail);say('No mail app found — address copied: '+mail);}
      catch{say(mail);}
    },700);
  });
});

document.getElementById('totop')?.addEventListener('click',()=>scrollTo({top:0,behavior:'smooth'}));

/* the résumé PDF may not exist yet — don't offer a link that 404s */
const pdf=document.querySelector('a[href$=".pdf"]');
if(pdf){
  pdf.hidden=true;
  fetch(pdf.getAttribute('href'),{method:'HEAD'})
    .then(r=>{if(r.ok)pdf.hidden=false;})
    .catch(()=>{});
}
