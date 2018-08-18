function index(ele, container){
	for (var i in container){
		if (ele == container[i]){
			return i;
		}
	}
	return -1;
}


function keyIn(key, container){
	for (var i in container){
		if (key == i){
			return true;
		}
	}
	return false;
}


var updatePaginator = function(){
  var paginator = $('#paginator');
  paginator.addClass('paginator');
  var currentPageNum = parseInt($('#paginator').attr('cpage'));
  var totalPageNum = parseInt($('#paginator').attr('tpage'));
  if ((currentPageNum-1)<4){
    var pageList = [];
    for(var i=1;i<=currentPageNum;i++){
      pageList.push(i);
    }
  }else{
    var pageList = [1, '...', currentPageNum-1, currentPageNum];
  }
  var pageList2 = [];
  if ((totalPageNum-currentPageNum)<4){
    for(var i=currentPageNum;i<=totalPageNum;i++){
      pageList2.push(i);
    }
  }else{
    pageList2 = [currentPageNum, currentPageNum+1, '...', totalPageNum];
  }
  pageList2.shift();
  pageList = pageList.concat(pageList2);
  for (var i in pageList){
    var pageEle = document.createElement('a');
    pageEle.classList.add('page');
    pageEle.innerText = pageList[i];
    paginator.append(pageEle);
    if (typeof(pageList[i])=='number'){
      if (pageList[i]==currentPageNum){
        pageEle.style.backgroundColor = '#E00';
      }else{
        pageEle.setAttribute('pg', pageList[i].toString());
        pageEle.style.cursor = 'pointer';
        pageEle.style.textDecoration = 'none';
        pageEle.href = location.pathname+'?page='+pageList[i];
      }
    }
  }
}

function getComments(pid){
	$.ajax({
		url: '/testapp/comment-get/',
		type: 'GET',
		data: {'refid': pid},
		success: function(suda){
			var cmts = suda.cmts;
			var outer = suda.outer;
			var rel = suda.rel;
			var genList = [outer];
			var cList = []
			var eleArray = [$('[pid="'+pid+'"]')];
			var eleParent;
			while(cList != undefined){
				var cid = cList.pop();
				if (cid == undefined){
					eleParent = eleArray.pop();
					cList = genList.pop();
				}else{
					var info = cmts[cid]
					var cmtWrapper = document.createElement('div');
					eleParent.append(cmtWrapper);
					cmtWrapper.classList.add('sub-post');
					$(cmtWrapper).attr('pid', cid);
					var cmtHead = $('.post-head').first().clone();
					cmtHead.children('.post-user').text(info.username);
					cmtHead.children('.post-pubtime').text(info.pubtime);
					var cmtBody = $('.post-body').first().clone();
					cmtBody.children('.post-text').text(info.text);
					var cmtTail = $('.post-tail').first().clone();
					cmtBody.children('.post-thumb').text(info.thumb);
					$(cmtWrapper).append(cmtHead, cmtBody, cmtTail);
					if ((keyIn(cid, rel)) && (rel[cid].length>0)){
						eleArray.push(eleParent);
						eleParent = $(cmtWrapper);
						genList.push(cList);
						cList = rel[cid];
					}
				}
			}
		}
	})
}

var bindCommentClick = function(){
  var resBox = $(this).parents('[pid]').first();
  var post = $(this).parents('.post');
  if (document.getElementById('comment-box')==null){
		getComments(post.attr('pid'));
    var commentBox = document.createElement('div');
    commentBox.id = 'comment-box';
    var newForm = document.createElement('form');
    newForm.action = 'javascript:void(0)';
    var newTextarea = document.createElement('textarea');
    newTextarea.name = 'content';
    newTextarea.maxlength = '140';
    var newSubmit = document.createElement('input');
    newSubmit.type = 'submit';
    newSubmit.value = 'Comment';
    var newInf = document.createElement('input');
    newInf.type = 'hidden';
    newInf.name = 'action';
    newInf.value = 'comment';
    var newRes = document.createElement('input');
    newRes.type = 'hidden';
    newRes.name = 'refid';
    resBox.addClass('res-post');
    newRes.value = resBox.attr('pid');
    var csrf = $('#post-form').children('[name="csrfmiddlewaretoken"]').clone();
    $(newForm).append(csrf);
    $(newForm).append(newTextarea);
    $(newForm).append(newSubmit);
    $(newForm).append(newInf);
    $(newForm).append(newRes);
    $(commentBox).append(newForm);
    resBox.append(commentBox);
  } else{
		var commentBox = document.getElementById('comment-box');
		var refEle = $(commentBox).find('input:hidden').filter('[name="refid"]');
		var preId = refEle.val();
		var prePost = $(commentBox).parents('.post');
		var preBox = $('[pid="'+preId+'"]');
		if (preBox.hasClass('post')){
			if(preBox.attr('pid')==resBox.attr('pid')){
				$(commentBox).remove();
				$('.sub-post').remove();
				$('.res-post').removeClass('res-post');
			}else if(preBox.attr('pid')!=post.attr('pid')){
				$(commentBox).detach();
				$(this).parent().after(commentBox);
				$('.sub-post').remove();
				$('.res-post').removeClass('res-post');
				resBox.addClass('res-post');
				getComments(post.attr('pid'));
				refEle.val(resBox.attr('pid'));
			}else{
				$(commentBox).detach();
				$(this).parent().after(commentBox);
				$('.res-post').removeClass('res-post');
				resBox.addClass('res-post');
				refEle.val(resBox.attr('pid'));
			}
		}else{
			if(preBox.attr('pid')==resBox.attr('pid')){
				$(commentBox).find('textarea').val('');
			}else{
				$(commentBox).detach();
				$(this).parent().after(commentBox);
				if (prePost.attr('pid')!=post.attr('pid')){
					$('.sub-post').remove();
					getComments(post.attr('pid'));
				}
				$('.res-post').removeClass('res-post');
				resBox.addClass('res-post');
				refEle.val(resBox.attr('pid'));
			}
		}
	}
}

var commentSubmit = function(){
	$.ajax({
		url: '/testapp/community/',
		type: 'POST',
		data: $(this).serialize(),
		success: function(suda){
			location.reload();
		}
	})
}

var deleteButtonClick = function(){
  var pid = $(this).parents('[pid]').attr('pid');
  var csrf = $('#post-form').children('[name="csrfmiddlewaretoken"]').clone();
  $.ajax({
    url: '/testapp/community/',
    type: 'POST',
    data: {'action': 'delete', 'pid': pid, 'csrfmiddlewaretoken': csrf.val()},
    success: function(){
      location.reload();
    }
  })
}

updatePaginator();
$('.post').delegate('form', 'submit', commentSubmit);
$('.post').delegate('.post-comment', 'click', bindCommentClick);
$('.post-delete').click(deleteButtonClick);
