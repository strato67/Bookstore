const className = document.getElementsByClassName("scontainer");

var fantasy =  document.getElementById("card");
console.log(fantasy)
//var fiction =  className[0].getElementsByClassName("Fiction");
//var nonfiction =  className[0].getElementsByClassName("Non-Fiction");
//var action =  className[0].getElementsByClassName("Action");
//var adventure =  className[0].getElementsByClassName("Adventure");
//var comics =  className[0].getElementsByClassName("Comics");

//Handles button selection
/*
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

    for(let i = 0;i<fantasy.length;i++){
        fantasy[i].style.display="grid";
               
    }
    for(let i = 0;i<fiction.length;i++){
        fiction[i].style.display="grid";
        
    }
    
}

//Handles category selection, when a category is selected, visibility of others set to none
function cardSelect(genre){
 
    visible();
    if(genre==='Fantasy'){
        
        for(let i = 0;i<fiction.length;i++){
            fiction[i].style.display="none";
        }
    
    }else{
        
        for(let i = 0;i<fantasy.length;i++){
            fantasy[i].style.display="none";
        }
    } 
        
}
*/