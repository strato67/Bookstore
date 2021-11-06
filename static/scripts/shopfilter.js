const className = document.getElementsByClassName("shop-container");

//Handles button selection
function shopFilter(selection){
    
    if(selection==='all'){
        visible();
                
    }else{
        cardSelect(selection);
    }
}

//Sets visibility for respective categories
function visible(){
    className[0].style.visibility = "visible";
    var amdArray =  className[0].getElementsByClassName("amd");
    var nArray =  className[0].getElementsByClassName("nvidia");
    for(let i = 0;i<amdArray.length;i++){
        amdArray[i].style.display="grid";
               
    }
    for(let i = 0;i<nArray.length;i++){
        nArray[i].style.display="grid";
        
    }
    
}

//Handles category selection, when a category is selected, visibility of others set to none
function cardSelect(card){
    var amdArray =  className[0].getElementsByClassName("amd");
    var nArray =  className[0].getElementsByClassName("nvidia");
    visible();
    if(card==='amd'){
        
        for(let i = 0;i<nArray.length;i++){
            nArray[i].style.display="none";
        }
    
    }else{
        
        for(let i = 0;i<amdArray.length;i++){
            amdArray[i].style.display="none";
        }
    } 
        
}