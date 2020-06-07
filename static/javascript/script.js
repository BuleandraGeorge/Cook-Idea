document.getElementById("edit-button").addEventListener("click", function(){
    content=document.getElementById("recipe-name").innerHTML;
    document.getElementById("recipe-name").innerHTML="<input placeholder=\"Introduce a name for the recipe\" value=\""+content+"\">";
    content=document.getElementById("recipe-description").innerHTML;
    document.getElementById("recipe-description").innerHTML="<input placeholder=\"Introduce a description for the recipe\" value=\""+content+"\">";
    for (node of document.getElementsByClassName("recipe-tool")){
        content=node.innerText;
        node.innerHTML="<input placeholder=\"Introduce a tool for recipe\" value=\""+content+"\">";
    }
    for (node of document.getElementsByClassName("recipe-ingredient")){
        content=node.innerText;
        node.innerHTML="<input placeholder=\"Introduce an ingredient for recipe\" value=\""+content+"\">";
    }
    for (node of document.getElementsByClassName("recipe-step")){
        content=node.innerText;
        node.innerHTML="<input placeholder=\"Introduce a cooking step for recipe\" value=\""+content+"\">";
    }
    document.getElementById("details-footer").style.display="none";
})