document.addEventListener("DOMContentLoaded", function() {
    let deadlineInput = document.getElementById("id_deadline");
    let checkButton = document.getElementById("checkButton");

    deadlineInput.addEventListener("input", function() {
        let value = deadlineInput.value;
        value = value.replace(/\D/g, "");
        if (value.length > 2) {
            value = value.substring(0, 2) + "/" + value.substring(2, 4) + "/" + value.substring(4, 8);
        }
        deadlineInput.value = value;
    });

    checkButton.addEventListener("click", function() {
        const currentDay = () => {
            let currentDate = new Date();
            let day = currentDate.getDate();
            let month = currentDate.getMonth() + 1;
            let year = currentDate.getFullYear();
            return new Date(year, month - 1, day); // Note: month - 1 because months are 0-indexed in Date objects
        }

        let enteredDate = deadlineInput.value;
        enteredDate = enteredDate.split('/').reverse().join('/'); // Convert date to 'yyyy/mm/dd' format for better parsing
        if (new Date(enteredDate) < currentDay()) {
            alert("Please enter a date that is equal to or later than the current date.");
            deadlineInput.value = "";
        }
    });

    deadlineInput.addEventListener("keydown", function(event) {
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
