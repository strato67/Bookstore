const className = document.getElementsByClassName("scontainer");
function shopFilter(selection){
    
    if(selection==='all'){
        visible();
                
    }
    else{
        cardSelect(selection);
    }
}
function visible(){
    className[0].style.visibility = "visible";

    var action =  className[0].getElementsByClassName("Action");
    var adventure =  className[0].getElementsByClassName("Adventure");
    var comics =  className[0].getElementsByClassName("Comics");
    var fantasy =  className[0].getElementsByClassName("Fantasy");
    var fiction =  className[0].getElementsByClassName("Fiction");
    var nonfiction =  className[0].getElementsByClassName("Non-Fiction");

    for(let i = 0;i<action.length;i++){
        action[i].style.display="grid";
               
    }
    for(let i = 0;i<adventure.length;i++){
        adventure[i].style.display="grid";
               
    }
    for(let i = 0;i<comics.length;i++){
        comics[i].style.display="grid";
               
    }
    for(let i = 0;i<fantasy.length;i++){
        fantasy[i].style.display="grid";
               
    }
    for(let i = 0;i<fiction.length;i++){
        fiction[i].style.display="grid";
               
    }
    for(let i = 0;i<nonfiction.length;i++){
        nonfiction[i].style.display="grid";
        
    }
    
}

function cardSelect(card){

    var action =  className[0].getElementsByClassName("Action");
    var adventure =  className[0].getElementsByClassName("Adventure");
    var comics =  className[0].getElementsByClassName("Comics");
    var fantasy =  className[0].getElementsByClassName("Fantasy");
    var fiction =  className[0].getElementsByClassName("Fiction");
    var nonfiction =  className[0].getElementsByClassName("Non-Fiction");

    
    visible();

    if(card==='Fantasy'){
        
        for(let i = 0;i<fiction.length;i++){
            fiction[i].style.display="none";
        }
    
    }else{
        
        for(let i = 0;i<fantasy.length;i++){
            fantasy[i].style.display="none";
        }
    } 
        
}