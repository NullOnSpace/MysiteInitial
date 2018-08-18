function popMsg(msg){
  var body = $("body")[0];
  var bodyHeight = body.clientHeight;
  var bodyWidth = body.clientWidth;
  var popBox = document.createElement("div");
  popBox.classList.add("pop-box");
  popBox.classList.add("hide");
  $(popBox).css("top", bodyHeight/2-30);
  $(popBox).css("left", bodyWidth/2-100);
  $(popBox).text(msg);
  $(body).append(popBox);
  $(popBox).fadeIn(300).delay(1000).fadeOut(300, function(){
    $(this).remove();
  });
}

function getWanderLight(){
  var lightBox = document.createElement("div");
  lightBox.id = 'light-box';
  var i = 8;
  while (i>0){
    var light = document.createElement("span");
    $(light).css('display', 'inline-block');
    $(light).css('height', '10px').css('width', '10px');
    var singleColor = ((i-1)*2).toString(16);
    var lightColor = singleColor.concat(singleColor).concat(singleColor);
    $(light).css('background-color', '#'.concat(lightColor));
    lightBox.appendChild(light);
    i--;
  }
  return lightBox;
}

function stepLightbox(){
  var lightBox = $("#light-box");
  lightBox.children().each(function(){
    var lColor = $(this).css('background-color');
    var rgbHex = lColor.slice(lColor.indexOf('(')+1, lColor.indexOf(')')).split(',')[0];
    var newRgbHex = (parseInt(rgbHex, 16)%16).toString(16);
    var newColor = newRgbHex.concat(newRgbHex).concat(newRgbHex)
    $(this).css('background-color', '#'.concat(newColor));
  })
}

function cookWithDali(info, tms){
  var infHex=parseInt(info, 16);
  var tmsHex=parseInt(tms.toString(16), 16);
  var ret=infHex+tmsHex;
  return ret.toString(16)
}

function userSearch(){
  console.log(222);
  $("#user-head").siblings().remove();
  $('#paginator').remove();
  var ele = getWanderLight();
  $("#searchfo").append(ele);
  lightInterval = window.setInterval(stepLightbox, 200);
  $.ajax({
    url: "/testapp/nickname-get/",
    type: "GET",
    data: $('form').filter('[name="search"]').serialize()+'&page='+$(this).attr('pg'),
    success: function(suda){
      window.clearInterval(lightInterval);
      $(ele).remove()
      console.log(suda);
      var userLine = $("#user-head");
      userLine.siblings().remove();
      for (var userNO in suda.nnlist){
        user = suda.nnlist[userNO];
        console.log(user);
        var newUser = $(document.createElement("tr"));
        newUser.attr("uid", user.uid);
        var userUID = document.createElement("td");
        $(userUID).addClass("res-uid");
        userUID.innerText = user.uid;
        var userNN = document.createElement("td");
        $(userNN).addClass("res-nn");
        userNN.innerText = user.nn;
        var userLV = document.createElement("td");
        $(userLV).addClass("res-lv");
        var userFo = document.createElement("td");
        $(userFo).addClass("button").click(toButton).text("+");
        userLV.innerText = user.lv;
        newUser.append(userUID, userNN, userLV, userFo);
        userLine.parent().append(newUser);
      }
      if ($('#searchfo').has('.paginator')){
        $('#searchfo .paginator').remove();
      }
      var paginator = document.createElement('div');
      $(paginator).addClass('paginator');
      userLine.parents('.pad').append(paginator);
      totalPageNum = suda.ptotal;
      currentPageNum = suda.pcurrent;
      if ((typeof(totalPageNum)=='number')&&(totalPageNum!=0)){
        if ((currentPageNum-1)<3){
          var pageList = []
          for(var i=1;i<=currentPageNum;i++){
            pageList.push(i);
          }
        }else{
          var pageList = [1, '...', currentPageNum-1, currentPageNum];
        }
        pageList2 = []
        if ((totalPageNum-currentPageNum)<3){
          for(var i=currentPageNum;i<=totalPageNum;i++){
            pageList2.push(i)
          }
        }else{
          pageList2 = [currentPageNum, currentPageNum+1, '...', totalPageNum];
        }
        pageList2.shift();
        pageList = pageList.concat(pageList2);
        for (var i in pageList){
          pageEle = document.createElement('span');
          pageEle.classList.add('page');
          pageEle.innerText = pageList[i];
          paginator.appendChild(pageEle);
          if (typeof(pageList[i])=='number'){
            if (pageList[i]==currentPageNum){
              pageEle.style.backgroundColor = '#E00';
            }else{
              pageEle.setAttribute('pg', pageList[i].toString());
              pageEle.style.cursor = 'pointer';
              pageEle.onclick = userSearch;
            }
          }
        }
      }
    }
  })
}

