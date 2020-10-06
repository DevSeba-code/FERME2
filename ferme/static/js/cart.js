var updateBtns = document.getElementsByClassName('update-cart')

for(var i =0;i<updateBtns.length;i++){
    updateBtns[i].addEventListener('click',function(){
        var productoid = this.dataset.producto
        var action = this.dataset.action
        updateOrdenUsuario(productoid,action)
    })
}

function updateOrdenUsuario(productoid,action){
    var url = '/update_producto/'

    fetch(url,{
        method:'POST',
        headers:{
            'Content-Type':'app/json',
            'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify({'productoId':productoid, 'action':action})
    })
    .then((response)=>{
        return response.json()
    })
    .then((data)=>{
        console.log('data:' , data)
        location.reload()
    })
}