
document.getElementById('delete-recipe-btn').addEventListener('click', function(){
    document.getElementById('delete-modal-msg').style.display='initial';
})
document.getElementById('confirm-btn').addEventListener('click', function(){
    document.getElementById('delete-modal-msg').style.display='none';
})
document.getElementById('cancel-btn').addEventListener('click', function(){
    document.getElementById('delete-modal-msg').style.display='none';
})
