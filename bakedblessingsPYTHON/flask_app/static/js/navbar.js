var navBtn = document.querySelector(".nav-btn")
var navMenu = document.querySelector("#nav-menu")

navBtn.addEventListener("click", function(){
    console.log("click")
    toggleMenu()
})

function toggleMenu(){
    if (!navMenu.classList.contains('nav-active')){
        navMenu.classList.remove('opacity-0', 'pointer-events-none')
        navMenu.classList.add('nav-active')
    } else {
        navMenu.classList.add('opacity-0', 'pointer-events-none')
        navMenu.classList.remove('nav-active')
    }
}