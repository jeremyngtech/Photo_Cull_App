var Ue=Object.defineProperty;var Ye=(t,e,n)=>e in t?Ue(t,e,{enumerable:!0,configurable:!0,writable:!0,value:n}):t[e]=n;var ce=(t,e,n)=>(Ye(t,typeof e!="symbol"?e+"":e,n),n);(function(){const e=document.createElement("link").relList;if(e&&e.supports&&e.supports("modulepreload"))return;for(const l of document.querySelectorAll('link[rel="modulepreload"]'))o(l);new MutationObserver(l=>{for(const r of l)if(r.type==="childList")for(const s of r.addedNodes)s.tagName==="LINK"&&s.rel==="modulepreload"&&o(s)}).observe(document,{childList:!0,subtree:!0});function n(l){const r={};return l.integrity&&(r.integrity=l.integrity),l.referrerPolicy&&(r.referrerPolicy=l.referrerPolicy),l.crossOrigin==="use-credentials"?r.credentials="include":l.crossOrigin==="anonymous"?r.credentials="omit":r.credentials="same-origin",r}function o(l){if(l.ep)return;l.ep=!0;const r=n(l);fetch(l.href,r)}})();function E(){}function Qe(t){return t()}function Ce(){return Object.create(null)}function P(t){t.forEach(Qe)}function Re(t){return typeof t=="function"}function he(t,e){return t!=t?e==e:t!==e||t&&typeof t=="object"||typeof t=="function"}function ze(t){return Object.keys(t).length===0}function f(t,e){t.appendChild(e)}function y(t,e,n){t.insertBefore(e,n||null)}function v(t){t.parentNode&&t.parentNode.removeChild(t)}function Z(t,e){for(let n=0;n<t.length;n+=1)t[n]&&t[n].d(e)}function S(t){return document.createElement(t)}function g(t){return document.createTextNode(t)}function C(){return g(" ")}function Be(){return g("")}function Y(t,e,n,o){return t.addEventListener(e,n,o),()=>t.removeEventListener(e,n,o)}function Je(t){return Array.from(t.childNodes)}function k(t,e){e=""+e,t.data!==e&&(t.data=e)}function z(t,e){t.value=e??""}function J(t,e,n){for(let o=0;o<t.options.length;o+=1){const l=t.options[o];if(l.__value===e){l.selected=!0;return}}(!n||e!==void 0)&&(t.selectedIndex=-1)}function Te(t){const e=t.querySelector(":checked");return e&&e.__value}let Se;function R(t){Se=t}const $=[],j=[];let A=[];const de=[],Xe=Promise.resolve();let fe=!1;function Ze(){fe||(fe=!0,Xe.then(qe))}function B(t){A.push(t)}function G(t){de.push(t)}const ue=new Set;let M=0;function qe(){if(M!==0)return;const t=Se;do{try{for(;M<$.length;){const e=$[M];M++,R(e),xe(e.$$)}}catch(e){throw $.length=0,M=0,e}for(R(null),$.length=0,M=0;j.length;)j.pop()();for(let e=0;e<A.length;e+=1){const n=A[e];ue.has(n)||(ue.add(n),n())}A.length=0}while($.length);for(;de.length;)de.pop()();fe=!1,ue.clear(),R(t)}function xe(t){if(t.fragment!==null){t.update(),P(t.before_update);const e=t.dirty;t.dirty=[-1],t.fragment&&t.fragment.p(t.ctx,e),t.after_update.forEach(B)}}function et(t){const e=[],n=[];A.forEach(o=>t.indexOf(o)===-1?e.push(o):n.push(o)),n.forEach(o=>o()),A=e}const U=new Set;let tt;function ae(t,e){t&&t.i&&(U.delete(t),t.i(e))}function Ee(t,e,n,o){if(t&&t.o){if(U.has(t))return;U.add(t),tt.c.push(()=>{U.delete(t),o&&(n&&t.d(1),o())}),t.o(e)}else o&&o()}function O(t){return(t==null?void 0:t.length)!==void 0?t:Array.from(t)}function V(t,e,n){const o=t.$$.props[e];o!==void 0&&(t.$$.bound[o]=n,n(t.$$.ctx[o]))}function ke(t){t&&t.c()}function pe(t,e,n){const{fragment:o,after_update:l}=t.$$;o&&o.m(e,n),B(()=>{const r=t.$$.on_mount.map(Qe).filter(Re);t.$$.on_destroy?t.$$.on_destroy.push(...r):P(r),t.$$.on_mount=[]}),l.forEach(B)}function _e(t,e){const n=t.$$;n.fragment!==null&&(et(n.after_update),P(n.on_destroy),n.fragment&&n.fragment.d(e),n.on_destroy=n.fragment=null,n.ctx=[])}function nt(t,e){t.$$.dirty[0]===-1&&($.push(t),Ze(),t.$$.dirty.fill(0)),t.$$.dirty[e/31|0]|=1<<e%31}function me(t,e,n,o,l,r,s=null,a=[-1]){const c=Se;R(t);const u=t.$$={fragment:null,ctx:[],props:r,update:E,not_equal:l,bound:Ce(),on_mount:[],on_destroy:[],on_disconnect:[],before_update:[],after_update:[],context:new Map(e.context||(c?c.$$.context:[])),callbacks:Ce(),dirty:a,skip_bound:!1,root:e.target||c.$$.root};s&&s(u.root);let p=!1;if(u.ctx=n?n(t,e.props||{},(i,_,...h)=>{const m=h.length?h[0]:_;return u.ctx&&l(u.ctx[i],u.ctx[i]=m)&&(!u.skip_bound&&u.bound[i]&&u.bound[i](m),p&&nt(t,i)),_}):[],u.update(),p=!0,P(u.before_update),u.fragment=o?o(u.ctx):!1,e.target){if(e.hydrate){const i=Je(e.target);u.fragment&&u.fragment.l(i),i.forEach(v)}else u.fragment&&u.fragment.c();e.intro&&ae(t.$$.fragment),pe(t,e.target,e.anchor),qe()}R(c)}class ge{constructor(){ce(this,"$$");ce(this,"$$set")}$destroy(){_e(this,1),this.$destroy=E}$on(e,n){if(!Re(n))return E;const o=this.$$.callbacks[e]||(this.$$.callbacks[e]=[]);return o.push(n),()=>{const l=o.indexOf(n);l!==-1&&o.splice(l,1)}}$set(e){this.$$set&&!ze(e)&&(this.$$.skip_bound=!0,this.$$set(e),this.$$.skip_bound=!1)}}const ot="4";typeof window<"u"&&(window.__svelte||(window.__svelte={v:new Set})).v.add(ot);const x={5036:"1 Western Ave",58381:"784 Memorial Drive",63189:"Barry's Corner (Northbound)",631890:"Barry's Corner (Southbound)",132600:"Cambridge Common",5041:"Harvard Square (Northbound)",58344:"Harvard Square (Southbound)",5040:"Kennedy School (Northbound)",5054:"Kennedy School (Southbound)",5045:"Lamont Library",5042:"Law School (WCC)",6854:"Leverett House",5050:"Mass and Garden",5046:"Mather House",5043:"Maxwell Dworkin",5044:"Memorial Hall",5049:"Quad",23509:"Radcliffe Yard",6248:"Science Center",58343:"SEC",154627:"Sever Gate",5039:"Stadium (Northbound)",23930:"Stadium (Southbound)",5047:"The Inn",5048:"Widener Gate",5051:"Winthrop House"},Oe={5036:[778,5707],58381:[778,790,792,2235,5707],63189:[778,2235,5707],631890:[2235],132600:[777,783,5707],5041:[778,792,2235,5707],58344:[2235],5040:[778,792,2235,5707],5054:[2235],5045:[777,778,783,789,785,792,793,5707],5042:[777,778,783,789,785,790,2235],6854:[777,778,783,789,785,792,5707],5050:[777,783,785,790,2235,792,793],5046:[777,783,789,785,792],5043:[777,778,783,789,785,790],5044:[777,778,783,789,785,790],5049:[777,783,785,790,2235,792,793],23509:[777,783,785,790,2235,792,793],6248:[777,778,783,789,785,790],58343:[778,2235,5707],154627:[5707],5039:[778,5707,778,790,2235,792,5707],23930:[2235],5047:[777,783,789,785],5048:[777,783,2021,789,785,793],5051:[785,792]},X={777:"1636'er",778:"Allston Loop",779:"Barry's Corner",782:"Commencement/Class Day Quad",783:"Crimson Cruiser",3681:"Harvard Square SEC Summer",2021:"HUIT Route",781:"Inauguration Day",786:"Kennedy School Charter AM",787:"Kennedy School Charter PM",788:"Mather Crimson Overnight",789:"Mather Express",785:"Overnight",790:"Quad Express",2235:"Quad SEC Direct",791:"Quad Stadium Direct",792:"Quad Stadium Express",793:"Quad Yard Express",5707:"SEC Express",3679:"Summer Schedule",3680:"Summer School Overnight",2654:"Thanksgiving Day"};function Ne(t,e,n){const o=t.slice();return o[8]=e[n],o}function Le(t){let e,n=t[8]+"",o,l;return{c(){e=S("option"),o=g(n),e.__value=l=t[8],z(e,e.__value)},m(r,s){y(r,e,s),f(e,o)},p(r,s){s&2&&n!==(n=r[8]+"")&&k(o,n),s&2&&l!==(l=r[8])&&(e.__value=l,z(e,e.__value))},d(r){r&&v(e)}}}function lt(t){let e,n,o,l=O(t[1]),r=[];for(let s=0;s<l.length;s+=1)r[s]=Le(Ne(t,l,s));return{c(){e=S("select");for(let s=0;s<r.length;s+=1)r[s].c();t[0]===void 0&&B(()=>t[4].call(e))},m(s,a){y(s,e,a);for(let c=0;c<r.length;c+=1)r[c]&&r[c].m(e,null);J(e,t[0],!0),n||(o=[Y(e,"change",t[4]),Y(e,"change",t[2])],n=!0)},p(s,[a]){if(a&2){l=O(s[1]);let c;for(c=0;c<l.length;c+=1){const u=Ne(s,l,c);r[c]?r[c].p(u,a):(r[c]=Le(u),r[c].c(),r[c].m(e,null))}for(;c<r.length;c+=1)r[c].d(1);r.length=l.length}a&3&&J(e,s[0])},i:E,o:E,d(s){s&&v(e),Z(r,s),n=!1,P(o)}}}function rt(t,e,n){let{startStops:o=[]}=e,{startSelectedStop:l=""}=e,{startSelectedStopID:r=""}=e;const s=Object.entries(x),a=s.map(([i,_])=>_),c=s.map(([i,_])=>i);function u(i){const _=a.indexOf(i.target.value);n(3,r=c[_]),n(0,l=i.target.value)}function p(){l=Te(this),n(0,l),n(1,o)}return t.$$set=i=>{"startStops"in i&&n(1,o=i.startStops),"startSelectedStop"in i&&n(0,l=i.startSelectedStop),"startSelectedStopID"in i&&n(3,r=i.startSelectedStopID)},[l,o,u,r,p]}class st extends ge{constructor(e){super(),me(this,e,rt,lt,he,{startStops:1,startSelectedStop:0,startSelectedStopID:3})}}function Me(t,e,n){const o=t.slice();return o[8]=e[n],o}function $e(t){let e,n=t[8]+"",o,l;return{c(){e=S("option"),o=g(n),e.__value=l=t[8],z(e,e.__value)},m(r,s){y(r,e,s),f(e,o)},p(r,s){s&2&&n!==(n=r[8]+"")&&k(o,n),s&2&&l!==(l=r[8])&&(e.__value=l,z(e,e.__value))},d(r){r&&v(e)}}}function it(t){let e,n,o,l=O(t[1]),r=[];for(let s=0;s<l.length;s+=1)r[s]=$e(Me(t,l,s));return{c(){e=S("select");for(let s=0;s<r.length;s+=1)r[s].c();t[0]===void 0&&B(()=>t[4].call(e))},m(s,a){y(s,e,a);for(let c=0;c<r.length;c+=1)r[c]&&r[c].m(e,null);J(e,t[0],!0),n||(o=[Y(e,"change",t[4]),Y(e,"change",t[2])],n=!0)},p(s,[a]){if(a&2){l=O(s[1]);let c;for(c=0;c<l.length;c+=1){const u=Me(s,l,c);r[c]?r[c].p(u,a):(r[c]=$e(u),r[c].c(),r[c].m(e,null))}for(;c<r.length;c+=1)r[c].d(1);r.length=l.length}a&3&&J(e,s[0])},i:E,o:E,d(s){s&&v(e),Z(r,s),n=!1,P(o)}}}function ct(t,e,n){let{destStops:o=[]}=e,{destSelectedStop:l=""}=e,{destSelectedStopID:r=""}=e;const s=Object.entries(x),a=s.map(([i,_])=>_),c=s.map(([i,_])=>i);function u(i){const _=a.indexOf(i.target.value);n(3,r=c[_]),n(0,l=i.target.value)}function p(){l=Te(this),n(0,l),n(1,o)}return t.$$set=i=>{"destStops"in i&&n(1,o=i.destStops),"destSelectedStop"in i&&n(0,l=i.destSelectedStop),"destSelectedStopID"in i&&n(3,r=i.destSelectedStopID)},[l,o,u,r,p]}class ut extends ge{constructor(e){super(),me(this,e,ct,it,he,{destStops:1,destSelectedStop:0,destSelectedStopID:3})}}const dt="https://corsproxy.io/?https%3A%2F%2Fpassio3.com%2Fharvard%2FpassioTransit%2Fgtfs%2Frealtime%2FvehiclePositions.json",ft=async()=>{try{const e=await(await fetch(dt)).json();return e.entity.forEach(n=>{n.vehicle.stop_id&&(n.vehicle.next_stop_name=x[n.vehicle.stop_id])}),console.log("run"),e}catch{console.error("An error occured")}};function je(t,e,n){const o=t.slice();return o[12]=e[n],o}function Ae(t,e,n){const o=t.slice();return o[15]=e[n],o}function at(t){let e;return{c(){e=S("p"),e.textContent="No common routes found."},m(n,o){y(n,e,o)},p:E,d(n){n&&v(e)}}}function pt(t){let e,n,o,l,r,s,a,c,u=O(t[4]),p=[];for(let i=0;i<u.length;i+=1)p[i]=Fe(Ae(t,u,i));return{c(){e=S("p"),n=g("Common routes between "),o=g(t[2]),l=g(" and "),r=g(t[3]),s=g(":"),a=C(),c=S("ul");for(let i=0;i<p.length;i+=1)p[i].c()},m(i,_){y(i,e,_),f(e,n),f(e,o),f(e,l),f(e,r),f(e,s),y(i,a,_),y(i,c,_);for(let h=0;h<p.length;h+=1)p[h]&&p[h].m(c,null)},p(i,_){if(_&4&&k(o,i[2]),_&8&&k(r,i[3]),_&16){u=O(i[4]);let h;for(h=0;h<u.length;h+=1){const m=Ae(i,u,h);p[h]?p[h].p(m,_):(p[h]=Fe(m),p[h].c(),p[h].m(c,null))}for(;h<p.length;h+=1)p[h].d(1);p.length=u.length}},d(i){i&&(v(e),v(a),v(c)),Z(p,i)}}}function Pe(t){let e,n=X[t[15]]+"",o;return{c(){e=S("li"),o=g(n)},m(l,r){y(l,e,r),f(e,o)},p(l,r){r&16&&n!==(n=X[l[15]]+"")&&k(o,n)},d(l){l&&v(e)}}}function Fe(t){let e,n=X[t[15]]&&Pe(t);return{c(){n&&n.c(),e=Be()},m(o,l){n&&n.m(o,l),y(o,e,l)},p(o,l){X[o[15]]?n?n.p(o,l):(n=Pe(o),n.c(),n.m(e.parentNode,e)):n&&(n.d(1),n=null)},d(o){o&&v(e),n&&n.d(o)}}}function _t(t){let e;return{c(){e=S("li"),e.textContent="Loading..."},m(n,o){y(n,e,o)},p:E,d(n){n&&v(e)}}}function ht(t){let e,n=O(t[5].entity),o=[];for(let l=0;l<n.length;l+=1)o[l]=He(je(t,n,l));return{c(){for(let l=0;l<o.length;l+=1)o[l].c();e=Be()},m(l,r){for(let s=0;s<o.length;s+=1)o[s]&&o[s].m(l,r);y(l,e,r)},p(l,r){if(r&32){n=O(l[5].entity);let s;for(s=0;s<n.length;s+=1){const a=je(l,n,s);o[s]?o[s].p(a,r):(o[s]=He(a),o[s].c(),o[s].m(e.parentNode,e))}for(;s<o.length;s+=1)o[s].d(1);o.length=n.length}},d(l){l&&v(e),Z(o,l)}}}function He(t){let e,n,o=t[12].vehicle.vehicle.id+"",l;return{c(){e=S("li"),n=g("ID: "),l=g(o)},m(r,s){y(r,e,s),f(e,n),f(e,l)},p(r,s){s&32&&o!==(o=r[12].vehicle.vehicle.id+"")&&k(l,o)},d(r){r&&v(e)}}}function St(t){let e,n,o,l,r,s,a,c,u,p,i,_,h,m,b,F,H,N,ee,Q,be,T,ve,te,ye,ne,oe,we,q,L;function Ke(d){t[7](d)}function We(d){t[8](d)}let le={startStops:t[6]};t[2]!==void 0&&(le.startSelectedStop=t[2]),t[0]!==void 0&&(le.startSelectedStopID=t[0]),r=new st({props:le}),j.push(()=>V(r,"startSelectedStop",Ke)),j.push(()=>V(r,"startSelectedStopID",We));function Ge(d){t[9](d)}function Ve(d){t[10](d)}let re={destStops:t[6]};t[3]!==void 0&&(re.destSelectedStop=t[3]),t[1]!==void 0&&(re.destSelectedStopID=t[1]),m=new ut({props:re}),j.push(()=>V(m,"destSelectedStop",Ge)),j.push(()=>V(m,"destSelectedStopID",Ve));function De(d,w){return d[4].length>0?pt:at}let K=De(t),D=K(t);function Ie(d,w){return d[5]&&d[5].entity?ht:_t}let W=Ie(t),I=W(t);return{c(){e=S("body"),n=S("div"),o=S("label"),o.textContent="Start:",l=C(),ke(r.$$.fragment),c=C(),u=S("br"),p=C(),i=S("div"),_=S("label"),_.textContent="Destination:",h=C(),ke(m.$$.fragment),H=C(),N=S("p"),ee=g("Start (Stop ID): "),Q=g(t[0]),be=C(),T=S("p"),ve=g("Destination (Stop ID): "),te=g(t[1]),ye=C(),D.c(),ne=C(),oe=S("p"),oe.textContent="Testing Vehicle Position Data",we=C(),q=S("ul"),I.c()},m(d,w){y(d,e,w),f(e,n),f(n,o),f(n,l),pe(r,n,null),f(e,c),f(e,u),f(e,p),f(e,i),f(i,_),f(i,h),pe(m,i,null),f(e,H),f(e,N),f(N,ee),f(N,Q),f(e,be),f(e,T),f(T,ve),f(T,te),f(e,ye),D.m(e,null),f(e,ne),f(e,oe),f(e,we),f(e,q),I.m(q,null),L=!0},p(d,[w]){const se={};!s&&w&4&&(s=!0,se.startSelectedStop=d[2],G(()=>s=!1)),!a&&w&1&&(a=!0,se.startSelectedStopID=d[0],G(()=>a=!1)),r.$set(se);const ie={};!b&&w&8&&(b=!0,ie.destSelectedStop=d[3],G(()=>b=!1)),!F&&w&2&&(F=!0,ie.destSelectedStopID=d[1],G(()=>F=!1)),m.$set(ie),(!L||w&1)&&k(Q,d[0]),(!L||w&2)&&k(te,d[1]),K===(K=De(d))&&D?D.p(d,w):(D.d(1),D=K(d),D&&(D.c(),D.m(e,ne))),W===(W=Ie(d))&&I?I.p(d,w):(I.d(1),I=W(d),I&&(I.c(),I.m(q,null)))},i(d){L||(ae(r.$$.fragment,d),ae(m.$$.fragment,d),L=!0)},o(d){Ee(r.$$.fragment,d),Ee(m.$$.fragment,d),L=!1},d(d){d&&v(e),_e(r),_e(m),D.d(),I.d()}}}function mt(t,e,n){let o="",l="",r="",s="";const a=Object.values(x);let c=[];function u(b,F){const H=Oe[b],N=Oe[F];return!H||!N?[]:H.filter(Q=>N.includes(Q))}let p={};ft().then(b=>{n(5,p=b),console.log(p,"test"),console.log(typeof p)});function i(b){o=b,n(2,o)}function _(b){l=b,n(0,l)}function h(b){r=b,n(3,r)}function m(b){s=b,n(1,s)}return t.$$.update=()=>{t.$$.dirty&3&&n(4,c=u(l,s))},[l,s,o,r,c,p,a,i,_,h,m]}class gt extends ge{constructor(e){super(),me(this,e,mt,St,he,{})}}new gt({target:document.getElementById("app")});
