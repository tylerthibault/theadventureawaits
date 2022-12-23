const allFormAPIBtn = document.querySelectorAll(".form-api-btn")

for (let btn of allFormAPIBtn) {
    btn.addEventListener("click", function () {
        if (btn.getAttribute("target") === "self") {
            handleSelf(btn)
        } else {
            handleForm(btn)
        }
    })
}

function handleSelf(el) {
    apiRoute = el.getAttribute("api")
    methodType = el.getAttribute("method")

    fetch(apiRoute, {
        method: methodType
    })
        .then(resp => resp.json())
        .then(data => {
            console.log(data)
            let afterAction = el.getAttribute("after-action")
            if (afterAction) {
                eval(afterAction)()
            }
        })
        .catch(err => console.log(err))
}

function handleForm(el) {
    apiRoute = el.getAttribute("api")
    methodType = el.getAttribute("method")
    formEl = document.querySelector(`#${el.getAttribute("target")}`)
    
    form = new FormData(formEl)
    fetch(apiRoute, {
        method: 'POST',
        body: form
    })
    .then(resp => resp.json())
    .then(data => {
        console.log(data)
        let afterAction = el.getAttribute("after-action")
            if (afterAction) {
                eval(afterAction)(el)
            }
    })
    .catch(err => console.log(err))
}


// TODO find a better file in which to put this
function updateCart(el) {
    const cartIndicator = document.querySelector("#cart-count")
    let cartIndicatorNum = parseInt(cartIndicator.textContent)
    cartIndicatorNum += 1
    cartIndicator.textContent = cartIndicatorNum
}

function refresh(el){
    window.location.reload();
}

function redirect(el){
    path = el.getAttribute("path")
    
    window.location.href = path
    console.log("redirecting")
}