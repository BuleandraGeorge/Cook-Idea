
document.getElementById('delete-recipe-btn').addEventListener('click', function(){
    document.getElementById('delete-modal-msg').style.display='initial';
})
document.getElementById('confirm-btn').addEventListener('click', function(){
    M.toast({html: 'The recipe has been deleted'});
    document.getElementById('delete-modal-msg').style.display='none';
})
document.getElementById('cancel-btn').addEventListener('click', function(){
    M.toast({html: 'Action cancelled'});
    document.getElementById('delete-modal-msg').style.display='none';
})
