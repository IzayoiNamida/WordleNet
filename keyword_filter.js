function static_num() 
{            
    document.getElementById("btnOperate").onclick = function () {                
        var arr = new Array();                
        var items = document.getElementsByName("category");                 
        for (i = 0; i < items.length; i++) {                    
            if (items[i].checked) {                        
                                  
            }                
        }                 
        alert("选择的个数为：" + arr.length);            
    };        
};  

