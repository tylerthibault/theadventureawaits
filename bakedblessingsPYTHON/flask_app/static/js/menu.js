var productBtns = document.querySelectorAll('.product-btn')

for (let btn of productBtns) {
    btn.addEventListener("click", function () {
        toggleMenuDisplay(btn)
    })
}

function toggleMenuDisplay(el) {
    let targetName = el.getAttribute("target")

    for (let btn of productBtns) {
        if (btn === el) {
            btn.classList.remove("bg-white")
            btn.classList.add("bg-bb-color-a", "shadow-white")
        } else {
            btn.classList.add("bg-white")
            btn.classList.remove("bg-bb-color-a", "shadow-white")
        }
    }

    const allTargets = document.querySelectorAll('.product-display')
    console.log(allTargets)
    for (const item of allTargets) {
        if (item.getAttribute("id") != targetName) {
            item.classList.add("hidden")
        } else {
            item.classList.remove("hidden")
        }
    }
}