// let navitem = document.querySelector('.nav-item');


// navitem.addEventListener('click',function(){
//     alert('You clicked')
//     navitem.classList.add('active');
//     console.log('added active')
// })



// let navitems = document.getElementsByClassName('nav-item');

// for (let i = 0; i < navitems.length; i++) {
//     navitems[i].addEventListener('click', function() {
//         // alert('You clicked')
//         this.classList.add('active');
//         console.log('added active');
//     });
// }



    // Array to store cart items

    // const cartItems = [
    //     { name: "Shirt 1", description: "Cotton T-shirt", price: 44.00, quantity: 1 },
    //     { name: "Shirt 2", description: "Cotton T-shirt", price: 54.00, quantity: 1 },
    //     { name: "Shirt 3", description: "Cotton T-shirt", price: 74.00, quantity: 1 },
    //     { name: "Shirt 3", description: "Cotton T-shirt", price: 74.00, quantity: 1 },
    //     { name: "Shirt 3", description: "Cotton T-shirt", price: 74.00, quantity: 1 },
    //     { name: "Shirt 3", description: "Cotton T-shirt", price: 74.00, quantity: 1 },
    //     { name: "Shirt 3", description: "Cotton T-shirt", price: 74.00, quantity: 1 },
    //     { name: "Shirt 3", description: "Cotton T-shirt", price: 74.00, quantity: 1 },
    //     { name: "Shirt 3", description: "Cotton T-shirt", price: 74.00, quantity: 1 },
    //     { name: "Shirt 3", description: "Cotton T-shirt", price: 74.00, quantity: 1 },
    //     { name: "Shirt 3", description: "Cotton T-shirt", price: 74.00, quantity: 1 },

        
    // ];

    // // Function to update the cart display
    // function updateCartDisplay() {
    //     const cartList = document.querySelector('.cart .items');
    //     cartList.innerHTML = '';

    //     cartItems.forEach((item, index) => {
    //         const itemRow = document.createElement('div');
    //         itemRow.classList.add('row', 'main', 'align-items-center');

    //         itemRow.innerHTML = `
    //             <div class="col-2"><img class="img-fluid" src="https://i.imgur.com/1GrakTl.jpg"></div>
    //             <div class="col">
    //                 <div class="row text-muted">${item.name}</div>
    //                 <div class="row">${item.description}</div>
    //             </div>
    //             <div class="col">
    //                 <a href="#" onclick="decreaseQuantity(${index})">-</a>
    //                 <span class="border">${item.quantity}</span>
    //                 <a href="#" onclick="increaseQuantity(${index})">+</a>
    //             </div>
    //             <div class="col amt-close">&euro; ${item.price.toFixed(2)} <a href="#" onclick="removeItem(${index})" class="close">&#10005;</a></div>
    //         `;

    //         cartList.appendChild(itemRow);
    //     });

    //     updateTotal();
    // }

    // // Function to decrease the quantity of an item
    // function decreaseQuantity(index) {
    //     if (cartItems[index].quantity > 1) {
    //         cartItems[index].quantity--;
    //     }
    //     updateCartDisplay();
    // }


    // // Function to increase the quantity of an item
    // function increaseQuantity(index) {
    //     cartItems[index].quantity++;
    //     updateCartDisplay();
    // }

    // // Function to remove an item from the cart
    // function removeItem(index) {
    //     cartItems.splice(index, 1);
    //     updateCartDisplay();
    // }

    // // Function to calculate and update the total
    // function updateTotal() {
    //     const totalDisplay = document.querySelector('#total');
    //     const total = cartItems.reduce((acc, item) => acc + (item.price * item.quantity), 0);
    //     totalDisplay.textContent = `&euro; ${total.toFixed(2)}`;
    // }

    // // Initial cart display
    // updateCartDisplay(); 


    // check out js
    $("button").click(function () {
        $(".check-icon").hide();
        setTimeout(function () {
          $(".check-icon").show();
        }, 10000);
      });

    // end check out js

    var updatebtns = document.getElementsByClassName('update-cart')
    var user = Request.username
    for (var i = 0; i < updatebtns.length; i++){
        updatebtns[i].addEventListener('click',function(){
            // alert('Update')
            var productId = this.dataset.product
            var action = this.dataset.action
            console.log('productId :',productId, 'action :',action)
            console.log('USER :', user)
            if (user == 'anonymousUser'){
                console.log('user is not authenticated')
            }else{
                console.log('user is authenticated')
            }
        })
    }