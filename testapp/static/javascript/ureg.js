window.onload = function(){
  var exeFun = function(inputEle){
    function _wrap(){
      isSparse=true;
      inputChangeEve(inputEle);
    }
    return _wrap;
  }
  $('input').change(function(){
    if (!isSparse){
      window.clearTimeout(lastTimer);
    }else{
      isSparse = false;
    }
    lastTimer = window.setTimeout(exeFun(this), 500);
  })
}

function inputChangeEve(inputEle){
  dataStr = $(inputEle).parents('form').serialize()+'&check=1&field='+inputEle.name;
        $(inputEle).siblings('[alias]').html('&#x1f4a6;');
  $.ajax({
    url: '/testapp/register/',
    type: 'POST',
    data: dataStr,
    success: function(suda){
      console.log(suda);
      var itemVali = suda.check;
      if (suda.check=='success'){
        $(inputEle).siblings('[alias]').html('&#10004;');
      }else{
        $(inputEle).siblings('[alias]').html('&#10008;'+suda.fieldError.slice(2,-2));
      }
    }
  })
}

var isSparse = true;
