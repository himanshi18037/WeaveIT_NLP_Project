function reset_selected_tab(){var tabs=document.getElementsByClassName("search_tab");var i;for(i=0;i<tabs.length;i++){var tab=tabs[i];if(tab.classList.contains('is-active')){tab.classList.remove('is-active');}}}
function switch_tab(list_element,value){reset_selected_tab();var inputForm=$("#input_form");var searchQuery=$('#search_query');inputForm.attr("action","/results"+value);list_element.classList.add('is-active');if(searchQuery.val()!==''){inputForm.submit();}
var placeHolder="Search for anything on the web";if(value==="/images"){placeHolder="Search for images on the web";}else if(value==="/infinity"){placeHolder="Search infinitely on the web";}
else if(value==="/food"){placeHolder="Search for recipes and food related content on the web";}
else if(value==="/books"){placeHolder="Search for free books on the web";}
else if(value==="/web_monetized"){placeHolder="Search for web monetization enabled pages";}
else if(value==="/reddit"){placeHolder="Search for anything from Reddit";}
else if(value==="/videos"){placeHolder="Search for videos on the web";}
else if(value==="/homepages"){placeHolder="Search for homepages on the web";}
searchQuery.attr("placeholder",placeHolder);}
function setTabsOnLoad(){var customTabsInfo=JSON.parse(localStorage.getItem("infinity_custom_tabs"));if(customTabsInfo==undefined){customTabsInfo=["web","images","videos","homepages","food","books"];}
var tabul=$("#id-results-tabs");var activeString=null;var tabString="";var tabIterator="";tabul.html("");for(var i=0;i<customTabsInfo.length;++i){tabIterator=customTabsInfo[i];activeString=(i===0?" is-active":"");tabString=tabIterator==="web"?"":("/"+tabIterator);if(i===0){$('#input_form').attr('action','/results'+tabString);}
var formattedTitle=tabIterator.charAt(0).toUpperCase()+tabIterator.slice(1);formattedTitle=formattedTitle.replaceAll('_',' ');tabul.append("<li class='search_tab "+activeString+"' onclick='switch_tab(this, \""+tabString+"\");'><a>"+formattedTitle+"</a></li>");}}
function dismissProNotification(){$('#id-pro-sign-in').hide();}
function hideOrShowProNotification(){var proCookie=Cookies.get('InfinityProEmail');var coilCookie=Cookies.get('coil_user');if(proCookie===undefined&&(coilCookie===undefined||coilCookie==='0')){$('#id-pro-sign-in').show();}}
$('.btn_nav').click(function(){$('#footer').addClass('animate_content');$('.page__style').addClass('animate_content');setTimeout(function(){$('#home_content').hide();$('#rabbit_hole').show();$('#rabbit_hole').load('/featured');},1500);setTimeout(function(){$('#footer').removeClass('animate_content');$('.page__style').removeClass('animate_content');},3000);});if(/Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent)){$('#featured_area').hide();}
setTabsOnLoad();hideOrShowProNotification();