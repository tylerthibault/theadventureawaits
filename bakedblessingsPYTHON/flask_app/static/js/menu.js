var productBtns = document.querySelectorAll('.product-btn')

for (let btn of productBtns) {
    btn.addEventListener("click", function(){
        toggleMenuDisplay(btn)
    })
}

function toggleMenuDisplay(el){
    let targetName = el.getAttribute("target")
    const allTargets = document.querySelectorAll('.product-display')
    for (const item of allTargets) {
        if (item.getAttribute("id") != targetName){
            item.classList.add("hidden")
        } else {
            item.classList.remove("hidden")
        }
    }
}