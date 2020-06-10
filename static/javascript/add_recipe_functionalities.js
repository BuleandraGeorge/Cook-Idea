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