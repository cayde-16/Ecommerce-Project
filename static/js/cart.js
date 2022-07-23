var updateBtns = document.getElementsByClassName('update-cart')

for (var i = 0; i < updateBtns.length; i++){
    updateBtns[i].addEventListener('click', function(){
        var productId = this.dataset.product
        var action = this.dataset.action
        console.log('productId:', productId, 'action:', action)

        console.log('USER:', user)
        if(user == 'AnonymousUser'){
            addCookieItem(productId, action)
        }else{
            updateUserOrder(productId, action)
        }
    })
}

function addCookieItem(productId, action){
    console.log('Not logged in')
    cart = {
        1:{'quanity':4},
        4:{'quanity':1},
        6:{'quanity':3}
    }

    if(action == 'add'){
        if(cart[productId] == undefined){
            cart[productId] = {'quanity':1}
        }else{
            cart[productId]['quanity'] += 1
        }
    }

    if(action == 'remove'){
        cart[productId]['quanity'] -= 1

        if(cart[productId]['quanity'] <= 0){
            console.log('Remove Item')
            delete cart[productId]
        }
    }

    console.log('Cart:', cart)
    document.cookie = 'cart=' + JSON.stringify(cart) + ";domain=;path=/"
    location.reload()
}

function updateUserOrder(productId, action){
    console.log('User is logged in, sending data')

    var url = '/update_item/'

    fetch(url,{
        method:'POST',
        headers:{
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body:JSON.stringify({'productId': productId, 'action':action})
    })

    .then((response) =>{
        return response.json()
    })

    .then((data) =>{
        console.log('data:', data)
        location.reload()
    })
}