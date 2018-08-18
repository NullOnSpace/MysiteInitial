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

function getDm(){
  $.ajax({
    url: "/testapp/dm-get/",
    type: "GET",
    data: { 'rid': rid, 'ts': ts, 'msgno': msgno},
    success: function(suda){
      ts = suda.ts.toString();
      msgno = suda.msgno.toString();
      for (msg in suda.msgpipe){
        dmPool.push(suda.msgpipe[msg]);
      }
    }
  })
}

function getLiving(){
  $.ajax({
    url: "/testapp/living-get/",
    type: "GET",
    success: function(suda){
      $("#roomlist").find(".room").each(function(){
        var rid = $(this).children(".roomno").text();
        var isLv = false;
        for (var i in suda){
          if (suda[i]==rid){
            $(this).children(".idc").removeClass("lived");
            $(this).children(".idc").addClass("living");
            return;
          }
        }
        $(this).children(".idc").removeClass("living");
        $(this).children(".idc").addClass("lived");
        return;
      });
    }
  })
	recentFetchLv = true;
	window.setTimeout(function(){
		recentFetchLv = false;
	}, 10000);
}

function fetchRooms(){
  var rmList = [];
  $("#roomlist").find(".roomno").each(function(){
    rmList.push($(this).text());
  });
  return rmList;
}

function getRmImgs(){
	imgLoaded = false;
  var rmList = fetchRooms();
  imgEleList = new Array(rmList.length);
	var imgListLen = 0;
  for (var i in rmList){
    var rmInfo;
    $.ajax({
      url: '/testapp/room-json-get/',
      type: 'GET',
			data: {'rid': rmList[i]},
      dataType: 'json',
      success: function(suda){
				var imgEle = document.createElement('img');
				imgEle.src = suda.data['room_thumb'];
				imgEle.width = 240;
				imgEleList[index(suda.data['room_id'], rmList)] = imgEle;
				imgListLen += 1;
				if (imgListLen==rmList.length){
					imgLoaded = true;
				}
      },
    })
  }
}

function getRolling(){
  getRmImgs();
  var rollingBox = document.createElement('span');
	var imgBox = document.createElement('span');
	var dotBox = document.createElement('span');
	imgBox.id = 'img-box';
	dotBox.id = 'dot-box';
	rollingBox.id = 'rolling';
	rollingBox.classList.add('pad');
  $('#fyi').append(rollingBox);
	$(rollingBox).append(imgBox);
	$(rollingBox).append(dotBox);
	imgEleItv = window.setInterval(imgElePolling, 1000);
}

function imgEleForm(){
  for (var i in imgEleList){
    var imgEle = imgEleList[i];
		imgEle.classList.add('hide');
    $('#img-box').append(imgEle);
    var imgDotEle = document.createElement('span');
		imgDotEle.style.backgroundColor = 'white';
		imgDotEle.classList.add('dot');
		imgDotEle.onclick = imgDotClick;
    $('#dot-box').append(imgDotEle);
  }
	var leftBt = document.createElement('span');
	leftBt.style.left = '0px';
	leftBt.innerText = '<';
	leftBt.onclick = function(){
		var imgNum = $('#img-box').children().length;
		var nextSlide = $('#img-box').children().eq(
				($('#img-box img').not('.hide').index()-1+imgNum)%imgNum);
		imgSlide(nextSlide);
	};
	var rightBt = document.createElement('span');
	rightBt.style.right = '0px';
	rightBt.innerText = '>';
	rightBt.onclick = imgSlideNext;
	leftBt.classList.add('side-bt');
	rightBt.classList.add('side-bt');
	$('#rolling').append(leftBt, rightBt);
	$('#img-box').children().eq(0).removeClass('hide');
	$('#dot-box').children().eq(0).css('background-color', 'red');
	$('#dot-box').children().eq(0).unbind('click', imgDotClick);
	$('#rolling').mouseenter(function(){
		console.log('ininin');
		console.log(eventList);
		for (var i in eventList){
			window.clearInterval(eventList[i])
		}
		eventList = [];
	});
	$('#rolling').mouseleave(function(){
		console.log('outoutout');
		if (eventList.length==0){
		eventList.push(window.setInterval(imgSlideNext, 2000));
		}
	});
}

function imgElePolling(){
	if (imgLoaded){
		imgEleForm();
		window.clearInterval(imgEleItv);
	}
}

function imgSlide(ns){
	var cSlide = $('#img-box img').not('.hide');
	cSlide.fadeToggle(1000);
	$(ns).fadeToggle(1000);
	$(ns).removeClass('hide').siblings().addClass('hide');
	$('#dot-box').children().eq($(ns).index()).css(
		'background-color', 'red').siblings().css(
		'background-color', 'white');
}

function imgDotClick(){
	var nextSlide = $('#img-box').children().eq($(this).index());
	imgSlide(nextSlide);
}

function imgSlideNext(){
	var imgNum = $('#img-box').children().length;
	$('#img-box').children().stop(true, true);
	var cSlide = $('#img-box img').not('.hide');
	var nextSlide = $('#img-box').children().eq((cSlide.index()+1)%imgNum);
	imgSlide(nextSlide);
}

