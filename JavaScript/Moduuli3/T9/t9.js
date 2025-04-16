document.getElementById("start").addEventListener("click", function () {
    const input = document.getElementById("calculation").value.trim();
    let result;

    const expression = input.replace(/\s+/g, '');

    if (expression.includes("+")) {
        const [a, b] = expression.split("+").map(n => parseInt(n));
        result = a + b;
    } else if (expression.includes("-")) {
        const [a, b] = expression.split("-").map(n => parseInt(n));
        result = a - b;
    } else if (expression.includes("*")) {
        const [a, b] = expression.split("*").map(n => parseInt(n));
        result = a * b;
    } else if (expression.includes("/")) {
        const [a, b] = expression.split("/").map(n => parseInt(n));
        result = b !== 0 ? Math.floor(a / b) : "Cannot divide by zero";
    } else {
        result = "Invalid format. Use like 3+4 or 10/2";
    }

    document.getElementById("result").textContent = "Result: " + result;
});
