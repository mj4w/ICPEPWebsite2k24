var userFunc = document.getElementById("user");
var subMenu = document.getElementById("subMenu");

userFunc.addEventListener("click", function(event) {
    event.stopPropagation(); // Prevent the click event from reaching the document body
    document.getElementById("user-function").style.display = "block";
    document.getElementById("close-user").style.display = "block";
    this.style.display = "none";
});

// Close the user function menu when clicking outside of it
document.addEventListener("click", function(event) {
    var targetElement = event.target;
    
    if (!subMenu.contains(targetElement) && targetElement !== userFunc) {
        // Clicked outside the user function menu and user icon, close the menu
        document.getElementById("user-function").style.display = "none";
        document.getElementById("close-user").style.display = "none";
        userFunc.style.display = "block";
    }
});

function toggleMenu() {
    subMenu.classList.toggle("open-menu");
}

var swiper = new Swiper(".tools-slider", {
    breakpoints: {
        0: {
            slidesPerView: 2,
        },
        768: {
            slidesPerView: 3,
        },
        991: {
            slidesPerView: 4,
        },
    },
    spaceBetween: 30,
    pagination: {
        el: ".swiper-pagination",
        clickable: true,
    },
});
