document.getElementById('add-step-add').addEventListener('click', function(){
    newInput=document.createElement('input');
    newInput.setAttribute('placeholder', 'Which\'s next step?');
    newInput.setAttribute('type', 'text');
    newInput.setAttribute('class', 'validate');
    referenceNode=document.getElementById('add-step-add')
    document.getElementById('add-steps-section').insertBefore(newInput, referenceNode);
})
document.getElementById('add-tool-add').addEventListener('click', function(){
    newInput=document.createElement('input');
    newInput.setAttribute('placeholder', 'Add a tool');
    newInput.setAttribute('type', 'text');
    newInput.setAttribute('class', 'validate');
    referenceNode=document.getElementById('add-tool-add')
    document.getElementById('add-tools-section').insertBefore(newInput, referenceNode);
})
document.getElementById('add-ingredient-add').addEventListener('click', function(){
    newInput=document.createElement('input');
    newInput.setAttribute('placeholder', 'Add an ingredient');
    newInput.setAttribute('type', 'text');
    newInput.setAttribute('class', 'validate');
    referenceNode=document.getElementById('add-ingredient-add')
    document.getElementById('add-ingredients-section').insertBefore(newInput, referenceNode);
})

document.getElementById("edit-button").addEventListener("click", function(){
    content=document.getElementById("recipe-name").innerHTML;
    document.getElementById("recipe-name").innerHTML="<input placeholder=\"Introduce a name for the recipe\" value=\""+content+"\">";
    content=document.getElementById("recipe-description").innerHTML;
    document.getElementById("recipe-description").innerHTML="<textarea placeholder=\"Introduce a description for the recipe\">"+ content +"</textarea>";
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
    document.getElementById("edit-footer").style.display="initial";
})
document.getElementById('delete-recipe-btn').addEventListener('click', function(){
    document.getElementById('delete-modal-msg').style.display='initial';
})
document.getElementById('confirm-btn').addEventListener('click', function(){
    document.getElementById('delete-modal-msg').style.display='none';
})
document.getElementById('cancel-btn').addEventListener('click', function(){
    document.getElementById('delete-modal-msg').style.display='none';
})
