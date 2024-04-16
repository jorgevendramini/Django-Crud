console.log("JavaScript code is executing");

document.addEventListener("DOMContentLoaded", function() {
    // Get the deadline input field
    var deadlineInput = document.getElementById("id_deadline");

    // Add an event listener for input events
    deadlineInput.addEventListener("input", function() {
        // Get the current value of the input field
        var value = deadlineInput.value;
        value = value.replace(/\D/g, "");
        if (value.length > 2) {
            value = value.substring(0, 2) + "/" + value.substring(2, 4) + "/" + value.substring(4, 8);
        }
        // Set the modified value back to the input field
        deadlineInput.value = value;
    });

    deadlineInput.addEventListener("keydown", function(event) {
        // Allow backspace, delete, arrow keys, and numeric keys
        if (
            event.key === "Backspace" ||
            event.key === "Enter" ||
            event.key === "Delete" || 
            event.key === "ArrowLeft" || 
            event.key === "ArrowRight" || 
            /^\d$/.test(event.key)
        ) {
            return true;
        } else {
            event.preventDefault();
            return false;
        }
    });
});