$('#fo-user').find('input:submit').click(function(){
  resList = [];
  var searchText = $(this).parent().children('input:text').get()[0].value;
  console.log(searchText);
  var trEles = $('#fo-user').find('tr').filter('[eid]');
  trEles.each(function(){
    this.style.backgroundColor = 'inherit';
    if ($(this).children('.res-nn').text().search(searchText) != -1){
      resList.push(this);
    }
  })
  if (resList.length>0){
    serFo = 0;
    toHideEle.each(function(){
      this.classList.remove('hide');
    })
    traversalSearch();
  }
})

$('#search-pre').click(function(){
  serFo = ((serFo-1)+resList.length)%resList.length;
  traversalSearch();
})

$('#search-next').click(function(){
  serFo = (serFo+1)%resList.length;
  traversalSearch();
})

$('#search-reset').click(function(){
  toHideEle.each(function(){
    this.classList.add('hide');
  })
  $(resList).each(function(){
    this.style.backgroundColor = 'inherit';
  })
  resList = [];
  $(this).siblings(':text').attr('value', '');
})

function traversalSearch(){
  toHideEle.filter('span').text((serFo+1)+'/'+resList.length);
  $(resList).each(function(){
    this.style.backgroundColor = 'inherit';
  })
  var curFocus = resList[serFo];
  curFocus.style.backgroundColor = 'yellow';
  var tbEle = $(curFocus).parents('table').get()[0];
  if (tbEle.scrollHeight-tbEle.clientHeight>curFocus.offsetTop){
    tbEle.scrollTop = curFocus.offsetTop;
    console.log('attop');
  }else{
    tbEle.scrollTop = curFocus.offsetTop-tbEle.clientHeight+$(curFocus).innerHeight();
    console.log('atbot');
  }
}

toButton = function(){
  var action;
  var food;
  var info;
  var chart=$(this).parentsUntil("table").parent().first().attr("name");
  if ($(this).text()=='-'){
    action='del';
    info=$(this).siblings().first().text();
  } else if ($(this).text()=='+'){
    action='add';
    info=$(this).siblings().first().text();
  } else{
    return false;
  }
  tms=Date.parse(Date());
  food=cookWithDali(info, tms);
  var bigCookie=new Object();
  var cookiesss=document.cookie.split(';');
  for (var cookiePair in cookiesss){
    var cookieArray=cookiesss[cookiePair].split('=');
    var cookey=cookieArray[0];
    var cookieval=cookieArray[1];
    bigCookie[cookey]=cookieval;
  }
  var ele = $(this).parent()
  console.log(bigCookie);
  console.log(food, info, tms, chart, action);
  $.ajax({
    url: "/testapp/management/",
    type: "POST",
    data: {'food': food, 'chart': chart, 'action': action, 'tms': tms,
      'csrfmiddlewaretoken': bigCookie['csrftoken']},
    success: function(suda){
      data=$.parseJSON(suda);
      if (data["res"]=="ss"){
        console.log('sssssss');
        var newEle=ele.clone();
        var bt=newEle.children().last();
        bt.click(toButton);
        var textBt=bt.text();
        var signs="+-";
        bt.text(signs[1-signs.indexOf(textBt)]);
        var one=ele.parents("span").first();
        var another=one.siblings().first();
        var tbEle=another.find('tr').first().parent();
        tbEle.append(newEle);
        ele.remove();
      }else {
        popMsg(data['error']);
      }
      console.log(suda,typeof(suda),tms,'successsssssss');}
  })
}

var resList = [];
var toHideEle = $('#fo-user').find(':text').siblings('.hide');
var serFo = 1;
$(".button").click(toButton);
$("#sub-search").click(userSearch);
