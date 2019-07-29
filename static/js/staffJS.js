function completeOrder(id){
    
    let data = {
       "ID" : parseInt(id)
    }
    
    let ajaxReq = $.ajax({
       url: "/compOrder",
       data: JSON.stringify(data),
       type: 'POST',
       async: true,
       contentType: "application/json; charset=utf-8",
       dataType: "json"
    });
 
    ajaxReq.done(msg=> location.reload(true));
    ajaxReq.fail((jqXHR, status)=>location.reload(true));

 }