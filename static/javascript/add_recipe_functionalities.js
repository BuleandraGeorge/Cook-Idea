document.getElementById('add-step-add').addEventListener('click', function(){
    newInput=document.createElement('input');
    newInput.setAttribute('placeholder', 'Which\'s next step?');
    newInput.setAttribute('type', 'text');
    newInput.setAttribute('class', 'validate');
    newInput.setAttribute('name', 'rep_step');
    referenceNode=document.getElementById('add-step-add')
    document.getElementById('add-steps-section').insertBefore(newInput, referenceNode);
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
    console.log(list)
    console.log(list.length)
    if (list.length > 9)
        {
            list[list.length-5].remove()
    }else {alert('Cannot to delete the intial field')}
    
})
document.getElementById('add-tool-del').addEventListener('click', function(){
    referenceNode=document.getElementById('add-tool-add')
    list=document.getElementById('add-tools-section').childNodes
    console.log(list)
    console.log(list.length)
    if (list.length > 9)
        {
            list[list.length-5].remove()
    }else {alert('Cannot to delete the intial field')}
    
})
document.getElementById('add-ingredient-del').addEventListener('click', function(){
    referenceNode=document.getElementById('add-ingredient-add')
    list=document.getElementById('add-ingredients-section').childNodes
    console.log(list)
    console.log(list.length)
    if (list.length > 9)
        {
            list[list.length-5].remove()
    }else {alert('Cannot to delete the intial field')}
    
})