// Student Performance Prediction System

document.addEventListener("DOMContentLoaded", function () {

    // Welcome Alert
    console.log("Student Performance Prediction System Loaded");

    // Animate Progress Bar
    const progressBar = document.querySelector(".progress-bar");

    if (progressBar) {
        const value = progressBar.innerText;
        progressBar.style.width = value;
    }

    // Form Validation
    const form = document.querySelector("form");

    if (form) {
        form.addEventListener("submit", function (e) {

            const hours = document.querySelector("[name='hours']").value;
            const attendance = document.querySelector("[name='attendance']").value;
            const previous = document.querySelector("[name='previous_score']").value;
            const sleep = document.querySelector("[name='sleep_hours']").value;
            const papers = document.querySelector("[name='papers']").value;

            if (
                hours === "" ||
                attendance === "" ||
                previous === "" ||
                sleep === "" ||
                papers === ""
            ) {
                alert("Please fill all fields.");
                e.preventDefault();
                return;
            }

            if (attendance > 100 || attendance < 0) {
                alert("Attendance should be between 0 and 100");
                e.preventDefault();
            }

            if (previous > 100 || previous < 0) {
                alert("Previous Score should be between 0 and 100");
                e.preventDefault();
            }

        });
    }

});