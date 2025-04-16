document.getElementById("start").addEventListener("click", function () {
    const num1 = parseInt(document.getElementById("num1").value);
    const num2 = parseInt(document.getElementById("num2").value);
    const operation = document.getElementById("operation").value;
    let result;

    if (isNaN(num1) || isNaN(num2)) {
        result = "Please enter valid integers.";
    } else {
        switch (operation) {
            case "add":
                result = num1 + num2;
                break;
            case "sub":
                result = num1 - num2;
                break;
            case "multi":
                result = num1 * num2;
                break;
            case "div":
                result = num2 !== 0 ? Math.floor(num1 / num2) : "Cannot divide by zero.";
                break;
            default:
                result = "Unknown operation.";
        }
    }

    document.getElementById("result").textContent = "Result: " + result;
});

