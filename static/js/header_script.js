 $(document).ready(()=>{
    $(()=> {

        $('#btnSignUp').click(()=>{
            let ajaxReq = $.ajax({
                url: "/signUp",
                data: $('form').serialize(),
                type: 'POST',
            });

            ajaxReq.done(response => done(response));
        });

        $('#login').click(()=>{
            let ajaxReq = $.ajax({
                url: "/login",
                data: $('form').serialize(),
                type: 'POST',
            });

            ajaxReq.done(response => done(response));
        });

        $('#change').click(()=> {
            let ajaxReq = $.ajax({
                url: "/resetPass",
                data: $('form').serialize(),
                type: 'POST',
            });

            ajaxReq.done(response => done(response));
        });

        $('#logout').click(()=>{
            let ajaxReq = $.ajax({
                url: "/logout",
            });

            ajaxReq.done(response => done(response));
        });
        
        function done(response){
            let json = response;
        
            if(json.message){
                $('.form-signin').children('p').remove();
                $('.form-signin').children('br').remove();
                $('.form-signin').append('<br><p style="color:green; font-size:15px;text-align:center">'+json.message+'</p>');
                if(json.redirect !== undefined && json.redirect){
                    setTimeout(()=>{
                        window.location.href = json.redirect;
                    }, 3000);
                }
            } else if(json.error){
                $('.form-signin').children('p').remove();
                $('.form-signin').children('br').remove();
                $('.form-signin').append('<br><p style="color:red; font-size:15px;text-align:center">'+json.error+'</p>');
            }
        }

        $("#inner-accordion, #outer-accordion, #accordion, #inner-accordion-bakery, #staff-accordion, #basket-accordion").accordion({
            collapsible: true,
            heightStyle: "content",
            active: false
        });

        function swapStyle(media) {
            
            if (media.matches) { // If media query matches
                $('#outer-accordion').show();
                $('#basket-accordion').css({'float':'none', 'max-width':'none'});
                
                if($(location).attr('pathname') != '/orders'){
                    $('.card').hide();
                }
 
                $('.basket-products').css('font-size','1.1em');
                $('.total').css('font-size','1.2em');
            } else {
                $('#outer-accordion').hide();
                $('.card').show();
                $('.container').css('max-width', '1200px');
                $('.basket-products').css('font-size','1.5em');
                $('.total').css('font-size','2em');
                $('#basket-accordion').css({'float':'right', 'max-width':'none'});
            }
        }

        function swapSmaller(media) {
            if (media.matches) { // If media query matches
                $('.basket-products').css('font-size','0.8em');
                $('.total').css('font-size','0.9em');
                $('#basket-accordion').css('float','none');
            } else {
                $('.basket-products').css('font-size','1.1em');
                $('.total').css('font-size','2em');
            }
        }
        
        var media = window.matchMedia("(max-width: 990px)")
        var media2 = window.matchMedia("(max-width: 500px)")
        swapStyle(media) // Call listener function at run time
        swapSmaller(media2) // Call listener function at run time
        media.addListener(swapStyle) // Attach listener function on state change
        media2.addListener(swapSmaller) // Attach listener function on state change
        $("#qty option").attr('selected', 'selected'); 

        if($(location).attr('pathname') == '/' || $(location).attr('pathname') == '/account' || $(location).attr('pathname') == '/register'){
            $('.container').css('max-width', '800px');
        }

    });
 });
 
 function getProduct(product_cat) {
    
    let data = {
       'category': product_cat,
    };
    
    let ajaxReq = $.ajax({
        url: "/product_cat",
        type: 'POST',
        contentType: "application/json",
        dataType: 'json',
        async: false, 
        data: JSON.stringify(data)
    });

    ajaxReq.done(response => appendToMenu(product_cat,response));
 }
 
 function appendToMenu(product_cat,product_cat_json){
    let json = product_cat_json;
    try{
       $('#outer-accordion').hide();
       for(let i = Object.keys(json[product_cat]).length; i--;){
          $(".container").append('<div class="card"><center><img class="card-img-top" style="width:195px; height:195px;" align="middle" src="../static/images/'+json[product_cat][i].Product_Image+'\"/><div class="card-body"><h5 class="card-title">'+json[product_cat][i].Product_Name+'</h5><span class="price-new">&pound;'+parseFloat(json[product_cat][i].Price).toFixed(2)+'<br></span><br><form action="/basket" method="post" onsubmit="event.preventDefault(); add_to_basket(&quot;form-'+json[product_cat][i].Product_Name+'&quot;);" id="form-'+json[product_cat][i].Product_Name+'"><input type="hidden" name="Product_ID" id="Product_ID" value="'+parseInt(json[product_cat][i].Product_ID)+'"><input type="hidden" name="Product_Name" id="Product_Name" value="'+json[product_cat][i].Product_Name+'"><input type="hidden" name="Product_Price" id="Product_Price" value="'+parseFloat(json[product_cat][i].Price).toFixed(2)+'">Quantity: <select id="qty" name=\"qty\"><option value=\"1\">1</option><option value=\"2\">2</option><option value=\"3\">3</option><option value=\"4\">4</option>:</select></div><div class="card-footer"><button type=\"submit\" form="form-'+json[product_cat][i].Product_Name+'" id="submit" name="submit" class=\"buttonAsLink\">Add to basket</button></center></form></div></div>');
          $("."+product_cat).append('<table><tr><th>Name</th><th>Price</th></tr><tr><td>'+json[product_cat][i].Product_Name+'</td>\n<td>&pound;'+parseFloat(json[product_cat][i].Price).toFixed(2)+'</td>\n<td><img align=\"middle\" src=\"../static/images/'+json[product_cat][i].Product_Image+'\"/></td>\n<td><form action="/basket" method="post" onsubmit="event.preventDefault(); add_to_basket(&quot;form-'+json[product_cat][i].Product_Name+'&quot;); id="form-'+json[product_cat][i].Product_Name+'"><input type="hidden" name="Product_ID" value="'+parseInt(json[product_cat][i].Product_ID)+'"><input type="hidden" name="Product_Name" value="'+json[product_cat][i].Product_Name+'"><input type="hidden" name="Product_Price" value="'+parseFloat(json[product_cat][i].Price).toFixed(2)+'"><select name=\"qty\"><option value=\"1\">1</option><option value=\"2\">2</option><option value=\"3\">3</option><option value=\"4\">4</option>:</select></div><div class="card-footer"><button type=\"submit\" form="form-'+json[product_cat][i].Product_Name+'" id="submit" class=\"buttonAsLink\">Add to basket</button></form></td>\n<!-- TABLE ROW {$i} END -->\n\n<!-- TABLE FOOTER START -->\n</table>\n<!-- TABLE FOOTER END -->\n<!-- TABLE HTML CODE END -->\n\n');
       }
    } catch(e){
       console.log(e);
    }
 }
 
 function getUserDetails(){
    let ajaxReq = $.ajax({
       url: "/return_user_details",
       type: 'POST',
    });

    ajaxReq.done(response => appendToUserPage(response));
 }
 
 function appendToUserPage(json_response){
    let count = Object.keys(json_response).length;
    $('.container').css('max-width', '800px');
 
    if(count == 1) /* then it's the admin */ {
       $(".userDetails").append('<label for="staff_email" class="sr-only">Email address</label><input style="margin-bottom:10px;" type="email" name="inputEmail" class="form-control" value="'+json_response.account_email+'" disabled>');
    } else {
       
       $(".userDetails").append('<label for="user_full_name" class="sr-only">Full Name</label><input style="margin-bottom:10px;" type="text" name="user_full_name" class="form-control" value="'+json_response.user_forename+ ' ' +json_response.user_surname+'" disabled><label for="email" class="sr-only">Second Name</label><input style="margin-bottom:10px;" type="email" name="email" class="form-control" value="'+json_response.account_email+'" disabled>');
    }
 }
 
 function add_to_basket(form_name){
    let Product_ID = document.getElementById(form_name).elements.namedItem("Product_ID").value;
    let Product_Name = document.getElementById(form_name).elements.namedItem("Product_Name").value;
    let Product_Price = document.getElementById(form_name).elements.namedItem("Product_Price").value;
    let Product_QTY = document.getElementById(form_name).elements.namedItem("qty").value;
 
    let data = {
       "Product_ID": Product_ID,
       "Product_Name": Product_Name,
       "Product_Price": Product_Price,
       "Product_QTY": Product_QTY
    }
 
    let ajaxReq = $.ajax({
       url: "/basket",
       data: JSON.stringify(data),
       type: 'POST',
       contentType: "application/json; charset=utf-8",
       dataType: "json"
    });
 
    ajaxReq.done(msg =>{
 
       if(typeof msg.error != undefined && msg.error){
          alert(msg.error);
       }
 
       location.reload(true);
    });
 
    ajaxReq.fail((jqXHR, status) => location.reload(true));
 }
 
 function remove_from_basket(index_of_item){
 
    let data = {
       "Index" : parseInt(index_of_item)
    }
    
    let ajaxReq = $.ajax({
       url: "/remove_item",
       data: JSON.stringify(data),
       type: 'POST',
       async: true,
       contentType: "application/json; charset=utf-8",
       dataType: "json"
    });
 
    ajaxReq.done(msg => location.reload(true));
    ajaxReq.fail((jqXHR, status) => location.reload(true));
 }
 
 function finaliseOrder(){
    let table_no =  document.getElementById("basket-tbl").elements.namedItem("tblNo").value;
 
    let data = {
       "Table" : parseInt(table_no)
    }
    
    let ajaxReq = $.ajax({
       url: "/finalizeOrder",
       data: JSON.stringify(data),
       type: 'POST',
       contentType: "application/json; charset=utf-8",
       dataType: "json"
    });
 
    ajaxReq.done(msg =>{
       $(".basket").append('<center><hr><br><p style="color:green; font-size:15px;">'+msg.message+'<br>Your order ID is: <b>'+msg.ID+'</b></p></<center>')
       location.reload(true);
    });
 
    ajaxReq.fail((jqXHR, status) => console.log(msg.message));
       //location.reload(true);
 }
 
 function clear_order(){
    let ajaxReq = $.ajax({
       type: "POST",
       url: "/clearOrder"
    });

    ajaxReq.done(response => {
        if (response) {
            window.location.href = '/';
         }
    });
 }
 
 function check_Stat(id){
    let data = {
       "ID" : parseInt(id)
    }
 
    let ajaxReq = $.ajax({
       type: "POST",
       url: "/checkStatus",
       contentType: "application/json; charset=utf-8",
       dataType: "json",
       data: JSON.stringify(data)
    });

    ajaxReq.done(response =>{
        if (response) {
            $(".basket").append('<center><hr><br><p style="color:green; font-size:15px;">'+response.message+'</p></center>');
            clear_order();
        }
    });
 }