function popDm(){
  while (true){
    dm = dmPool.shift();
    if (dm == undefined){
      return ;
    }else {
      var ts = parseFloat(dm.ts)*1000;
      if ((ts+10000)<Date.now()){
      }else if ((ts+3000)<Date.now()){
        addDmFall(dm);
      }else{
        dmPool.unshift(dm);
        return;
      }
    }
  }
}

function addDmFall(dm){
  var fallBox = $("#dm-box");
  var dmLine = document.createElement('div');
  var dmNN = document.createElement('span');
  var dmLV = document.createElement('span');
  var dmNL = document.createElement('span');
  var dmTxt = document.createElement('span');
  $(dmLine).addClass('dm').attr('uid', dm.uid);
  $(dmLine).attr('icon', dm.ic);
  $(dmNN).addClass('nickname').text(dm.nn);
  $(dmLV).addClass('level').text(dm.level);
  if (dm.nl != undefined){
    $(dmNL).addClass('noble-lv').text(NobleDict[dm.nl]);
  }
  $(dmTxt).addClass('dmtxt').text(dm.txt);
  $(dmLine).append(dmNN);
  $(dmLine).append(dmLV);
  $(dmLine).append(dmNL);
  $(dmLine).append(dmTxt);
  dmNN.onclick = popUserOpt;
  dmNN.style.cursor = 'pointer';
  var isBlk = false;
  for (var i in blackList){
    if (blackList[i] == dm.uid){
      isBlk = true;
      break;
    }
  }
  if (!isBlk){
    fallBox.append(dmLine);
  }
  for (var i in speFoList){
    if (dm.uid == speFoList[i]){
      var speDmLine = $(dmLine).clone();
      speDmLine.children('.nickname').click(popUserOpt);
      $("#spe-dm-box").append(speDmLine);
      if ($(speDmLine).siblings().length>80){
        var toDelSpeEle = $("#spe-dm-box").children(".dm").eq(1);
        toDelSpeEle.remove();
      }
      var scrollWin = $('#spe-dm-box');
      if (speKeepBot){
        scrollWin.scrollTop(scrollWin[0].scrollHeight-scrollWin[0].clientHeight);
      }else {
      }
      break;
    }
  }
  dmNN.onclick = popUserOpt;
  dmNN.style.cursor = 'pointer';
  var toDelHeight = 0;
  if ($(dmLine).siblings().length>80){
    var toDelEle = fallBox.children(".dm").eq(1);
    toDelEle.remove();
  }
  var scrollWin = $('#dm-box');
  if (keepBottom){
    scrollWin.scrollTop(scrollWin[0].scrollHeight-scrollWin[0].clientHeight);
  }else {
  }
}

function getSpeFollow(){
  $.ajax({
    url: "/testapp/spe-follow-get/",
    type: "GET",
    success: function(suda){
      speFoList = [];
      for (var obj in suda){
        speFoList.push(suda[obj].uid);
      }
    }
  })
}

function cookWithDali(info, tms){
  var infHex=parseInt(info, 16);
  var tmsHex=parseInt(tms.toString(16), 16);
  var ret=infHex+tmsHex;
  return ret.toString(16)
}


function popUserOpt(){
  var oldOne = $("#user-opt");
  if (oldOne != undefined){
    oldOne.remove();
  }
  var userBox = document.createElement("div");
  var isFo = '0';
  var isBlk = '0';
  userBox.id = 'user-opt';
  var uid = $(this).parent().attr('uid');
  $(userBox).css(
      'top', $('#roomdm')[0].clientHeight/2-80).css(
      'left', $('#roomdm')[0].clientWidth/2-100).attr('uid', uid);
  for (var i in speFoList){
    if (uid == speFoList[i]){
      isFo = '1';
      break;
    }
  }
  for (var i in blackList){
    if (uid == blackList[i]){
      isBlk = '1';
      break;
    }
  }
  userBox.setAttribute('isfo', isFo);
  userBox.setAttribute('isblk', isBlk);
  var foBtText = {'1': 'unfo', '0': 'follow'};
  var blkBtText = {'1': 'unshield', '0': 'shield'};
  var userIcon = document.createElement('div');
  userIcon.classList.add('user-icon');
  var iconImg = document.createElement('img');
  iconImg.src = iconURL+$(this).parent().attr('icon')+'_middle.jpg';
  iconImg.height = 60;
  userIcon.appendChild(iconImg);
  var userInfo = document.createElement('div');
  userInfo.classList.add('user-info');
  $(this).parent().children().last().siblings().clone().each(function(){
    userInfo.appendChild(this);
  })
  var foButton = document.createElement('span');
  var blkButton = document.createElement('span');
  foButton.innerText = foBtText[isFo];
  blkButton.innerText = blkBtText[isBlk];
  $(foButton).click(toggleSpeFo);
  $(blkButton).click(toggleBlack);
  userBox.appendChild(userIcon);
  userBox.appendChild(userInfo);
  userBox.appendChild(foButton);
  userBox.appendChild(blkButton);
  foButton.classList.add('opt-button');
  foButton.classList.add('left');
  blkButton.classList.add('opt-button');
  blkButton.classList.add('right');
  $('#roomdm').append(userBox);
  $('#dm-box').one('click', function(){
    $(userBox).remove();
  })
  event.stopPropagation();
}

