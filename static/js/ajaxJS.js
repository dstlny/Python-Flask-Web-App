function getProduct(product_cat) {
    category  = product_cat;
    return_response = "";
    data = {
      'category': product_cat,
    };
    $.ajax({
       url: "/product_cat",
       type: 'POST',
       contentType: "application/json",
       dataType: 'json', 
       data: JSON.stringify(data),
       async: false,
       success: function(response) {
         return_response = response
       }
   });
   appendToMenu(category,return_response)
}

function appendToMenu(product_cat,product_cat_json){
   var json = product_cat_json;
   try{
      var count = Object.keys(json[product_cat]).length;
      $('#outer-accordion').hide();
      for(var i=0; i<count; i++){
         if(json[product_cat] == "Bakery"){
            $(".container").append('<div class="card"><center><img class="card-img-top" style="width:195px; height:195px;" align="middle" src="../static/images/'+json[product_cat][i].Product_Image+'\"/><div class="card-body"><h5 class="card-title">'+json[product_cat][i].Product_Name+'</h5><span class="price-new">&pound;'+parseFloat(json[product_cat][i].Price).toFixed(2)+'<br>Category: '+json[product_cat][i].Product_Cat+'</span><br><br><form method=\"get\"><select name=\"bkQty\"><option value=\"1\">1</option><option value=\"2\">2</option><option value=\"3\">3</option><option value=\"4\">4</option>:</select></div><div class="card-footer"><input type=\"hidden\" name=\"bkID\" value=\"'+parseInt(json[product_cat][i].Product_ID)+'\"><button type=\"submit\" class=\"buttonAsLink\">Add to basket</button></center></div></div>');
            $("."+product_cat).append('<table><tr><th>Name</th><th>Price</th></tr><tr><td>'+json[product_cat][i].Product_Name+'</td>\n<td>&pound;'+parseFloat(json[product_cat][i].Price).toFixed(2)+'</td>\n<td><img align=\"middle\" src=\"../static/images/'+json[product_cat][i].Product_Image+'\"/></td>\n<td><form method=\"get\"><select name=\"bkQty\"><option value=\"1\">1</option><option value=\"2\">2</option><option value=\"3\">3</option><option value=\"4\">4</option>:</select><input type=\"hidden\" name=\"bkID\" value=\"'+parseInt(json[product_cat][i].Product_ID)+'\"><button type=\"submit\" class=\"buttonAsLink\">Add to basket</button></form></td>\n<!-- TABLE ROW {$i} END -->\n\n<!-- TABLE FOOTER START -->\n</table>\n<!-- TABLE FOOTER END -->\n<!-- TABLE HTML CODE END -->\n\n');
         } else{
            $(".container").append('<div class="card"><center><img class="card-img-top" style="width:195px; height:195px;" align="middle" src="../static/images/'+json[product_cat][i].Product_Image+'\"/><div class="card-body"><h5 class="card-title">'+json[product_cat][i].Product_Name+'</h5><span class="price-new">&pound;'+parseFloat(json[product_cat][i].Price).toFixed(2)+'<br>Category: '+json[product_cat][i].Product_Cat+'</span><br><br><form method=\"get\"><select name=\"bkQty\"><option value=\"1\">1</option><option value=\"2\">2</option><option value=\"3\">3</option><option value=\"4\">4</option>:</select></div><div class="card-footer"><input type=\"hidden\" name=\"bkID\" value=\"'+parseInt(json[product_cat][i].Product_ID)+'\"><button type=\"submit\" class=\"buttonAsLink\">Add to basket</button></center></div></div>');
            $("."+product_cat).append('<table><tr><th>Name</th><th>Price</th></tr><tr><td>'+json[product_cat][i].Product_Name+'</td>\n<td>&pound;'+parseFloat(json[product_cat][i].Price).toFixed(2)+'</td>\n<td><img align=\"middle\" src=\"../static/images/'+json[product_cat][i].Product_Image+'\"/></td>\n<td><form method=\"get\"><select name=\"bkQty\"><option value=\"1\">1</option><option value=\"2\">2</option><option value=\"3\">3</option><option value=\"4\">4</option>:</select><input type=\"hidden\" name=\"bkID\" value=\"'+parseInt(json[product_cat][i].Product_ID)+'\"><button type=\"submit\" class=\"buttonAsLink\">Add to basket</button></form></td>\n<!-- TABLE ROW {$i} END -->\n\n<!-- TABLE FOOTER START -->\n</table>\n<!-- TABLE FOOTER END -->\n<!-- TABLE HTML CODE END -->\n\n');
         }
      }
   } catch(e){
      console.log(e);
   }
}

function getUserDetails(){
   return_response = "";
   $.ajax({
      url: "/return_deet",
      type: 'POST',
      async: false,
      success: function(response) {
         return_response = response
      }
   });
   appendToUserPage(return_response)
}

function appendToUserPage(json_response){
   json_response =  JSON.parse(json_response)
   var count = Object.keys(json_response).length;

   if(count < 1) /* then it's the admin */ {
       $(".userDetails").append('<label for="staff_email" class="sr-only">Email address</label><input style="margin-bottom:10px;" type="email" name="inputEmail" class="form-control" value="'+json_response['account_email']+'" disabled>');
   } else {
      
      $(".userDetails").append('<label for="user_full_name" class="sr-only">Full Name</label><input style="margin-bottom:10px;" type="text" name="user_full_name" class="form-control" value="'+json_response['user_forename']+ ' ' +json_response['user_surname']+'" disabled><label for="email" class="sr-only">Second Name</label><input style="margin-bottom:10px;" type="email" name="email" class="form-control" value="'+json_response['account_email']+'" disabled>');
   }
}