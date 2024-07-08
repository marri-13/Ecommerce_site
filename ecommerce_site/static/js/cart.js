// products/static/js/cart.js
function addToCart(productId) {
    let cart = JSON.parse(localStorage.getItem('cart')) || [];
    cart.push(productId);
    localStorage.setItem('cart', JSON.stringify(cart));
    alert('Product added to cart!');
}

function viewCart() {
    let cart = JSON.parse(localStorage.getItem('cart')) || [];
    console.log('Cart:', cart);
    // Implement cart display logic
}