function toggleBlack(){
  var uid = $("#user-opt").attr('uid');
  if ($('#user-opt').attr('ifblk') == '1'){
    for (var i in blackList){
      if (blackList[i] == uid){
        break;
      }
    }
    blackList.splice(i, 1);
    $(this).text('shield');
    popMsg('Cancel Shield');
    $('#user-opt').attr('ifblk', '0');
  }else{
    blackList.push(uid);
    $(this).text('unshield');
    popMsg('Shield Success');
    $('#user-opt').attr('ifblk', '1');
  }
}

function toggleSpeFo(){
  var action;
  var food;
  var info = $("#user-opt").attr('uid');
  var tms = Date.parse(Date());
  var button = $(this);
  if ($('#user-opt').attr('isfo') == '1'){
    action = 'del';
  }else {
    action = 'add';
  }
  food = cookWithDali(info, tms);
  var bigCookie = new Object();
  var cookiesss = document.cookie.split(';');
  for (var cookiePair in cookiesss){
    var cookieArray=cookiesss[cookiePair].split('=');
    var cookey=cookieArray[0];
    var cookieval=cookieArray[1];
    bigCookie[cookey]=cookieval;
  }
  console.log(food, info, tms, action);
  $.ajax({
    url: "/testapp/management/",
    type: "POST",
    data: {'food': food, 'chart': 'Userfollow', 'action': action, 'tms': tms,
      'csrfmiddlewaretoken': bigCookie['csrftoken']},
    success: function(suda){
      data=$.parseJSON(suda);
      if (data["res"]=="ss"){
        if (action == 'del'){
          $('#user-opt').attr('isfo', '0');
          button.text('follow');
          for (var i in speFoList){
            if (speFoList[i] == info){
              break;
            }
          }
          speFoList.splice(i, 1);
        }else if(action == 'add'){
          $('#user-opt').attr('isfo', '1');
          button.text('unfo');
          speFoList.push(info);
        }
      }else {
        popMsg(data['error']);
      }
    }
  })
}

function roomClick(){
  if ($(this).hasClass('curoom')){
  }else {
    $(this).siblings().removeClass('curoom');
    $(this).addClass('curoom');
    rid = $(this).children('.roomno').text();
    $('#roomdm').children('h3').text('Danmu in '+rid);
    ts = '0';
    msgno = '0';
    dmPool = [];
    if (danmuClaw != undefined){
      window.clearInterval(danmuClaw);
      window.clearInterval(danmuPoper);
      $("#roomdm .dm.hide").siblings().remove();
    }
    danmuClaw = window.setInterval(getDm, 1000);
    danmuPoper = window.setInterval(popDm, 100);
  }
}

var dmScrollEve = function(){
  if ((this.scrollTop != this.scrollHeight-this.clientHeight)&&
      (keepBottom == true)){
    toggleScrollLock();
  }else if ((this.scrollTop == this.scrollHeight-this.clientHeight)&&
      (keepBottom == false)){
    toggleScrollLock();
  }
}

function toggleScrollLock(){
  if (keepBottom==true){
    $('#scroll').text('FreeScroll');
    keepBottom = false;
  }else{
    $('#scroll').text('LockBottom');
    keepBottom = true;
  }
}

function index(mem, ar){
	for (var i in ar){
		if (ar[i]==mem){
			return i;
		}
	}
	return -1;
}

var rid = '57321';
var ts = '0';
var msgno = '0';
var dmPool = [];
var blackList = [];
var eventList = [window.setInterval(imgSlideNext, 2000), ];
var danmuClaw;
var keepBottom = true;
var speKeepBot = true;
var recentFetchLv = false;
var iconURL = 'http://apic.douyucdn.cn/upload/';
var NobleDict={1: '骑士', 2: '子爵', 3: '伯爵', 4: '公爵', 5: '国王', 6: '皇帝', 7: '游侠'};
$('.room').click(roomClick);
$('#scroll').click(toggleScrollLock);
$('#spe-scroll').click(function(){
  if (speKeepBot==true){
    $(this).text('FreeScroll');
    speKeepBot = false;
  }else{
    $(this).text('LockBottom');
    speKeepBot = true;
  }
})
getLiving();
$('#roomlist').mouseenter(function(){
	if (!recentFetchLv){
		getLiving();
	}
});
getSpeFollow();
$('#clear-dm').click(function(){
  $("#roomdm .dm.hide").siblings().remove();
})
$('#spe-clear-dm').click(function(){
  $("#spe-dm-box .dm.hide").siblings().remove();
})
document.getElementById('dm-box').onscroll = dmScrollEve;
getRolling();
