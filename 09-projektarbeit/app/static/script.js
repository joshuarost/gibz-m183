onload = () => {
    let password = document.getElementById("password");
    let submit = document.getElementById("submit");

    let signUp = document.getElementById("signUp");
    let signIn = document.getElementById("signIn");
    let container = document.getElementById("container");

    signUp.addEventListener('click', () => {
        container.classList.add("right-panel-active");
    });

    signIn.addEventListener('click', () => {
        container.classList.remove("right-panel-active");
    });


    submit.disabled = true;

    let requirements = [
        {id: "length", regex: /.{10,}/g},
        {id: "letter", regex: /[a-z]/g},
        {id: "capital", regex: /[A-Z]/g},
        {id: "number", regex: /[0-9]/g},
        {id: "special", regex: /[!@#/$%^&*(),.?":{}|<>]/g},
    ];

    password.onkeyup = function() {
        let valid = validatePassword(password.value);
        if(valid) {
            submit.disabled = false;
        } else {
            submit.disabled = true;
        }
    }

    function validatePassword(password) {
        let valid = true;

        for(let req of requirements) {
            if(password.match(req.regex)) {
                setCssValid(req.id)
            } else {
                setCssInvalid(req.id)
                valid = false;
            }
        }
        return valid;
    }

    function setCssValid(id) {
        let object = document.getElementById(id)
        object.classList.remove("invalid");
        object.classList.add("valid");
    }

    function setCssInvalid(id) {
        let object = document.getElementById(id)
        object.classList.remove("valid");
        object.classList.add("invalid");
    }

}
