function validateForm() {
    var username = document.getElementsByName("username")[0].value;
    var email = document.getElementsByName("email")[0].value;
    var password = document.getElementsByName("pwd")[0].value;
    var confirm_password = document.getElementsByName("cpwd")[0].value;

    if (username == "") {
        alert("Please enter your username.");
        return false;
    }
    if (email == "") {
        alert("Please enter your email.");
        return false;
    }
    if (password == "") {
        alert("Please enter your password.");
        return false;
    }
    if (confirm_password == "") {
        alert("Please confirm your password.");
        return false;
    }
    if (password != confirm_password) {
        alert("Passwords do not match.");
        return false;
    }

    // Check password strength requirements individually
    if (password.length < 8) {
        alert("Password must be at least 8 characters long.");
        return false;
    }

    if (!/[a-z]/.test(password)) {
        alert("Password must contain at least one lowercase letter.");
        return false;
    }

    if (!/[A-Z]/.test(password)) {
        alert("Password must contain at least one uppercase letter.");
        return false;
    }

    if (!/\d/.test(password)) {
        alert("Password must contain at least one digit.");
        return false;
    }

    if (!/[@$!%*?&]/.test(password)) {
        alert("Password must contain at least one special character (@, $, !, %, *, ?, or &).");
        return false;
    }

    return true;
}

var form = document.querySelector("form");
form.addEventListener("submit", function (event) {
    event.preventDefault();
    if (validateForm()) {
        form.submit();
    }
});
