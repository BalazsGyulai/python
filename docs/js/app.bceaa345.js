(function(t){function e(e){for(var r,s,c=e[0],d=e[1],i=e[2],u=0,p=[];u<c.length;u++)s=c[u],Object.prototype.hasOwnProperty.call(o,s)&&o[s]&&p.push(o[s][0]),o[s]=0;for(r in d)Object.prototype.hasOwnProperty.call(d,r)&&(t[r]=d[r]);l&&l(e);while(p.length)p.shift()();return a.push.apply(a,i||[]),n()}function n(){for(var t,e=0;e<a.length;e++){for(var n=a[e],r=!0,c=1;c<n.length;c++){var d=n[c];0!==o[d]&&(r=!1)}r&&(a.splice(e--,1),t=s(s.s=n[0]))}return t}var r={},o={app:0},a=[];function s(e){if(r[e])return r[e].exports;var n=r[e]={i:e,l:!1,exports:{}};return t[e].call(n.exports,n,n.exports,s),n.l=!0,n.exports}s.m=t,s.c=r,s.d=function(t,e,n){s.o(t,e)||Object.defineProperty(t,e,{enumerable:!0,get:n})},s.r=function(t){"undefined"!==typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(t,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(t,"__esModule",{value:!0})},s.t=function(t,e){if(1&e&&(t=s(t)),8&e)return t;if(4&e&&"object"===typeof t&&t&&t.__esModule)return t;var n=Object.create(null);if(s.r(n),Object.defineProperty(n,"default",{enumerable:!0,value:t}),2&e&&"string"!=typeof t)for(var r in t)s.d(n,r,function(e){return t[e]}.bind(null,r));return n},s.n=function(t){var e=t&&t.__esModule?function(){return t["default"]}:function(){return t};return s.d(e,"a",e),e},s.o=function(t,e){return Object.prototype.hasOwnProperty.call(t,e)},s.p="/";var c=window["webpackJsonp"]=window["webpackJsonp"]||[],d=c.push.bind(c);c.push=e,c=c.slice();for(var i=0;i<c.length;i++)e(c[i]);var l=d;a.push([0,"chunk-vendors"]),n()})({0:function(t,e,n){t.exports=n("56d7")},"56d7":function(t,e,n){"use strict";n.r(e);n("e260"),n("e6cf"),n("cca6"),n("a79d");var r=n("7a23");function o(t,e,n,o,a,s){var c=Object(r["h"])("HelloWorld");return Object(r["e"])(),Object(r["b"])(c,{msg:"Welcome to Your Vue.js App"})}var a=Object(r["m"])("data-v-f0821d88");Object(r["g"])("data-v-f0821d88");var s={class:"setup"},c={class:"container"},d={class:"box"},i=Object(r["d"])("h1",null,"Szín",-1),l=Object(r["d"])("div",{id:"color"},null,-1),u={class:"box"},p=Object(r["d"])("h1",null,"Fényerő",-1),b=Object(r["d"])("div",{id:"brightness"},null,-1),f={class:"box"},h=Object(r["d"])("h1",null,"Mód",-1),j=Object(r["c"])('<option value="man" data-v-f0821d88>MAN</option><option value="auto" data-v-f0821d88>AUTO</option><option value="rainbow" data-v-f0821d88>RAINBOW</option><option value="white" data-v-f0821d88>FEHÉR</option><option value="off" data-v-f0821d88>OFF</option>',5),v={class:"box"},O=Object(r["d"])("h1",null,"Távolság",-1),m={class:"value"},y={class:"box"},g=Object(r["d"])("h1",null,"Hányadik led kapcsoljon be",-1),x={class:"value"};Object(r["f"])();var w=a((function(t,e,n,o,a,w){return Object(r["e"])(),Object(r["b"])("div",s,[Object(r["d"])("div",c,[Object(r["d"])("div",d,[i,l,Object(r["l"])(Object(r["d"])("input",{class:"slider",type:"range",onBlur:e[1]||(e[1]=function(e){return t.changeColor()}),"onUpdate:modelValue":e[2]||(e[2]=function(t){return a.h=t}),min:"0",max:"360",step:"1"},null,544),[[r["k"],a.h]])]),Object(r["d"])("div",u,[p,b,Object(r["l"])(Object(r["d"])("input",{class:"slider",type:"range",onBlur:e[3]||(e[3]=function(e){return t.changeBright()}),"onUpdate:modelValue":e[4]||(e[4]=function(t){return a.v=t}),min:"0",max:"100",step:"10"},null,544),[[r["k"],a.v]])]),Object(r["d"])("div",f,[h,Object(r["l"])(Object(r["d"])("select",{"onUpdate:modelValue":e[5]||(e[5]=function(t){return a.opt=t})},[j],512),[[r["j"],a.opt]])]),Object(r["d"])("div",v,[O,Object(r["d"])("p",m,Object(r["i"])(a.distance),1),Object(r["l"])(Object(r["d"])("input",{class:"slider",type:"range",onBlur:e[6]||(e[6]=function(e){return t.changeDist()}),min:"5",max:"2000",step:"1","onUpdate:modelValue":e[7]||(e[7]=function(t){return a.distance=t})},null,544),[[r["k"],a.distance]])]),Object(r["d"])("div",y,[g,Object(r["d"])("p",x,Object(r["i"])(a.led),1),Object(r["l"])(Object(r["d"])("input",{class:"number",type:"range",onBlur:e[8]||(e[8]=function(e){return t.changeDist()}),min:"1",max:"20",step:"1","onUpdate:modelValue":e[9]||(e[9]=function(t){return a.led=t})},null,544),[[r["k"],a.led]])])])])})),I=n("bc3a"),k=n.n(I),_={name:"HelloWorld",data:function(){return{opt:"off",distance:0,h:0,v:0,led:1}},methods:{setDistanceColor:function(){k.a.put("https://raspberry-8d528-default-rtdb.firebaseio.com/distanceColor.json",{h:parseInt(this.h)})}},watch:{led:function(t){k.a.put("https://raspberry-8d528-default-rtdb.firebaseio.com/led.json",{led:parseInt(t)}),k.a.put("https://raspberry-8d528-default-rtdb.firebaseio.com/opt.json",{opt:this.opt,change:1})},h:function(t){k.a.put("https://raspberry-8d528-default-rtdb.firebaseio.com/color.json",{hex:this.color,h:parseInt(t),v:parseInt(this.v)}),k.a.put("https://raspberry-8d528-default-rtdb.firebaseio.com/distance.json",{maxdistance:parseInt(this.distance)}),k.a.put("https://raspberry-8d528-default-rtdb.firebaseio.com/opt.json",{opt:this.opt,change:1})},v:function(t){k.a.put("https://raspberry-8d528-default-rtdb.firebaseio.com/color.json",{hex:this.color,h:parseInt(this.h),v:parseInt(t)}),k.a.put("https://raspberry-8d528-default-rtdb.firebaseio.com/distance.json",{maxdistance:parseInt(this.distance)}),k.a.put("https://raspberry-8d528-default-rtdb.firebaseio.com/opt.json",{opt:this.opt,change:1})},distance:function(t){k.a.put("https://raspberry-8d528-default-rtdb.firebaseio.com/distance.json",{maxdistance:parseInt(t)})},opt:function(t){k.a.put("https://raspberry-8d528-default-rtdb.firebaseio.com/opt.json",{opt:t,change:1}),k.a.put("https://raspberry-8d528-default-rtdb.firebaseio.com/distance.json",{maxdistance:parseInt(this.distance)})}}};n("ea17");_.render=w,_.__scopeId="data-v-f0821d88";var P=_,B={name:"App",components:{HelloWorld:P}};B.render=o;var M=B;Object(r["a"])(M).mount("#app")},e61d:function(t,e,n){},ea17:function(t,e,n){"use strict";n("e61d")}});
//# sourceMappingURL=app.bceaa345.js.map