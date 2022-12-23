// const allOrderFormSections = document.querySelectorAll(".order-form-section")
// const allOrderNavigations = document.querySelectorAll(".order-form-navigation")


// for (let btn of allOrderNavigations) {
//     btn.addEventListener('click', function(){
//         navigate(btn)
//     })
// }

// function navigate(el){
//     const next = document.querySelector(`div[step="${el.getAttribute("goto")}"]`)
//     const current = findParent(el)
//     update()
//     current.classList.add("hidden")
//     next.classList.remove("hidden")
// }

// function findParent(el){
//     if (el.classList.contains("order-form-section")){
//         return el
//     } else {
//         const parent = el.parentElement
//         return findParent(parent)
//     }
// }

// function update(){

// }

console.log("testing")

var radioPickup = document.querySelectorAll('.radio-pickup')
for (let btn of radioPickup) {
    btn.addEventListener("click", function(){
        const deliveryAddress = document.querySelector("#delivery_address")
        if (btn.value != 1){
            deliveryAddress.classList.remove("hidden")
        } else {
            deliveryAddress.classList.add("hidden")

        }
    })
}