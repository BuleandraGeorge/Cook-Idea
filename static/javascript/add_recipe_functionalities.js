document.getElementById('add-type-add').addEventListener('click', function(){
    newInput=document.createElement('input');
    newInput.setAttribute('placeholder', 'Next type');
    newInput.setAttribute('type', 'text');
    newInput.setAttribute('class', 'validate');
    newInput.setAttribute('name', 'rep_type');
    referenceNode=document.getElementById('add-type-add')
    document.getElementById('add-type-section').insertBefore(newInput, referenceNode);
})
document.getElementById('add-step-add').addEventListener('click', function(){
    newInput=document.createElement('input');
    newInput.setAttribute('placeholder', 'Which\'s next step?');
    newInput.setAttribute('type', 'text');
    newInput.setAttribute('class', 'validate');
    newInput.setAttribute('name', 'rep_step');
    referenceNode=document.getElementById('add-step-add')
    document.getElementById('add-steps-section').insertBefore(newInput, referenceNode);
})
document.getElementById('add-country-add').addEventListener('click', function(){
    newInput=document.createElement('input');
    newInput.setAttribute('placeholder', 'Where else?');
    newInput.setAttribute('type', 'text');
    newInput.setAttribute('class', 'validate');
    newInput.setAttribute('name', 'rep_country');
    referenceNode=document.getElementById('add-country-add')
    document.getElementById('add-country-section').insertBefore(newInput, referenceNode);
})
document.getElementById('add-tool-add').addEventListener('click', function(){
    newInput=document.createElement('input');
    newInput.setAttribute('placeholder', 'Add a tool');
    newInput.setAttribute('type', 'text');
    newInput.setAttribute('class', 'validate');
    newInput.setAttribute('name', 'rep_tool');
    referenceNode=document.getElementById('add-tool-add')
    document.getElementById('add-tools-section').insertBefore(newInput, referenceNode);
})
document.getElementById('add-ingredient-add').addEventListener('click', function(){
    newInput=document.createElement('input');
    newInput.setAttribute('placeholder', 'Add an ingredient');
    newInput.setAttribute('type', 'text');
    newInput.setAttribute('class', 'validate');
    newInput.setAttribute('name', 'rep_igd');
    referenceNode=document.getElementById('add-ingredient-add')
    document.getElementById('add-ingredients-section').insertBefore(newInput, referenceNode);
})


document.getElementById('add-step-del').addEventListener('click', function(){
    referenceNode=document.getElementById('add-step-add')
    list=document.getElementById('add-steps-section').childNodes
    if (list.length > 9)
        {
            list[list.length-5].remove()
    }else {M.toast({html: 'Cannot Delete Initial field'})}
    
})
document.getElementById('add-tool-del').addEventListener('click', function(){
    referenceNode=document.getElementById('add-tool-add')
    list=document.getElementById('add-tools-section').childNodes
    if (list.length > 9)
        {
            list[list.length-5].remove()
    }else {M.toast({html: 'Cannot Delete Initial field'})}
    
})
document.getElementById('add-ingredient-del').addEventListener('click', function(){
    referenceNode=document.getElementById('add-ingredient-add')
    list=document.getElementById('add-ingredients-section').childNodes
    if (list.length > 9)
        {
            list[list.length-5].remove()
    }else {M.toast({html: 'Cannot Delete Initial field'})}
    
})
document.getElementById('add-country-del').addEventListener('click', function(){
    referenceNode=document.getElementById('add-country-add')
    list=document.getElementById('add-country-section').childNodes
    if (list.length > 9)
        {
            list[list.length-5].remove()
    }else {M.toast({html: 'Cannot Delete Initial field'})}
    
})
document.getElementById('add-type-del').addEventListener('click', function(){
    referenceNode=document.getElementById('add-type-add')
    list=document.getElementById('add-type-section').childNodes
    if (list.length > 9)
        {
            list[list.length-5].remove()
    }else {M.toast({html: 'Cannot Delete Initial field'})}
    
})