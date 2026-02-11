// Shopping Cart
let cart = [];

// Menu hamburguesa
const navToggle = document.getElementById('navToggle');
const navMenu = document.getElementById('navMenu');
const navOverlay = document.getElementById('navOverlay');
const mainNav = document.querySelector('.main-nav');

if (navToggle) {
    navToggle.addEventListener('click', function() {
        navMenu.classList.toggle('active');
        navOverlay.classList.toggle('active');
        mainNav.classList.toggle('active');
        
        // Cambia el icono
        const icon = this.querySelector('i');
        if (navMenu.classList.contains('active')) {
            icon.classList.remove('bi-list');
            icon.classList.add('bi-x');
        } else {
            icon.classList.remove('bi-x');
            icon.classList.add('bi-list');
        }
    });
    
    // Cierra el menú al hacer click en el overlay
    navOverlay.addEventListener('click', function() {
        navMenu.classList.remove('active');
        navOverlay.classList.remove('active');
        mainNav.classList.remove('active');
        const icon = navToggle.querySelector('i');
        icon.classList.remove('bi-x');
        icon.classList.add('bi-list');
    });
    
    // Cierra el menú al hacer click en un enlace
    document.querySelectorAll('.main-nav a').forEach(link => {
        link.addEventListener('click', function() {
            navMenu.classList.remove('active');
            navOverlay.classList.remove('active');
            mainNav.classList.remove('active');
            const icon = navToggle.querySelector('i');
            icon.classList.remove('bi-x');
            icon.classList.add('bi-list');
        });
    });
}

// Get category icon
function getCategoryIcon(category) {
    const icons = {
        'smartphones': 'phone',
        'laptops': 'laptop',
        'tablets': 'tablet',
        'headphones': 'headphones',
        'cameras': 'camera',
        'smartwatches': 'smartwatch'
    };
    return icons[category] || 'box';
}

// Toggle cart
function showCart() {
    document.getElementById('cartDropdown').classList.add('active');
    document.getElementById('cartOverlay').classList.add('active');
}

function hideCart() {
    document.getElementById('cartDropdown').classList.remove('active');
    document.getElementById('cartOverlay').classList.remove('active');
}

document.getElementById('cartToggle').addEventListener('click', showCart);
document.getElementById('closeCart').addEventListener('click', hideCart);
document.getElementById('cartOverlay').addEventListener('click', hideCart);

// View toggle
const gridView = document.getElementById('gridView');
const listView = document.getElementById('listView');
const productsGrid = document.getElementById('productsGrid');

gridView.addEventListener('click', function() {
    productsGrid.classList.remove('list-view');
    gridView.classList.add('active');
    listView.classList.remove('active');
});

listView.addEventListener('click', function() {
    productsGrid.classList.add('list-view');
    listView.classList.add('active');
    gridView.classList.remove('active');
});

// Wishlist functionality
document.querySelectorAll('.wishlist-btn').forEach(btn => {
    btn.addEventListener('click', function() {
        this.classList.toggle('active');
        const icon = this.querySelector('i');
        icon.classList.toggle('bi-heart');
        icon.classList.toggle('bi-heart-fill');
        this.style.color = icon.classList.contains('bi-heart-fill') ? 'var(--primary-color)' : '';
    });
});

// Initialize cart
loadCart();