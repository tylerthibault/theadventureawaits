var addProductBtn = document.querySelector('#add-product-btn')
addProductBtn.addEventListener("click", function(){
    toggleShow(this)
})

var addCategoryBtn = document.querySelector('#add-category-btn')
addCategoryBtn.addEventListener("click", function(){
    toggleShow(this)
})

function toggleShow(el){
    let targetName = el.getAttribute("target")
    let target = document.querySelector(`#${targetName}`)
    let elArr = el.textContent.split(" ")
    if (target.classList.contains("hidden")){
        target.classList.remove("hidden")
        el.textContent = "Close " + elArr[1]
    } else {
        target.classList.add("hidden")
        el.textContent = "Add " + elArr[1]
    }
}