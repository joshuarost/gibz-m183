onload = () => {
    let password = document.getElementById("password");
    let email = document.getElementById("email");
    let submit = document.getElementById("submit");

    let requirements = [
        {id: "length", regex: /.{10,}/g},
        {id: "letter", regex: /[a-z]/g},
        {id: "capital", regex: /[A-Z]/g},
        {id: "number", regex: /[0-9]/g},
        {id: "special", regex: /[!@#/$%^&*(),.?":{}|<>]/g},
    ];

    submit.onclick = function(e) {
        e.preventDefault();
        let output = document.getElementById("output");
        if(!validatePassword(password.value)) {
            output.innerHTML = "Please consider the password requirements"
            return
        }
        const salt = "v4Z@HM6z^!zSii1"
        let hashedPassword = hashPassword(salt, password.value);

        output.innerHTML = "Password Hash: " + hashedPassword;
    }

    password.onkeyup = function() {
        let valid = validatePassword(password.value);
        if(valid) {
            submit.disabled = false;
        } else {
            submit.disabled = true;
        }
    }

    function hashPassword(password, salt) {
        const rounds = 10;
        return dcodeIO.bcrypt.hashSync(combinePassword(salt, password), rounds);
    }

    function combinePassword(salt, password) {
        const pepper = "@qU1t6wgc!oWXnn"
        return pepper + sha256(password) + salt;
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

        if(email.value == password) {
            setCssInvalid("mail")
            valid = false;
        } else {
            setCssValid("mail")
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
